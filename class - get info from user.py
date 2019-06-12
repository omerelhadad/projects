# get info from player

import random

MAX_PLAYERS = 4
MIN_PLAYERS = 2
CHARACTERS = dict()
CHARACTERS['mr shvets'] = {'hp': 100, 'stamina': 3, 'strength': 2}
CHARACTERS['pishoto'] = {'hp': 25, 'stamina': 14, 'strength': 6}
CHARACTERS['lord dror'] = {'hp': 70, 'stamina': 4, 'strength': 3}
CHARACTERS['witch of witches'] = {'hp': 50, 'stamina': 8, 'strength': 4}


class Game(object):

    def __init__(self, min_players=MIN_PLAYERS, max_players=MAX_PLAYERS, characters=CHARACTERS):
        self.list_for_turns = []
        self.character_players_dictionary = dict()
        self.min_players = min_players
        self.max_players = max_players
        self.characters = characters
        self.choose_character()

    def choosing_options(self):

        for characters, info in CHARACTERS.items():
            print('\nCharacter: ' + characters)

            for key_thing in info:
                print("{0}: {1}".format(key_thing, info[key_thing]))

    def choose_character(self):

        self.choosing_options()
        player_counter = 1

        while len(self.character_players_dictionary) < self.max_players:
            player_name = input('Enter player name ')
            chosen_character = input('Choose your character ').lower()

            if chosen_character in CHARACTERS:
                print('Player {}: {}'.format(player_counter, player_name))
                print('Character: ', chosen_character)
                for keys, value in CHARACTERS[chosen_character].items():
                    print('{0}: {1}'.format(keys, value))
                self.character_players_dictionary[player_name] = {chosen_character: CHARACTERS[chosen_character]}
                self.list_for_turns.append(player_name)
                player_counter += 1

            else:
                print('The character you chose does not exist. Choose again.')
                continue

            if len(self.character_players_dictionary) >= self.min_players:
                yes = '1'
                no = '2'
                print('Do you want to choose another player? ')
                ask_user = input('For YES choose 1. for NO choose 2.')

                if ask_user == yes:
                    continue

                elif ask_user == no:
                    break
        for key_character, item in self.character_players_dictionary.items():
            print('Player: {} | Character: {} | Stats: {} |'.format(key_character, chosen_character, item))



def main():
    Game()


if __name__ == '__main__':
    main()
