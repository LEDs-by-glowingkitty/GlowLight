import bpy

# Define a list of RGB values for the rainbow colors
rainbow_colors = [(1.0, 0.0, 0.0, 1.0), # Red
                  (1.0, 0.5, 0.0, 1.0), # Orange
                  (1.0, 1.0, 0.0, 1.0), # Yellow
                  (0.0, 1.0, 0.0, 1.0), # Green
                  (0.0, 0.0, 1.0, 1.0), # Blue
                  (0.5, 0.0, 1.0, 1.0), # Indigo
                  (1.0, 0.0, 1.0, 1.0)] # Violet

# Get the number of rainbow colors
num_colors = len(rainbow_colors)

# Get all the objects in the scene
objects = bpy.data.objects

# Initialize a counter for the rainbow colors
color_index = 0

# Loop through the objects
for obj in objects:

    # Check if the object name starts with "LED light"
    if obj.name.startswith("LED light"):

        # Check if the object is a mesh
        if obj.type == "MESH":

            # Create a new material with the object name
            mat = bpy.data.materials.new(obj.name)

            # Enable the use nodes option
            mat.use_nodes = True

            # Get the node tree of the material
            nodes = mat.node_tree.nodes
            links = mat.node_tree.links

            # Get the material output node
            output = nodes.get("Material Output")

            # Create an emission node
            emission = nodes.new("ShaderNodeEmission")

            # Set the emission color to the current rainbow color
            emission.inputs["Color"].default_value = rainbow_colors[color_index]

            # Set the emission strength to 10000.0
            emission.inputs["Strength"].default_value = 10000.0

            # Connect the emission output to the material output
            links.new(emission.outputs["Emission"], output.inputs["Surface"])

            # Assign the new material to the object
            obj.data.materials[0] = mat

            # Increment the color index by one
            color_index += 1

            # Wrap the color index around the number of colors
            color_index %= num_colors