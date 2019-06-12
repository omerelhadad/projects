# functions
import random


class Functions (object):

    def __init__(self, hp, stamina, strength,playing_player,choose_character):

        self.hp = hp
        self.stamina = stamina
        self. strength = strength
        self.playing_player = playing_player
        self.choose_player = choose_character


    def get_hp(self):

        player_hp = self.character_players_dictionary[self.choose_player[chosen_character['stamina']]]
        return player_hp


    def get_hp_playing_player(self):

        playing_player_hp = self.character_players_dictionary[self.playing_player[chosen_character['hp']]]
        return playing_player_hp


    def get_stamina(self):

        player_stamina = self.character_players_dictionary[self.playing_player[chosen_character['stamina']]]
        return player_stamina

    def get_stamina_for_each_player(self, player_survived):

        player_survived = player_survived
        player_stamina = self.character_players_dictionary[player_survived[chosen_character['stamina']]]
        return player_stamina

    def turn_creator(self):

        new_shffled_list = random.shuffle(self.list_for_turns)
        number = 1

        for player_turn in new_shffled_list:

            print('{}. {}'.format(number, player_turn))
            number += 1
        return new_shffled_list


    def turn_roatation(self):

        self.turn_creator()
        counter = 1
        max_value = len(self.turn_creator())

        if max_value == 4:
            self.turn_creator()[0], self.turn_creator()[1] = self.turn_creator()[1], self.turn_creator()[0]
            self.turn_creator()[1], self.turn_creator()[2] = self.turn_creator()[2], self.turn_creator()[1]
            self.turn_creator()[2], self.turn_creator()[3] = self.turn_creator()[3], self.turn_creator()[2]

        elif max_value == 3:
            self.turn_creator()[0], self.turn_creator()[1] = self.turn_creator()[1], self.turn_creator()[0]
            self.turn_creator()[1], self.turn_creator()[2] = self.turn_creator()[2], self.turn_creator()[1]

        elif max_value == 2:
            self.turn_creator()[0], self.turn_creator()[1] = self.turn_creator()[1], self.turn_creator()[0]

        elif max_value == 1:
            print('{} WON!'.format(self.turn_creator()[0]))

        print('TURNS:')
        for player_turn in self.turn_creator():
            print('\n{}. {}'.format(counter, player_turn))
            counter += 1

        return self.turn_creator()


    def get_strength(self):

        player_strength = self.character_players_dictionary[self.playing_player[chosen_character['strength']]]
        return player_strength


    def get_hp_for_heal(self, player_survived):

        player_hp = self.character_players_dictionary[player_survived[chosen_character['stamina']]]
        return player_hp


    def heal_playing_player(self, player_survived):

        player_survived = player_survived
        self.get_hp_for_heal(player_survived) += self.get_stamina_for_each_player(player_survived)*0.1


    def add_stamina(self, player_survived):

        player_survived = player_survived
        self.get_stamina_for_each_player(player_survived) += self.get_stamina_for_each_player(get_hp_for_heal)*0.2


    def pop_out(self):

        if self.get_hp() <= 0:

            self.turn_roatation().pop(self.choose_player)
            self.character_players_dictionary.pop[self.choose_player]
            print('{} died.'.format(self.choose_player))

        elif self.get_hp_playing_player() <= 0:

            self.turn_roatation().pop(self.playing_player)
            self.character_players_dictionary.pop[self.playing_player]
            print('{} died.'.format(self.choose_player))


    def check_hamoodim_mesahakim(self):

        for key, value in self.hamoodim:

            if value == 'on':

                return 'on'

            else:

                continue


    def end_of_turn(self):

        for player_survived in self.turn_creator():
            self.heal_playing_player(player_survived)
            self.add_stamina(player_survived)











