import random

states = ['rock', 'paper', 'scissors']

# Game initialize
name = input('Enter your name:')
print(f'Hello, {name}')
new_states = input()
if len(new_states) > 0:
    states = new_states.split(',')
print("Okay, let's start")
# print(states)

# Rating db check
score_base = open('rating.txt', 'r')
rating = 0
ratings = {}
for item in score_base.readlines():
    x, y = item.split()
    if y.endswith('\n'):
        ratings[x] = y[:len(y) - 1]
    else:
        ratings[x] = y
score_base.close()
if name in list(ratings):
    rating = int(ratings[name])

# Main game loop
while True:
    user_choice = input()
    if user_choice == '!exit':
        print('Bye!')
        break
    elif user_choice == '!rating':
        print(f'Your rating: {rating}')
    elif user_choice not in states:
        print('Invalid input')
    else:
        ai_choice = random.choice(states)
        messages = {'lose': f'Sorry, but computer chose {ai_choice}',
                    'draw': f'There is a draw ({ai_choice})',
                    'win': f'Well done. Computer chose {ai_choice} and failed'}
        current_state = states[states.index(user_choice) + 1:] + states[:states.index(user_choice)]
        # print(current_state)
        if ai_choice not in current_state:
            result = 'draw'
            rating += 50
        elif current_state.index(ai_choice) <= len(current_state) / 2 - 1:
            result = 'lose'
        else:
            result = 'win'
            rating += 100
        print(messages[result])