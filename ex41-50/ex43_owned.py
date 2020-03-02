from textwrap import dedent

first_scene_name = 'central_jungle'
death_scene_name = 'death'
win_scene_name = 'win'

class jungle(object):
    def __init__(self, scenes):
        self.scenes = scenes
        # pass
    def next_area(self, area_name):
        return self.scenes[area_name]


class area(object):
    def __init__(self, this_area_name, description, test_answer, next_area_name):
        self.this_area_name = this_area_name
        self.description = description
        self.test_answer = test_answer
        self.next_area_name = next_area_name
    def enter(self):
        print('===================')
        print(self.description)
    def test(self):
        self.answer = input('> ')
    def result(self):
        return self.next_area_name if self.answer==self.test_answer else death_scene_name


class central_jungle(area):
    def __init__(self):
        this_area_name = first_scene_name
        description = dedent('''
        You are now at the central of the jungle!
        You are facing a panther.
        She's studying math, but you've bothered her.
        Now you have to help her with her homework, otherwise she will eat you alive!

        Say it, what is the Pi to the 6th digit?
        ''')
        test_answer = str(3.141593)
        next_area_name = 'volcano'
        super().__init__(this_area_name, description, test_answer, next_area_name)

class volcano(area):
    def __init__(self):
        this_area_name = 'volcano'
        description = dedent('''
        You've passed the central of the jungle and arrived at the greatest volcano of the forest.
        There lies Passbei Opzekt-reeferinz, a fire dragon with thousand-fahrenheit breadth 
        \tand also a Python guru.
        It asks you what is the output of these two scripts.

        Script 1:
        \tdef function(x):
        \t    x = [0,1]
        \tx= [0]
        \tfunction(x)
        \tprint(x)

        Script 2:
        \tdef function(x):
        \t    x.append(1)
        \tx = [0]
        \tfunction(x)
        \tprint(x)

        If you get them wrong then you are not worthy and only dead meat.
        ''')
        test_answer = {'Script 1': [0], 'Script 2': [0,1]}
        next_area_name = 'fall'
        super().__init__(this_area_name, description, test_answer, next_area_name)
    def test(self):
        answer = {}
        print('(put string in quotation mark)')
        for s in ('Script 1', 'Script 2'):
            answer[s] = eval(input('> {}: '.format(s)))
        self.answer = answer
        print(self.answer)
        

class fall(area):
    def __init__(self):
        this_area_name = 'fall'
        description = dedent('''
        You've successfully overcome the dragon's Python test.
        The dragon carried you over the exploding volcano by its giant, bloody-red wings
        \tand has dropped you by the great Linir Algeeba fall.
        As you're wandering aroudn not knowing where to go next, the fall suddenly splits in two
        \tand from behind comes Deetir Minoan, the god guardian of the fall.
        He asks you what is the following value:
             | 2 -3  1|
        det( | 4  2 -1| )
             |-5  3 -2|
        It's one of the most basic things in linear algebra, so if you don't know it
        \tthen there's no point to go any further.
        ''')
        test_answer = str(-19)
        next_area_name = 'cliff'
        super().__init__(this_area_name, description, test_answer, next_area_name)

class cliff(area):
    def __init__(self):
        this_area_name='cliff'
        description=dedent('''
        You've successfully figured out the correct determinant.
        The god guardian allowed you to enter the path behind the fall
        \tand showed you a secret tunnel which leads to the very end of the jungle.
        There, you stand of the cliff facing the final challenge: a giant ape named Piton Zen.
        It asks you one simple question which, if you can answer, will open your path to the Python Heaven.
        But, if you fail this last but not least challenge, the ape will throw you off the cliff.
        \t"What does DRY mean?"
        ''')
        test_answer = "do not repeat yourself"
        next_area_name = 'win'
        super().__init__(this_area_name, description, test_answer, next_area_name)
    def test(self):
        answer = input('> ').lower()
        self.answer = "do not repeat yourself" if answer in ("don't repeat yourself"\
            , "do not repeat yourself"\
            , "dont repeat yourself") else answer
        

class death(area):
    def __init__(self):
        this_area_name = death_scene_name
        description = dedent('''
        You are dead! GGWP!
        Good luck next time noob!
        ''')
        super().__init__(this_area_name, description, None, None)
    def test(self):
        pass
    def result(self):
        print('#'*50)
        again = input('> Do you want to play again (enter Y if yes)?\n')
        return first_scene_name if again.lower() == 'y' else 'exit'

class win(area):
    def __init__(self):
        this_area_name = 'win'
        description=dedent('''
        You've successfully completed all challenges on your quest to the Python Heaven!
        But careful you should be, this is just the start.
        The bigger, more important and even more challenging path lies ahead.
        Eat a lot, sleep a tons, and be hardworking and patient.
        Eventually you will be blessed by Pythonion, the Programming God.
        ''')
        super().__init__(this_area_name, description, None, None)
    def test(self):
        pass
    def result(self):
        print('#'*50)
        again = input('> Do you want to play again (enter Y if yes)?\n')
        return first_scene_name if again.lower() == 'y' else 'exit'


class rope(object):
    def __init__(self, jungle, first_scene, death_scene, win_scene):
        self.jungle = jungle
        self.first_scene_name = first_scene
        self.death_scene_name = death_scene
        self.win_scene_name = win_scene
    def play(self):
        print(dedent('''
        Welcome to the Journey to Python Heaven!
        You're about to face a series of challenges on your path to be with Pythonion - the Programming God.
        Best of luck on your journey!
        '''))
        scene = self.first_scene_name
        while scene != 'exit':
            current_scene = self.jungle.next_area(scene)
            current_scene.enter()
            current_scene.test()
            scene = current_scene.result()
        print('The game has been exit.')



everything = {}
for s in (central_jungle, cliff, fall, volcano, win, death):
    scene = s()
    everything[scene.this_area_name] = scene
jungle = jungle(everything)
rope = rope(jungle, first_scene_name, death_scene_name, win_scene_name)
rope.play()