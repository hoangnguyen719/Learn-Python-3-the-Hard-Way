from textwrap import dedent

death_scene_name = 'death'

class jungle(object):
    def __init__(self):
        print('Successfully init jungle!')
        pass
    def next_area(self, area_name):
        pass


class area(object):
    def __init__(self, this_area_name, description, test_answer, next_area_name):
        self.this_area_name = this_area_name
        self.description = description
        self.test_answer = test_answer
        self.next_area_name = next_area_name
    def enter(self):
        print(self.description)
    def test(self):
        self.answer = input('> ')
    def result(self):
        return self.next_area_name if self.answer==self.test_answer else death_scene_name


class central_jungle(area):
    def __init__(self):
        this_area_name = 'central_jungle'
        description = dedent('''
        ===================
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
        ===================
        You've passed the central of the jungle and arrived at the greatest volcano of the forest.
        There is a fire dragon with thousand-fahrenheit breadth and also a Python guru.
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

        If you get them wrong then you are not worth and only dead meat.
        ''')
        test_answer = {'Script 1': [0], 'Script 2': [0,1]}
        next_area_name = 'mountain'
        super().__init__(this_area_name, description, test_answer, next_area_name)
    def test(self):
        answer = {}
        for s in ('Script 1', 'Script 2'):
            answer[s] = eval(input('> {}: '.format(s)))
        print(self.answer)
        

class mountain(area):
    def __init__(self):
        pass
    def enter(self):
        pass

class cliff(area):
    def __init__(self):
        pass
    def enter(self):
        pass

class death(area):
    def __init__(self):
        pass
    def enter(self):
        pass

class rope(object):
    def __init__(self, map):
        self.map = map
    def play(self):
        self.map.next_area()

jungle_map = jungle()

central_jungle = central_jungle()
# print(central_jungle.next_area_name)
# print(central_jungle.description)
# print(central_jungle.test_answer)
central_jungle.enter()
central_jungle.test()
central_jungle.result()

volcano = volcano()
volcano.enter()
volcano.test()
print(volcano.result())
