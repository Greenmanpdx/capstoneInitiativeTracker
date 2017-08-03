class Character:
    def __init__(self, name, initiative, initiative_bonus, ac):
        self.name = name
        self.initiative_bonus = initiative_bonus
        self.initiative = initiative
        self.ac = ac

    def set_initiative(self, initiative):
        self.initiative = initiative

    def __lt__(self, other):
        if self.initiative == other.initiative:
            return self.initiative_bonus > other.initiative_bonus
        else:
            return self.initiative > other.initiative

    def __gt__(self, other):
        if self.initiative == other.initiative:
            return self.initiative_bonus < other.initiative_bonus
        else:
            return self.initiative < other.initiative

    def __eq__(self, other):
        if self.initiative == other.initiative:
            return self.initiative_bonus == other.initiative_bonus
        else:
            return self.initiative == other.initiative

    def __str__(self):
        return '{} AC: {} Initiative: {} + {}'.format(self.name, self.ac, self.initiative, self.initiative_bonus)

    def __repr__(self):
        return '{}'.format('{}: {} + {}'.format(self.name, self.initiative, self.initiative_bonus))


class NPC(Character):
    def __init__(self, name, initiative, initiative_bonus, ac, hp, fort, ref, will, attacks):
        self.name = name
        self.initiative_bonus = initiative_bonus
        self.ac = ac
        self.hp = hp
        self.fort = fort
        self.ref = ref
        self.will = will
        self.initiative = initiative
        self.attacks = attacks



