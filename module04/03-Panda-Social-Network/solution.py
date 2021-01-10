'''
ivo = Panda("Ivo", "ivo@pandamail.com", "male")

ivo.name() == "Ivo" # True
ivo.email() == "ivo@pandamail.com"  # True
ivo.gender() == "male" # True
ivo.isMale() == True # True
ivo.isFemale() == False # True
```

The `Panda` class also should be possible to:

    * Be turned into a string
    * Be hashed and used as a key in a dictionary (`__eq__` and `__hash__`)
    * Make sure that the email is a valid email!

    Two `Panda` instances are equal if they have matching `name`, `email` and `gender` attributes.
'''

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

'''
`add_panda(panda)` - this method adds a panda to the social network. The panda has 0 friends for now.
If the panda is already in the network, raise a `PandaAlreadyThere` error.
`has_panda(panda)` - returns `True` or `False` if the panda is in the network or not.
`make_friends(panda1, panda2)` - makes the two pandas friends. Raise `PandasAlreadyFriends` if they are already friends.
The friendship is two-ways - `panda1` is a friend with `panda2` and `panda2` is a friend with `panda1`.
If `panda1` or `panda2` are not members of the network, add them!
`are_friends(panda1, panda2)` - returns `True` if the pandas are friends. Otherwise, `False`
`friends_of(panda)` - returns a list of `Panda` with the friends of the given panda.
Returns `False` if the panda is not a member of the network.
'''
class PandaAlreadyThere(Exception):
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
        self._network[panda1].append(panda2)
        self._network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda2 in self._network[panda1]

    def friends_of(self, panda):
        return self._network[panda]
