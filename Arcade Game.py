# Work Cited Code:
#https://api.arcade.academy/en/latest/examples/sprite_change_coins.html#sprite-change-coins
#https://api.arcade.academy/en/latest/examples/sprite_collect_coins_diff_levels.html#example-sprite-collect-coins-diff-levels

# Directions
# Before the game begins it will show the instructions of how to play the game on the first screen.
# To start the game press the space bar.
# Use the arrows to move the sprite across the screen to collect the stars, blue diamonds, and green diamonds.
# Stars are worth 1, blue diamonds are worth 10, and green diamonds are worth 20 points.
# There are five levels in this game that progressively get harder.

import arcade
import arcade.gui
import random


SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Collecting Diamonds"
GAME_RUNNING = 1
GAME_INTRO = 2
GAME_OVER = 3

MOVEMENT_SPEED = 5


class Collectable(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change = False


class FallingDiamond(arcade.Sprite): # Sprite falls down
    def update(self): #Move the diamond
        self.center_y -= 5 #Fall Down
        if self.top < 0: # pop back to the top after going off screen
            self.bottom = SCREEN_HEIGHT

class RisingDiamond(arcade.Sprite): # Sprite that falls up

    def update(self): # move the coin
        self.center_y += 5 # move up
        if self.bottom > SCREEN_HEIGHT: # pop back to the bottom after going off screen
            self.top = 0

class InstructionView(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE) #Instruction background

    def on_draw(self): #Instructions
        arcade.draw_text("Use the arrows to ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.LIGHT_BLUE, font_size=50, anchor_x="center")
        arcade.draw_text("collect the stars ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.LIGHT_BLUE, font_size=50, anchor_x="center")
        arcade.draw_text("and diamonds.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.LIGHT_BLUE, font_size=50, anchor_x="center")
        arcade.draw_text("Click space bar to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 225,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = MyGame()
            game_view.setup()
            self.window.show_view(game_view)



class MyGame(arcade.View):

    def __init__(self):
        super().__init__()

        # Variable List
        self.background = None
        self.frame_count = 0
        self.player_list = None
        self.blue_diamond_list = None
        self.green_diamond_list = None
        self.star_list = None
        self.star_score =1
        self.green_diamond_score = 20
        self.blue_diamond_score = 10
        # Player Info
        self.player_sprite = None
        self.score = 0
        self.level = 1
        self.state = None
        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        #Don't show mouse cursor
        self.window.set_mouse_visible(False)
        # First screen
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        # Set background color
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )


    def level_1(self):
        for i in range(30):
            #create star
            star = arcade.Sprite(":resources:images/items/star.png", SPRITE_SCALING
            / 3)
            blue_diamond = arcade.Sprite(":resources:images/items/gemBlue.png", SPRITE_SCALING / 3)
            green_diamond = arcade.Sprite(":resources:images/items/gemGreen.png", SPRITE_SCALING /3)
            # Position star
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)
            #Position blue diamond
            blue_diamond.center_x = random.randrange(SCREEN_WIDTH)
            blue_diamond.center_y = random.randrange(SCREEN_HEIGHT)
            #Position green diamond
            green_diamond.center_x = random.randrange(SCREEN_WIDTH)
            green_diamond.center_y = random.randrange(SCREEN_HEIGHT)
            # Add star to the lists
            self.star_list.append(star)
            #Add blue diamond to the lists
            self.blue_diamond_list.append(blue_diamond)
            # Add green diamond to the lists
            self.green_diamond_list.append(green_diamond)
            # Set the background color
            arcade.set_background_color(arcade.color.RED)

    def level_2(self):
        for i in range(25):
            star = FallingDiamond(":resources:images/items/star.png", SPRITE_SCALING / 3)
            blue_diamond = FallingDiamond(":resources:images/items/gemBlue.png", SPRITE_SCALING /3)
            green_diamond = FallingDiamond(":resources:images/items/gemGreen.png", SPRITE_SCALING /3)
            # Position star
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
            # Position blue diamond
            blue_diamond.center_x = random.randrange(SCREEN_WIDTH)
            blue_diamond.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
            # Position green diamond
            green_diamond.center_x = random.randrange(SCREEN_WIDTH)
            green_diamond.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
            # Add star to the lists
            self.star_list.append(star)
            # Add blue diamond to the lists
            self.blue_diamond_list.append(blue_diamond)
            # Add green diamond to the lists
            self.green_diamond_list.append(green_diamond)
            # Set the background color
            arcade.set_background_color(arcade.color.BLACK)

    def level_3(self):
        for i in range(25):
            star = RisingDiamond(":resources:images/items/star.png", SPRITE_SCALING / 3)
            blue_diamond = RisingDiamond(":resources:images/items/gemBlue.png", SPRITE_SCALING / 3)
            green_diamond = RisingDiamond(":resources:images/items/gemGreen.png", SPRITE_SCALING / 3)
            # Position star
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(-SCREEN_HEIGHT, 0)
            # Position blue diamond
            blue_diamond.center_x = random.randrange(SCREEN_WIDTH)
            blue_diamond.center_y = random.randrange(-SCREEN_HEIGHT, 0)
            # Position green diamond
            green_diamond.center_x = random.randrange(SCREEN_WIDTH)
            green_diamond.center_y = random.randrange(-SCREEN_HEIGHT, 0)
            # Add star to the lists
            self.star_list.append(star)
            # Add blue diamond to the lists
            self.blue_diamond_list.append(blue_diamond)
            # Add green diamond to the lists
            self.green_diamond_list.append(green_diamond)
            # Set the background color
            arcade.set_background_color(arcade.color.DARK_GREEN)

    def level_4(self):
        for i in range(25):
            star = FallingDiamond(":resources:images/items/star.png", SPRITE_SCALING / 3)
            blue_diamond = RisingDiamond(":resources:images/items/gemBlue.png", SPRITE_SCALING / 3)
            green_diamond = RisingDiamond(":resources:images/items/gemGreen.png", SPRITE_SCALING / 3)
            # Position star
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
            # Position blue diamond
            blue_diamond.center_x = random.randrange(SCREEN_WIDTH)
            blue_diamond.center_y = random.randrange(-SCREEN_HEIGHT, 0)
            # Position green diamond
            green_diamond.center_x = random.randrange(SCREEN_WIDTH)
            green_diamond.center_y = random.randrange(-SCREEN_HEIGHT, 0)
            # Add star to the lists
            self.star_list.append(star)
            # Add blue diamond to the lists
            self.blue_diamond_list.append(blue_diamond)
            # Add green diamond to the lists
            self.green_diamond_list.append(green_diamond)
            # Set the background color
            arcade.set_background_color(arcade.color.PURPLE_HEART)

    def level_5(self):
        for i in range(25):
            star = RisingDiamond(":resources:images/items/star.png", SPRITE_SCALING / 3)
            blue_diamond = FallingDiamond(":resources:images/items/gemBlue.png", SPRITE_SCALING / 3)
            green_diamond = FallingDiamond(":resources:images/items/gemGreen.png", SPRITE_SCALING / 3)
            # Position star
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(-SCREEN_HEIGHT, 0)
            # Position blue diamond
            blue_diamond.center_x = random.randrange(SCREEN_WIDTH)
            blue_diamond.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT *2)
            # Position green diamond
            green_diamond.center_x = random.randrange(SCREEN_WIDTH)
            green_diamond.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT *2)
            # Add star to the lists
            self.star_list.append(star)
            # Add blue diamond to the lists
            self.blue_diamond_list.append(blue_diamond)
            # Add green diamond to the lists
            self.green_diamond_list.append(green_diamond)
            # Set the background color
            arcade.set_background_color(arcade.color.DARK_CORAL)


    def setup(self):
        self.level = 1
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.green_diamond_list = arcade.SpriteList()
        self.blue_diamond_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.current_state = GAME_INTRO


        # Set up player
        self.score = 0
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        self.level_1()



    def on_draw(self):
        arcade.start_render()
        self.draw_game()

    def draw_game(self):
        self.clear()
        self.manager.draw()
        #draw all sprites
        self.star_list.draw()
        self.blue_diamond_list.draw()
        self.green_diamond_list.draw()
        self.player_sprite.draw()
        # Put text on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 15)


    def on_update(self, delta_time):

        # call update on all sprites
        self.player_sprite.update()
        self.star_list.update()
        self.green_diamond_list.update()
        self.blue_diamond_list.update()

        #Generate a list of all sprites that collided with the player
        hit_list1 = arcade.check_for_collision_with_list(self.player_sprite, self.blue_diamond_list)
        hit_list2 = arcade.check_for_collision_with_list(self.player_sprite, self.star_list)
        hit_list3 = arcade.check_for_collision_with_list(self.player_sprite, self.green_diamond_list)


        # Loop through each colliding sprite, remove it, and add to the score
        for star in hit_list2:
            star.remove_from_sprite_lists()
            self.score += self.star_score
        for blue_diamond in hit_list1:
            blue_diamond.remove_from_sprite_lists()
            self.score +=  self.blue_diamond_score
        for green_diamond in hit_list3:
            green_diamond.remove_from_sprite_lists()
            self.score += self.green_diamond_score
        if len(self.star_list) == 0 and len(self.blue_diamond_list) == 0 and len(self.green_diamond_list) == 0 and self.level == 1:
            self.level += 1
            self.level_2()
        elif len(self.star_list) == 0 and len(self.blue_diamond_list) == 0 and len(self.green_diamond_list) == 0 and self.level == 2:
            self.level += 1
            self.level_3()
        elif len(self.star_list) == 0 and len(self.blue_diamond_list) == 0 and len(self.green_diamond_list) == 0 and self.level == 3:
            self.level += 1
            self.level_4()
        elif len(self.star_list) == 0 and len(self.blue_diamond_list) == 0 and len(self.green_diamond_list) == 0 and self.level == 4:
            self.level += 1
            self.level_5()
        elif self.score >= 4030:
            self.current_state = GAME_OVER
            game_view = EndingView()
            self.window.show_view(game_view)




    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.SPACE:
            self.current_state = GAME_RUNNING
        elif key == arcade.key.DOWN or key == arcade.key.UP:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.ESCAPE:
            self.current_state = GAME_OVER

class EndingView(arcade.View):
    def _on_show_view(self):
        arcade.set_background_color(arcade.color.BLUEBERRY)
    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME OVER", SCREEN_WIDTH /2, SCREEN_HEIGHT /2,
                         arcade.color.BLACK, font_size= 50, anchor_x= "center")
        arcade.draw_text("Press Escape to Exit ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.LIGHT_BLUE, font_size=50, anchor_x="center")
#
    def on_key_release(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()






def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Collecting Diamonds")
    instruction_view = InstructionView()
    window.show_view(instruction_view)
    arcade.run()


if __name__ == "__main__":
    main()