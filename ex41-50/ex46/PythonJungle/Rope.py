from textwrap import dedent
from time import sleep

print('Initialized Rope.py!')

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