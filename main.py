import tracker
import character
import combat
import encounter

initiative_tracker = tracker.Tracker()
not_done = True


def new_player():
    name = input('Player name: ')
    initiative = int(input("Initiative: "))
    initiative_bonus = int(input('Initiative bonus'))
    ac = int(input('AC: '))
    initiative_tracker.add_player(character.Character(name, initiative, initiative_bonus, ac))


def load_encounter():
    initiative_tracker.load_encounter()


def start_combat(tracker):
    combat.run_combat(tracker)


def edit_player():
    pass


def quit_running():
    global not_done
    not_done = False


# main_menu = {'1': ('Add player', new_player()),
#              '2': ('Load encounter', load_encounter()),
#              '3': ('Start combat', start_combat(initiative_tracker)),
#              '4': ('Edit player', edit_player()),
#              '5': ('Quit', quit_running(not_done))
#              }


def pretty_print_dict(dict):
    for k in dict:
        print('{}. {}'.format(k, dict[k][0]))


while not_done:
    selection = input('1: Add player \n'
                      '2: Load Encounter \n'
                      '3: Start combat \n'
                      '4: Edit player \n'
                      '5: Quit')

    if selection == '1':
        new_player()
    if selection == '2':
        load_encounter()
    if selection == '3':
        start_combat(initiative_tracker)
    if selection == '4':
        edit_player()
    if selection == '5':
        quit_running()
    # main_menu[selection][1]
