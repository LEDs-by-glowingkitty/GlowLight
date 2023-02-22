import bpy
import math

# Step 1: duplicate the mesh object "LED light" 14 times on the z-axis with a +16.66mm distance between each duplicate
led_light = bpy.data.objects["LED light.000"] # get the original LED light object
led_lights = [led_light] # create a list to store the LED light objects
for i in range(1, 15): # loop 14 times
    new_led_light = led_light.copy() # make a copy of the original LED light
    new_led_light.location.z += i * 0.01666 # move the copy on the z-axis by 16.66mm times the loop index
    bpy.context.collection.objects.link(new_led_light) # link the copy to the current collection
    led_lights.append(new_led_light) # add the copy to the list

# Step 2: Select all LED lights and duplicate them around a circle that has an 11mm radius. The end result is 4 LED strips of 15 LED lights each. Every LED strip is rotatet 45 degrees (z-axis) in relation to the previous LED strip.
led_strips = [led_lights] # create a list to store the LED strips
for j in range(1, 4): # loop 3 times
    new_led_strip = [] # create a list to store the new LED strip
    for k in range(15): # loop 15 times
        new_led_light = led_lights[k].copy() # make a copy of the LED light at the same index in the original LED strip
        new_led_light.data = led_light.data.copy() # make a copy of the mesh data
        angle = math.radians(j * 90) # calculate the angle of rotation in radians
        new_led_light.rotation_euler.z += angle # rotate the copy on the z-axis by the angle
        new_led_light.location.x = led_lights[k].location.x * math.cos(angle) - led_lights[k].location.y * math.sin(angle) # move the copy on the x-axis by the matrix multiplication of the original LED light location and the rotation matrix
        new_led_light.location.y = led_lights[k].location.x * math.sin(angle) + led_lights[k].location.y * math.cos(angle) # move the copy on the y-axis by the matrix multiplication of the original LED light location and the rotation matrix
        bpy.context.collection.objects.link(new_led_light) # link the copy to the current collection
        new_led_strip.append(new_led_light) # add the copy to the new LED strip
    led_strips.append(new_led_strip) # add the new LED strip to the list