import arcade
import random

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

        self.playerx = 400
        self.playery = 350
        self.speedx1 = 400
        self.speedy1 = 400

        self.coin_list = arcade.SpriteList()
        self.coin = arcade.AnimatedTimeBasedSprite()


        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.frames = []

        self.coin_list = arcade.SpriteList()
        self.coin = arcade.AnimatedTimeBasedSprite()

        self.coin.frames = []
        for i in range(30):
            self.coin = arcade.AnimatedTimeBasedSprite()
            self.coin.frames = []
            for row in range(1):
                for col in range(2):
                    tex = arcade.load_texture('Sprites/coin/coinanim.png', x=col * 9, y=row * 10, width=10, height=10)
                    frame = arcade.AnimationKeyframe(col, 100, tex)
                    self.coin.frames.append(frame)
                    self.coin._points = tex.hit_box_points
            self.coin.scale = 2
            self.coin.center_x = random.randint(20, 780)
            self.coin.center_y = random.randint(20,580)
            self.coin_list.append(self.coin)

        self.player_list.append(self.player)

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture('Sprites/Megamen6.png'))


        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture('Sprites/Megamen9.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Sprites/Megamen9.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Sprites/Megamen10.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Sprites/Megamen10.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Sprites/Megamen11.png'))
        self.player.walk_right_textures.append(arcade.load_texture('Sprites/Megamen11.png'))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture('Sprites/Megamen6.png', mirrored=True))

        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(arcade.load_texture('Sprites/Megamen9.png', mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture('Sprites/Megamen9.png', mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture('Sprites/Megamen10.png', mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture('Sprites/Megamen10.png', mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture('Sprites/Megamen11.png', mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture('Sprites/Megamen11.png', mirrored=True))

        self.player.center_x = 400
        self.player.center_y = 300

        self.player.scale = 2

        # self.player_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()
        self.coin_list.update_animation()
        self.player_list.update_animation()
        collisions = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for i in collisions:
            self.coin_list.remove(i)


    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.RIGHT:
            self.player.change_x = 10
        elif symbol == arcade.key.LEFT:
            self.player.change_x = -10
        elif symbol == arcade.key.UP:
            self.player.change_y = 10
        elif symbol == arcade.key.DOWN:
            self.player.change_y = -10

    def on_key_release(self, symbol, modifiers):

        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player.change_y = 0


def main():

    game = MyGame(WIDTH, HEIGHT)
    arcade.run()


main()
