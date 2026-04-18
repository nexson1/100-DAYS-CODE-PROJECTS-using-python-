import  random



print('GUESSING GAME')
game_over = False
users_tries = 5
cpu_pick = random.randint(1, 10)

while True:
    while not  game_over:
        print(f'your life remains {users_tries}')
        user_pick = int(input('Enter a Guess from 1-10: '))


        print(cpu_pick)
        if user_pick == cpu_pick:

            print('Correct pick!!')
            game_over = True
        elif user_pick > cpu_pick:
            print('Too HIGh')
        else:
            print('Too Low')

        users_tries -= 1
        if users_tries == 0:
            game_over = True
            print(f'You lost the number {cpu_pick}')
    rewind = input('do u want to play: ')
    if rewind == 'yes':
            game_over = False
