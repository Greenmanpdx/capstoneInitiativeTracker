import character
import csv


class Circular_list(list):
    def __getitem__(self, item):
        try:
            return super(Circular_list, self).__getitem__(item)
        except IndexError:
            pass

        try:
            index = int(item)
            index = index % self.__len__()
            return super(Circular_list, self).__getitem__(index)
        except ValueError:
            raise TypeError


class Tracker:
    def __init__(self):
        self.turn_tracker = Circular_list()
        self.delayed_dict = {}

    def add_player(self, player):
        self.turn_tracker.append(player)

    def remove_player(self, index):
        del self.turn_tracker[index % len(self.turn_tracker)]

    def delay_turn(self, index):
        delayed = self.turn_tracker.pop(index % len(self.turn_tracker))
        i = str(len(self.delayed_dict) + 1)
        self.delayed_dict[i] = delayed

    def resume_turn(self, turn_index, delay_index):
        self.turn_tracker.insert(turn_index % len(self.turn_tracker), self.delayed_dict[delay_index])
        del self.delayed_dict[delay_index]

    def build_encounter(self, enc_list):
        i = 0

        while i < len(enc_list):
            number = int(enc_list[i])
            i += 1
            npc_name = enc_list[i]
            i += 1
            initiative = int(enc_list[i])
            i += 1
            bonus = int(enc_list[i])
            i += 1
            ac = enc_list[i]
            i += 1
            hp = enc_list[i]
            i += 1
            fort = enc_list[i]
            i += 1
            ref = enc_list[i]
            i += 1
            will = enc_list[i]
            i += 1
            attack = enc_list[i]
            i += 1
            k = 0
            while k < number:
                self.turn_tracker.append(character.NPC(npc_name, initiative, bonus, ac, hp, fort, ref, will, attack))
                k += 1

    def load_encounter(self):
        enc_dict = {}
        with open('encounters.txt', newline='') as csvfile:
            enc_reader = csv.reader(csvfile, delimiter=',')

            for row in enc_reader:
                enc_dict[row[0]] = list(row[1:])

        i = 1
        selection_dict = {}
        for k in enc_dict:
            selection_dict[str(i)] = k
            print('{}. Encounter {}'.format(str(i), k))
            i += 1

        selection = input()

        self.build_encounter(enc_dict[selection_dict[selection]])


class Encounter:
    def __init__(self, name, npc_list):
        self.name = name
        self.npc_list = npc_list
