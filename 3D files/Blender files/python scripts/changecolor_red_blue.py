import bpy

# Create a red material
red_mat = bpy.data.materials.new("Red")
red_mat.use_nodes = True
red_nodes = red_mat.node_tree.nodes
red_links = red_mat.node_tree.links
red_output = red_nodes.get("Material Output")
red_emission = red_nodes.new(type="ShaderNodeEmission")
red_emission.inputs[0].default_value = (1.0, 0.0, 0.0, 1.0) # Red color
red_emission.inputs[1].default_value = 10000.0 # Strength
red_links.new(red_emission.outputs[0], red_output.inputs[0])

# Create a blue material
blue_mat = bpy.data.materials.new("Blue")
blue_mat.use_nodes = True
blue_nodes = blue_mat.node_tree.nodes
blue_links = blue_mat.node_tree.links
blue_output = blue_nodes.get("Material Output")
blue_emission = blue_nodes.new(type="ShaderNodeEmission")
blue_emission.inputs[0].default_value = (0.0, 0.0, 1.0, 1.0) # Blue color
blue_emission.inputs[1].default_value = 10000.0 # Strength
blue_links.new(blue_emission.outputs[0], blue_output.inputs[0])

# Define the total number of LED lights
total_leds = 60

# Generate a list of names for the LED lights
led_names = ["LED light." + str(i).zfill(3) for i in range(total_leds)]

# Loop through the list of names and assign the materials
for name in led_names:
    # Get the LED number from the name
    led_num = int(name[10:])
    # Get the object with the name
    obj = bpy.data.objects.get(name)
    # Assign the red material to LED lights 000 to 029
    if 0 <= led_num <= 29:
        obj.data.materials.clear()
        obj.data.materials.append(red_mat)
    # Assign the blue material to LED lights 030 to 059
    elif 30 <= led_num <= 59:
        obj.data.materials.clear()
        obj.data.materials.append(blue_mat)
    # Print the name of the LED light and the material assigned to it
    print(name, obj.data.materials[0].name)