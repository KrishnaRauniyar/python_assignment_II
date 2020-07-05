#  Imagine you are creating a Super Mario game. You need to define a class to represent Mario. What would it look like? If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.


from pynput import keyboard


def controller(key):
    is_jump = False
    if str(key) == 'Key.right':
        move.right()
    elif str(key) == 'Key.left':
        move.left()
    elif str(key) == 'Key.up':
        is_jump = True
        move.jump()
    elif str(key) == 'Key.esc':
        end.score()
        end.menu()
        return False

    if is_jump == True:
        move.gravity()


class Startgame:
    def startmenu(self):
        a = input('Enter s to start game : ')
        if a == 's':
            print('Game started.')
            return True
        else:
            return False

    def background(self):
        print('background is moving.')

    def showmario(self):
        print('mario is ready to play.')


class Move:
    def right(self):
        print('moving right by 5.')

    def left(self):
        print('moving left by 5.')

    def jump(self):
        print('mario jumping.')

    def gravity(self):
        print('gravity enable.')


class Gameover:

    def score(self):
        print('your score : ', 1512)

    def menu(self):
        print('Game over!!!')


start = Startgame()
move = Move()
end = Gameover()
if start.startmenu() == True:
    start.background()
    start.showmario()
    print('Enter escape to exit')
    with keyboard.Listener(on_press=controller) as listener:
        listener.join()