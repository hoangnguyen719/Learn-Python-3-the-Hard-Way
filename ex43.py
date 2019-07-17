from sys import exit
from random import randint
from textwrap import dedent
# just a new comment
class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    def enter(self):
        print("You are dead, noob!")
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        You are in the central corridor.
        The aliens have surrounded the whole spaceship.
        You have to run away, but there is an alien in front of you.
        What are you going to do?
        """))
        print("1. Shoot")
        print("2. Run")
        print("3. Tell a joke")
        action = input("> ")
        if action == "1":
            print(dedent("""
            The alien shot faster, and you are dead meat!
            """))
            return('death')
        elif action == "2":
            print(dedent("""
            There is no way to run. As you are trying to find an escape,
            the alien pulled out a gatling gun and shot you to pieces.
            """
            ))
            return('death')
        elif action == "3":
            print(dedent("""
            Good choice, aliens love jokes. While it was laughing
            you snatched the gun and put tens of holes on its body.
            """
            ))
            return('laser_weapon_armory')
        else:
            print("This is not one of the options!")
            return("central_corridor")

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        You run into the Laser Weapon Armory room.
        At this point, there is no way to win the battle ship back.
        Only one way to survive: blow up the ship with the aliens
        then escape in a survival pod.
        There is a mini-nuclear bomb in a lock shelve in this room.
        The shelve is locked using 3-digit code. You have to guess the code.
        """))
        guess = input("[codepad] > ")
        guessing = 10
        code = "{}{}{}".format(randint(0,9), randint(0,9), randint(0,9))
        while (guess != code) & (guessing > 0):
            print("Wrong! You have {} guess(es) left!".format(guessing))
            code = input("[codepad] > ")
        if guess != code:
            print(dedent("""
            You guessed wrong 10 times! The shelve is permanently locked!
            You ran out of time and the aliens came.
            You're dead!
            """))
            return("death")
        else:
            print("You've got the bomb, now go to the bridge!")
            return("bridge")

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
