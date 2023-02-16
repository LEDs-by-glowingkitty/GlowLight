import bpy

# Create a new material
mat = bpy.data.materials.new("Green LED")

# Enable the use nodes option
mat.use_nodes = True

# Get the node tree of the material
nodes = mat.node_tree.nodes
links = mat.node_tree.links

# Get the material output node
output = nodes.get("Material Output")

# Create an emission node
emission = nodes.new("ShaderNodeEmission")

# Set the emission color to green using RGB values
emission.inputs["Color"].default_value = (0.0, 1.0, 0.0, 1.0)

# Set the emission strength to 10000.0
emission.inputs["Strength"].default_value = 10000.0

# Connect the emission output to the material output
links.new(emission.outputs["Emission"], output.inputs["Surface"])

# Get all the objects in the scene
objects = bpy.data.objects

# Loop through the objects
for obj in objects:

    # Check if the object name starts with "LED light"
    if obj.name.startswith("LED light"):

        # Check if the object is a mesh
        if obj.type == "MESH":

            # Assign the new material to the object
            obj.data.materials[0] = mat