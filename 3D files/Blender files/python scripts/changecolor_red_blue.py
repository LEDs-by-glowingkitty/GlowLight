# create two materials that glow with a strength of 10000
import bpy

# loop through LED light objects and assign materials

for i in range(60):
    # format name with leading zeros
    name = "LED light.{:03d}".format(i)
    
    # select object by name
    ob = bpy.data.objects[name]
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = ob 
    ob.select_set(True)

    # create material
    mat_name = "LED light.{:03d}".format(i)
    mat = bpy.data.materials.new(name=mat_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    output = nodes.get("Material Output")
    emission = nodes.new(type="ShaderNodeEmission")

    # assign material based on index
    if i < 30:
        emission.inputs[0].default_value = (1, 0, 0, 1) # set color to red

    else:
        emission.inputs[0].default_value = (0, 0, 1, 1) # set color to blue
    
    emission.inputs[1].default_value = 10000 # set strength to 10000
    mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
    
    bpy.context.object.active_material = mat # assign material
        
   