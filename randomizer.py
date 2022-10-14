import tkinter as tk
import random

GEOMETRY = '300x200'
PARTY_SIZE = 3

class Randomizer():
    current_solution = []
    previous_solution = []
    response: tk.Label = None

state = Randomizer()

def get_party(input: str) ->  str:

    # parse input string
    try:
        input = int(input)
    except:
        return 'Enter a positive integer.'
    if input < 1:
        return 'Enter a positive integer.'
    if input > 15:
        return 'I\'m not smart enough for that many players.'

    # find a solution
    get_solution(input)
    while state.current_solution == state.previous_solution and input != 1:
        get_solution(input)

    # build output string
    out_str = ''
    team_num = 1
    for i in range(len(state.current_solution)):
        cur_team = state.current_solution[i]
        team_str = f'Team {team_num}: '
        if len(cur_team) == 1:
            team_str += f' Player {cur_team[0]}'
        elif len(cur_team) == 2:
            team_str += f' Players {cur_team[0]} and {cur_team[1]}'
        elif len(cur_team) == 3:
            team_str += f' Players {cur_team[0]}, {cur_team[1]}, and {cur_team[2]}'
        team_str += '\n'
        out_str += team_str
        team_num += 1

    return out_str

def get_solution(num_players: int):

    # store off the prior solution
    state.previous_solution = state.current_solution
    state.current_solution = []

    # create list of unique player numbers starting at 1
    players = [x + 1 for x in range(num_players)]

    # assign each player to a team of size PARTY_SIZE
    assigned_count = 0
    cur_team = []
    while assigned_count < num_players:
        cur_player = players[random.randrange(0, len(players))]
        players.remove(cur_player)
        if len(cur_team) == PARTY_SIZE:
            state.current_solution.append(cur_team)
            cur_team = []
        cur_team.append(cur_player)
        assigned_count += 1
    
    # last time may sometimes be smaller than PARTY_SIZE
    if len(cur_team) > 0:
        state.current_solution.append(cur_team)


def randomize():
    input = textbox.get()
    if state.response is not None:
        state.response.destroy()
    state.response = tk.Label(main_window, text=f'{get_party(input)}')
    state.response.pack()

main_window = tk.Tk()
main_window.title('Apex Party Randomizer')
main_window.geometry(GEOMETRY)

prompt = tk.Label(main_window, text='How many players do you have?')
prompt.pack()

textbox = tk.Entry(main_window, width=10)
textbox.pack()

button = tk.Button(main_window, text="Randomize!", command=randomize)
button.pack()

main_window.mainloop()