from sys import exit

from random import randint
from textwrap import dedent
from time import sleep


class Area(object):
    def __init__(self, this_area_name, description, test_answer, next_area_name):
        self.this_area_name = this_area_name
        self.description = description if isinstance(description, list) else [description]
        self.test_answer = test_answer
        self.next_area_name = next_area_name
    def enter(self):
        print('==================='); sleep(0.2)
        for line in self.description:
            print(line); sleep(0.5)
    def test(self):
        self.answer = input('> ')
    def result(self):
        return self.next_area_name if self.answer==self.test_answer else 'death'


class CentralJungle(Area):
    def __init__(self):
        this_area_name = 'central_jungle'
        description = dedent('''
        You are now at the central of the jungle!
        You are facing a panther.
        She's studying math, but you've bothered her.
        Now you have to help her with her homework, otherwise she will eat you alive!\n
        Say it, what is the Pi to the 6th digit?
        ''').split('\n')
        test_answer = str(3.141593)
        next_area_name = 'volcano'
        super().__init__(this_area_name, description, test_answer, next_area_name)

class Volcano(Area):
    def __init__(self):
        this_area_name = 'volcano'
        description = dedent('''
        You've passed the central of the jungle and arrived at the greatest volcano of the forest.
        There lies Passbei Opzekt-reeferinz, a fire dragon with thousand-fahrenheit breadth and also a Python guru.
        It asks you what is the output of these two scripts.
        ''').split('\n')
        script1 = dedent('''
        Script 1:
        \tdef function(x):
        \t    x = [0,1]
        \tx= [0]
        \tfunction(x)
        \tprint(x)
        ''')
        script2 = dedent('''
        Script 2:
        \tdef function(x):
        \t    x.append(1)
        \tx = [0]
        \tfunction(x)
        \tprint(x)
        ''')
        final_line = 'If you get them wrong then you are not worthy and only dead meat.'
        description = description + [script1, script2, final_line]
        test_answer = {'Script 1': [0], 'Script 2': [0,1]}
        next_area_name = 'fall'
        super().__init__(this_area_name, description, test_answer, next_area_name)
    def test(self):
        answer = {}
        print('(put string in quotation mark)')
        for s in ('Script 1', 'Script 2'):
            answer[s] = eval(input('> {}: '.format(s)))
        self.answer = answer
        

class Fall(Area):
    def __init__(self):
        this_area_name = 'fall'
        description = dedent('''
        You've successfully overcome the dragon's Python test.
        The dragon carried you over the exploding volcano by its giant, bloody-red wings
        \tand has dropped you by the great Linir Algeeba fall.
        As you're wandering aroudn not knowing where to go next, the fall suddenly splits in two
        \tand from behind comes Deetir Minoan, the god guardian of the fall.
        He asks you what is the following value:
        ''').split('\n')
        det = dedent('''
             | 2 -3  1|
        det( | 4  2 -1| )
             |-5  3 -2|
        ''')
        final_line = dedent('''
        It's one of the most basic things in linear algebra, so if you don't know it
        \tthen there's no point to go any further.
        ''')
        description += [det, final_line]
        test_answer = str(-19)
        next_area_name = 'cliff'
        super().__init__(this_area_name, description, test_answer, next_area_name)

class Cliff(Area):
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
        ''').split('\n')
        test_answer = "do not repeat yourself"
        next_area_name = 'win'
        super().__init__(this_area_name, description, test_answer, next_area_name)
    def test(self):
        answer = input('> ').lower()
        self.answer = "do not repeat yourself" if answer in ("don't repeat yourself"\
            , "do not repeat yourself"\
            , "dont repeat yourself") else answer
        

class Death(Area):
    def __init__(self):
        this_area_name = 'death'
        death_reasons = ['You are dead! GGWP!\nGood luck next time noob!'
                        , 'Even my grandma can do better than that!'
                        , 'You really suck you know that?!'
                        , 'WRONG ANSWER! YOU N....O...O...B!'
                        ]
        description = dedent(death_reasons[randint(0, len(death_reasons) -1)])
        super().__init__(this_area_name, description, None, None)
    def test(self):
        pass
    def result(self):
        return 'exit'

class Win(Area):
    def __init__(self):
        this_area_name = 'win'
        description=dedent('''
        You've successfully completed all challenges on your quest to the Python Heaven!
        But careful you should be, this is just the start.
        The bigger, more important and even more challenging path lies ahead.
        Eat a lot, sleep a tons, and be hardworking and patient.
        Eventually you will be blessed by Pythonion, the Programming God.
        ''').split('\n')
        super().__init__(this_area_name, description, None, None)
    def test(self):
        pass
    def result(self):
        return 'exit'


class Rope(object):
    def __init__(self, jungle):
        self.jungle = jungle
    def play(self):
        for line in dedent('''
        Welcome to the Journey to Python Heaven!
        You're about to face a series of challenges on your path to be with Pythonion - the Programming God.
        Best of luck on your journey!
        ''').split('\n'):
            print(line); sleep(0.5)
        current_area_name = self.jungle.first_area_name
        previous_area_name = self.jungle.first_area_name
        while current_area_name != 'exit':
            current_area = self.jungle.next_area(current_area_name)
            current_area.enter()
            current_area.test()
            if current_area_name in (self.jungle.death_area_name, self.jungle.win_area_name):
                print('#'*50)
                again = input('Enter R to restart game.\nEnter A to play this round again.\nEnter to exit.\n> ').lower()
                if again == 'r':
                    current_area_name = self.jungle.first_area_name
                    continue
                elif again == 'a':
                    current_area_name = previous_area_name
                    continue
            previous_area_name = current_area_name
            current_area_name = current_area.result()
        print('The game has been exit.')
        exit(1)

class Jungle(object):
    areas = {'central_jungle': CentralJungle()
            , 'cliff': Cliff()
            , 'fall': Fall()
            , 'volcano': Volcano()
            , 'win': Win()
            , 'death': Death()
    }
    first_area_name = 'central_jungle'
    death_area_name = 'death'
    win_area_name = 'win'
    def __init__(self):
        pass
    def next_area(self, area_name):
        return self.areas[area_name]