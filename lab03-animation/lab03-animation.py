import arcade


def draw_grass():
    """ Draw the ground """
    arcade.draw_rectangle_filled(0, 0, 10000, 500, arcade.color.SHAMROCK_GREEN)  # suelo


def draw_slime(x,y,w,h,verde,oscuro,espada):
    arcade.draw_ellipse_filled(w*480+x, h*190+y, 255*w, 129*h, arcade.color.LA_SALLE_GREEN, 10)  # sombra

    arcade.draw_ellipse_filled(w*270+x, h*270+y, 20*w, 70*h, arcade.color.BLACK, 40)
    arcade.draw_rectangle_filled(w*300+x, h*245+y, 20*w, 70*h, arcade.color.BLACK, 310)

    arcade.draw_rectangle_filled(w*230+x, h*300+y, 30*w, 100*h, espada, 310)  #cambiar por -50
    arcade.draw_triangle_filled(w*205+x, h*341+y, w*186+x, h*316+y, w*165+x, h*355+y, espada)

    arcade.draw_rectangle_filled(w*230+x, h*300+y, 1*w, 100*h, arcade.color.SPANISH_GRAY, 310)

    arcade.draw_rectangle_filled(w*400+x, h*240+y, 190*w, 80*h, verde)
    arcade.draw_rectangle_filled(w*440+x, h*240+y, 105*w, 80*h, oscuro)

    arcade.draw_ellipse_filled(w*312+x, h*262+y, 40*w, 129*h, verde)
    arcade.draw_ellipse_filled(w*488+x, h*262+y, 40*w, 129*h, oscuro)
    arcade.draw_rectangle_filled(w*400+x, h*200+y, 190*w, 10*h, oscuro)

    arcade.draw_ellipse_filled(w*400+x, h*300+y, 200*w, 189*h, verde)  # circulo principal
    arcade.draw_ellipse_filled(w*340+x, h*300+y, 20*w, 70*h, arcade.color.BLACK)  # ojos
    arcade.draw_ellipse_filled(w*420+x, h*300+y, 20*w, 70*h, arcade.color.BLACK)

    # correccion esquinas xd:
    arcade.draw_arc_outline(w*470+x, h*235+y, 100*w, 100*h, arcade.color.LA_SALLE_GREEN, 20, 100, w*40, 240)
    arcade.draw_arc_outline(w*340+x, h*230+y, 110*w, 100*h, arcade.color.SHAMROCK_GREEN, 20, 100, w*40, 160)


def main():

    # Open up a window.
    # From the "arcade" library, use a function called "open_window"
    # Set the window title to "Drawing Example"
    # Set the and dimensions (width and height)
    arcade.open_window(800, 600, "Drawing Example")


    # Get ready to draw

    arcade.set_background_color(arcade.color.SHAMROCK_GREEN)
    arcade.start_render()

    draw_slime(200,200,1,1,arcade.color.DARK_PASTEL_GREEN,arcade.color.FOREST_GREEN,arcade.color.LIGHT_SLATE_GRAY)
    draw_slime(-100, 100, 0.7, 0.7,arcade.color.DEEP_LILAC,arcade.color.ENGLISH_VIOLET,arcade.color.ROBIN_EGG_BLUE)
    draw_slime(0, 0,0.5,0.5,arcade.color.TURQUOISE,arcade.color.PINE_GREEN,arcade.color.LIGHT_SLATE_GRAY)
    draw_slime(0, 0,0.2,0.2,arcade.color.PINK_SHERBET,arcade.color.RASPBERRY_ROSE,arcade.color.LIGHT_SLATE_GRAY)
    draw_slime(180, -10, 0.9, 0.9,arcade.color.ALIZARIN_CRIMSON,arcade.color.ANTIQUE_RUBY,arcade.color.LIGHT_SLATE_GRAY)

    draw_slime(300, 0, 0.3, 0.3,arcade.color.SAE,arcade.color.BURNT_ORANGE,arcade.color.LIGHT_SLATE_GRAY)

    draw_slime(150, 300, 0.4, 0.4,arcade.color.BALL_BLUE,arcade.color.BLUE_SAPPHIRE,arcade.color.LIGHT_SLATE_GRAY)
    draw_slime(-80, 380, 0.5, 0.5,arcade.color.MUSTARD,arcade.color.DARK_YELLOW,arcade.color.LIGHT_SLATE_GRAY)

    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


main()
