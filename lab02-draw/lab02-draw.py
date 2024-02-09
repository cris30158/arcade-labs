import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

arcade.draw_rectangle_filled(0, 0, 10000, 500, arcade.color.SHAMROCK_GREEN) #suelo

arcade.draw_ellipse_filled(480,190,255,129,arcade.color.LA_SALLE_GREEN	,10) #sombra


arcade.draw_ellipse_filled(270,270,20,70,arcade.color.BLACK,40)
arcade.draw_rectangle_filled(300, 245, 20, 70, arcade.color.BLACK,310)

arcade.draw_rectangle_filled(230, 300, 30, 100, arcade.color.LIGHT_SLATE_GRAY,310)
arcade.draw_triangle_filled(205, 341, 186, 316, 165, 355, arcade.color.LIGHT_SLATE_GRAY)

arcade.draw_rectangle_filled(230, 300, 1, 100, arcade.color.SPANISH_GRAY,310)

arcade.draw_rectangle_filled(400, 240, 190, 80, arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(440, 240, 105, 80, arcade.color.FOREST_GREEN)

arcade.draw_ellipse_filled(312,262,40,129,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_ellipse_filled(488,262,40,129,arcade.color.FOREST_GREEN)
arcade.draw_rectangle_filled(400, 200, 190, 10, arcade.color.FOREST_GREEN)

arcade.draw_ellipse_filled(400, 300, 200,189, arcade.color.DARK_PASTEL_GREEN) #circulo principal
arcade.draw_ellipse_filled(340,300,20,70,arcade.color.BLACK) #ojos
arcade.draw_ellipse_filled(420,300,20,70,arcade.color.BLACK)



#correccion esquinas xd:
arcade.draw_arc_outline(470, 235, 100, 100,arcade.color.LA_SALLE_GREEN	, 20, 100,40,240)
arcade.draw_arc_outline(340, 230, 110, 100,arcade.color.SHAMROCK_GREEN, 20, 100,40,160)





arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

