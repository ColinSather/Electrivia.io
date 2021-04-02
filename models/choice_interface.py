
class ChoiceInterface:
    """
    This interface persists the trivia questions, to determine if questions are
    right or wrong.

    Instance variable(s):
        p: JSON data, list containing a hashmap
    """
    def __init__(self):
        self.p = None

    def setPossibilities(self, p):
        self.p = p

    def getPossibilities(self):
        return self.p


