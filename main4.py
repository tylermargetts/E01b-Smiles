#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(800, 600, "Smiley Face Example")
arcade.set_background_color(open_color.white)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()


#start at 100, go to 799, counting by 150
for x in range(100,800,150):
        #start at 100, go to 599, counting by 150
        for y in range(100,600,150):
                face_x,face_y = (x,y)
                smile_x,smile_y = (face_x + 0,face_y - 15)
                eye1_x,eye1_y = (face_x - 35,face_y + 35) 
                eye2_x,eye2_y = (face_x + 35,face_y + 35)
                catch1_x,catch1_y = (face_x - 30,face_y + 45) 
                catch2_x,catch2_y = (face_x + 40,face_y + 45) 


                # Draw the smiley face:
                # (x,y,radius,color)
                arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)
                # (x,y,radius,color,border_thickness)
                arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)

                #(x,y,width,height,color)
                arcade.draw_ellipse_filled(eye1_x,eye1_y,30,50,open_color.black)
                arcade.draw_ellipse_filled(eye2_x,eye2_y,30,50,open_color.black)
                arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
                arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)

                #(x,y,width,height,color,start_degrees,end_degrees,border_thickness)
                arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)


# Finish the render
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()
