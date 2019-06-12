# attacks
import random

class Attacks(object):


    def __init__(self, cube1, cube2, attack, choose_player, playing_player, choose_attack):

        self.cube1 = cube1
        self.cube2 = cube2
        self.attack = attack
        self.choose_player = choose_player
        self.playing_player = playing_player
        self.choose_attack = choose_attack
        self.defend_function = dict()
        self.hamoodim = dict()



    def choose_attacks(self):

        for player in self.turn_rotation():

            self.playing_player = player
            self.choose_attack = input('Choose the attack you want to use: ').lower()

            if player_hamoodim in self.hamoodim :
                self.hamoodim.pop(player_hamoodim)
                self.hamoodim_mesahakim()

            if self.choose_attack == 'kamikaza':
                self.kamikaza()

            elif self.choose_attack == 'attack':
                self.attack()


            elif self.choose_attack == 'haim poison':

                self.haim_poison()

                break


            elif self.choose_attack == 'pishoto ttt':

                self.pishoto_ttt()

                break


            elif self.choose_attack == 'hamoodim':

                self.hamoodim_mesahakim()


            elif self.choose_attack == 'nizan goldberg':

                self.nizan_goldberg()

            elif self.choose_attack == 'defend':

                self.defend




    def try_again(self):

        while True:

            self.choose_attack = input('Choose the attack you want to use: ').lower()

            if self.choose_attack == 'kamikaza':

                self.kamikaza()
                break

            elif self.choose_attack == 'attack':

                self.attack()
                break

            elif self.choose_attack == 'haim poison':

                self.haim_poison()
                break

            elif self.choose_attack == 'pishoto ttt':

                self.pishoto_ttt()
                break

            elif self.choose_attack == 'hamoodim':

                self.hamoodim_mesahakim()
                break

            elif self.choose_attack == 'nizan goldberg':

                self.nizan_goldberg()
                break
            elif self.choose_attack == 'hamoodim mesahakim':

                self.hamoodim_mesahakim()
                break
            elif self.choose_attack == 'defend':

                self.defend
                break



    def kamikaza(self):

        self.choose_player = input('Enter the player you want to attack: ').lower()
        self.cube1 = random.randint(1, 6)
        self.cube2 = random.randint(1, 6)

            if self.check_hamoodim_mesahakim == 'on':

                self.hamoodim_mesahakim

            if self.cube1 or self.cube2 is 1:

                print('{} got {} and {}.'.format(self.playing_player, self.cube1, self.cube2))
                self.get_hp_playing_player() = 0
                self.pop_out()

            elif self.cube1 and self.cube2 is 2

                print('{} got {} and {}.'.format(self.playing_player, self.cube1, self.cube2))
                print('You killed {}.'.format(self.choose_player))
                self.get_hp() = 0
                self.pop_out()

                if self.defend_function[self.choose_player] == 'on':

                    self.attack = self.cube1 * self.get_strength() - self.get_stamina()
                    self.get_hp() -= self.attack
                    self.defend_function.pop(self.choose_player)
                    print('You broke {} shield. '.format(self.choose_player))
                    print('{} lost {} HP from your attack. He has {} HP left.'.format(self.choose_player, self.attack
                                                                                      , self.get_hp))
                    self.pop_out()
                else:

                    print('You killed {}.'.format(self.choose_player))
                    self.get_hp() = 0
                    self.pop_out()

            else:

                print('{} got {} and {}.'.format(self.playing_player, self.cube1, self.cube2))
                self.attack = (self.cube1 + self.cube2) * self.get_strength() - self.get_stamina()
                self.get_hp() -= self.attack
                print('{} lost {} HP from your attack. He has {} HP left.'.format(self.choose_player, self.attack
                                                                                  , self.get_hp))
                self.pop_out



    def attack(self):

        self.choose_player = input('Enter the player you want to attack: ').lower()
        self.cube1 = random.randint(1, 6)

        if player_hamoodim in self.hamoodim:
            self.hamoodim.pop(player_hamoodim)
            self.hamoodim_mesahakim()

        if self.defend_function[self.choose_player] == 'on':

            print('{} is using defend this turn.'.format(self.choose_player))
            self.defend_function.pop(self.choose_player)
            print('You broke {} shield. '.format(self.choose_player))

        else:

            print('You threw {}.'.format(self.cube1))
            self.attack =  self.cube1 * self.get_strength() - self.get_stamina()
            self.get_hp() -= self.attack
            print('{} lost {} HP from your attack. He has {} HP left.'.format(self.choose_player, self.attack
                                                                              , self.get_hp))
            self.pop_out()


    def defend(self):

        self.defend_function[self.playing_player] = ['on']
        print('{} activated defend! He is immune for one attack!'.format(self.playing_player))


    def haim_poison(self):

        if self.character_players_dictionary[self.playing_player[chosen_character] == 'mr shvets':

            self.choose_player = input('Choose the player you want to attack: ')
            self.attack = 10

            if self.defend_function[self.choose_player] == 'on':

                print('{} is using defend this turn.'.format(self.choose_player))
                self.defend_function.pop(self.choose_player)
                print('You broke {} shield. '.format(self.choose_player))


        else:

            print('You are not playing mr shvets. Try other attack.')
        self.try_again()


    def pishoto_ttt(self):

        if self.character_players_dictionary[self.playing_player[chosen_character] == 'pishoto':

            self.get_strength() += 2
        else:

            print('You are not playing Pishot. Try other attack.')
        self.try_again()


    def hamoodim_mesahakim(self):

        if self.character_players_dictionary[self.playing_player[chosen_character] == 'nizan goldberg':

            self.hamoodim[self.playing_player] = 'on'
            self.choose_player = self.turn_roatation.random.choice()
            return self.choose_player

        else:

            print('You are not playing lord dror. Try other attack.')
            self.try_again()



    def nizan_goldberg(self):

        if self.character_players_dictionary[self.playing_player[chosen_character] == 'nizan goldberg':

            self.get_stamina(self.playing_player) += self.get_stamina() * 1.5

        else:

            print('You are not playing lord dror. Try other attack.')
            self.try_again()

