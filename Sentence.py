import DonBase

class Sentence:
    """Sentences are created with the relevant string to create and interact with a group of word (database) objects,
        to be interpreted and acted on by Donna"""

    def __init__(self, string, environment, learn=False):
        """Creates && analyzes word objects based on Donna's working environment, and whether it is actively learning"""
        self.learning = learn
        self.word_list = string.split()

        """Here's  a question, which is 'better' to create the word objs?
        1.

        def PopulateWordList(self)
            for word in self.word_list:
                word_obj = InterpretedWord(word)
                self.word_objs.append(word_obj)


            OR

        self.word_objs =

        def GenerateWordList(self)
            word_objs = []
            for word in self.word_list:
                word_obj = InterpretedWord(word)
                word_objs.append(word_obj)
            return word_objs

            Does it matter
        """
        self.word_objs = self.create_word_objects()
        self.verb = self.id_verb()
        # Each word item has an associated operation
        self.linked_operation = Donna.known_commands[self.verb.operator_name]
        self.dir_obj = self.id_dir_obj()
        # self.joining_operator = self.operated_word.operator[self.operative_word]

    def new_sentence(self, string):
        return Sentence(string)

    def create_word_objects(self):
        word_objs = []
        for word in self.word_list:
            word = DonBase.MakeWordObj(word)
            word_objs.append(word)
        return word_objs

    def id_verb(self, environment="default"):
        """Bad algorithm for now, but just checks for the first word stored in the DB as a known acting verb"""
        for word in self.word_objs:
            if word.isOperative:
                return word
            else:
                print("no operative word")

    def id_dir_obj(self, operative):
        """First checks if the relevant verb recognizes any of the """
        for possible_dir_obj in self.word_objs:
            if self.verb.looking_for.contains(possible_dir_obj.type):
                return possible_dir_obj
            elif self.learning:
                pass
        else:
            print("I don't know what you want me to do that on.")

    def new_cat_item(self, word):
        self.dir_obj
        pass