import bpy
import random

# Define a list of RGB values for the fire colors
fire_colors = [(1.0, 0.0, 0.0, 1.0), # Red
               (1.0, 0.5, 0.0, 1.0), # Orange
               (1.0, 1.0, 0.0, 1.0), # Yellow
               (0.8, 0.8, 0.8, 1.0)] # White

# Get the number of fire colors
num_colors = len(fire_colors)

# Get all the objects in the scene
objects = bpy.data.objects

# Create a list to store the heat values for each LED light
heat = []

# Initialize the heat values to zero
for obj in objects:
    if obj.name.startswith("LED light"):
        heat.append(0)

# Loop through the objects
for i, obj in enumerate(objects):

    # Check if the object name starts with "LED light"
    if obj.name.startswith("LED light"):

        # Check if the object is a mesh
        if obj.type == "MESH":

            # Get the material of the object
            mat = obj.data.materials[0]

            # Check if the material is using the Eevee or Cycles render engine
            if mat.use_nodes and mat.node_tree:

                # Get the node tree of the material
                nodes = mat.node_tree.nodes
                links = mat.node_tree.links

                # Get the emission node
                emission = nodes.get("Emission")

                # Check if the emission node exists and has a color input
                if emission and emission.inputs.get("Color"):

                    # Step 1: All cells cool down a little bit, losing heat to the air
                    cooling = random.randint(0, 3)
                    heat[i] = max(0, heat[i] - cooling)

                    # Step 2: The heat from each cell drifts 'up' and diffuses a little
                    if i < len(objects) - 1:
                        heat[i] = (heat[i] + heat[i + 1]) / 2

                    # Step 3: Sometimes randomly new 'sparks' of heat are added at the bottom
                    if i == 0 and random.randint(0, 255) < 120:
                        heat[i] = random.randint(160, 255)

                    # Step 4: The heat from each cell is rendered as a color into the leds array
                    # Map the heat value to a color index
                    color_index = int(heat[i] / 256.0 * num_colors)

                    # Clamp the color index to the range of fire colors
                    color_index = min(num_colors - 1, max(0, color_index))

                    # Set the emission color to the fire color
                    emission.inputs["Color"].default_value = fire_colors[color_index]

                else:
                    # Print an error message if the emission node is not found or has no color input
                    print(f"Error: Emission node not found or has no color input for object {obj.name}")

            else:
                # Print an error message if the material is not using the Eevee or Cycles render engine
                print(f"Error: Material {mat.name} is not using the Eevee or Cycles render engine for object {obj.name}")

# Update the scene
bpy.context.view_layer.update()