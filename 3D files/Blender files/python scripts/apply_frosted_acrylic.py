import bpy

# Create a new material
mat = bpy.data.materials.new("Frosted_Acrylic")

# Set the material to use nodes
mat.use_nodes = True

# Get the material node tree
tree = mat.node_tree

# Clear all the existing nodes
tree.nodes.clear()

# Create a new Principled BSDF node
bsdf = tree.nodes.new("ShaderNodeBsdfPrincipled")

# Set the base color to white
bsdf.inputs["Base Color"].default_value = (1, 1, 1, 1)

# Set the subsurface to 0.05
bsdf.inputs["Subsurface"].default_value = 0.05

# Set the subsurface color to a light pink
bsdf.inputs["Subsurface Color"].default_value = (0.95, 0.8, 0.8, 1)

# Set the roughness to 0.4
bsdf.inputs["Roughness"].default_value = 0.4

# Set the transmission to 0.9
bsdf.inputs["Transmission"].default_value = 0.9

# Set the IOR to 1.49
bsdf.inputs["IOR"].default_value = 1.49

# Create a new output node
output = tree.nodes.new("ShaderNodeOutputMaterial")

# Link the BSDF node to the output node
tree.links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

# Get the mesh object "acrylic tube - frosted"
obj = bpy.data.objects["acrylic tube - frosted"]

# Assign the material to the object
obj.data.materials[0] = mat