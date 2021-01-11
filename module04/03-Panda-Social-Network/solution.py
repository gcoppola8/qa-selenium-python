class Panda:
    def __init__(self, name, email, gender):
        self._name = name
        self._email = email
        self._gender = gender

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        return self._gender == "male"

    def isFemale(self):
        return self._gender == "female"

    def __str__(self):
        return "Panda ({}) - {} with email {}".format(self._name, self._gender, self._email)

    def __eq__(self, other):
        if other._name is not None and self._name == other._name:
            if other._gender is not None and self._gender == other._gender:
                if other._email is not None and self._email == other._email:
                    return True
        return False

    def __hash__(self):
        return hash((self._name, self._email, self._gender))

class PandaAlreadyThere(Exception):
    None

class PandaAlreadyFriends(Exception):
    None

class PandaSocialNetwork:
    def __init__(self):
        self._network = {}

    def add_panda(self, panda):
        if panda in self._network:
            raise PandaAlreadyThere("")
        self._network[panda] = []

    def has_panda(self, panda):
        return panda in self._network

    def make_friends(self, panda1, panda2):
        if panda1 not in self._network:
            self.add_panda(panda1)
        if panda2 not in self._network:
            self.add_panda(panda2)
        if panda1 in self._network[panda2]:
            raise PandaAlreadyFriends
        self._network[panda1].append(panda2)
        self._network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda2 in self._network[panda1]

    def friends_of(self, panda):
        if panda not in self._network:
            return False
        return self._network[panda]
