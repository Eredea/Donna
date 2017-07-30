import DonBase








"""This class could just as easily be named parser. Donna will be my personal assistant,
    whose primary function at the time being is to listen to sentences, convert them to Sentence obnjects, and command
    objects when necessary."""
class Donna:
    environment = None

    def default(self):pass

    #Once a command verb is learned, it passes a keyword to donna to know what operation to be performed
    mapped_opverb_keywords = {"open"  :default(),
                      }


    #This should be Donna's first encounter with a user input.
    def listen(self, listened_to_string, admin=True, learn =False, **kwargs):
        if admin and learn:
            sentence = Sentence(listened_to_string, Donna.environment, learn = True)

        if admin:
            sentence = Sentence(listened_to_string, Donna.environment)
            self.handle(sentence)


    def handle(self, sentence, admin = True, **kwargs):

        """Here, we need to be taken away from parsing and into doing what we need to.
            """
        #This is a check to make sure the verb is known, otherwise a new sentence object is created to try and parse immediately.
        if sentence.verb.linked_operation in known_commands:
            sentence.operate = known_commands[sentence.verb.name]
                if sentence.dir_obj_is_known
                    sentence.operate(sentence.dir_obj)
        """Donna.todo = sentence.necessary_operation.
        Donna.todo_on = sentence.operated_word.bound_cat
        self.todo(self.todo_on)"""
        Donna.operation = Donna.known_commands[sentence.verb.name]
        Donna.operation(sentence.dir_obj)
        Donna.todo_on = sentence.operated_word.bound_cat

        #actee = sentence.operated_word.NewCatItem()


        #sentence.operated_word.be_operated(sentence.operative_word)

    """Here begins the list of things that Donna knows how to do. I am looking for a better way of storing these."""
    def learn_to_handle(self):
        self.listen(learn = True)

    #This is for learning verbs. If no word linked with an operation is found in a sentence, she will try every command she knows on the dir_obj.

    def open(self):
    def load_known_commands(self)
        for word in
        return

    def Identify(self, string):
        Sentence("string")
        print(xyz + "is a" + word.item_cat[Donna.environment] + word.item_cat.description)

    def donnaTry(self, trying, trying_on,):
        trying.trying()
        #I've yet to decide how to implement this function- do we pass her the name of her function directly:
        if trying == str:
            globals()[trying](trying_on)
        #Do we pass her a word object and grab the string from there:
        if trying == DonBase.InterpretedWord:
            globals()[trying.name](trying_on)
        #Or do we have the word object itself have a function bound:
        else: trying(trying_on)

        #For now, all 3.



    """def open(self, obj_to_open):

        obj_to_open.open()
        pass
    def analyze(self, obj_to_analyze):
        obj_to_analyze.analyze()
        pass
    def play(self, to_play):
        song = MusicObject()
        song.play()
        pass
    def open(self):
        pass
    def analyze(self):
        pass
    def organize(self):
        pass"""

    #known_commands = DonBase.query.filter(operative words)



class LanguageTools():

        @staticmethod
        def seperate_words(text):
            # split the text
            words = text.split()
            return words

        def parse_sentence(self, sentence):
            words = self.identify_words(sentence)
            return words

        def identify_words(self, sentence):
            categorized_items = []
            for word in self.seperate_words(sentence):
                categorized_items.append(word)
            return categorized_items

        def act_on(self, prompt):
            items = self.parse_sentence(prompt)
            for item in items:
                if item.isOperative:
                    item.Operate()

        """def combine_strings(self, ):
            out_str = ''
            for num in xrange(loop_count):
                out_str += `num`
            return out_str"""


"""Right now focuses on commands, and identifying the acting verb in a sentence."""
class Sentence:
    """Sentences are created with the relevant string to create and interact with a group of word (database) objects,
        to be interpreted and acted on by Donna"""
    def __init__(self, string, environment, learn = False):
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
        #Each word item has an associated operation
        self.linked_operation = Donna.known_commands[self.verb.operator_name]
        self.dir_obj = self.id_dir_obj()
        #self.joining_operator = self.operated_word.operator[self.operative_word]


    def new_sentence(self, string):
        return Sentence(string)



    def create_word_objects(self):
        word_objs = []
        for word in self.word_list:
            word = DonBase.MakeWordObj(word)
            word_objs.append(word)
        return word_objs

    def id_verb(self, environment = "default"):
        """Bad algorithm for now, but just checks for the first word stored in the DB as a known acting verb"""
        for word in self.word_objs:
            if word.isOperative:
                return word
            else: print("no operative word")

    def id_dir_obj(self, operative):
            """First checks if the relevant verb recognizes any of the """
            for possible_dir_obj in self.word_objs:
                if self.verb.looking_for.contains(possible_dir_obj.type):
                    return possible_dir_obj
                elif self.learning:
                    pass
            else: print("I don't know what you want me to do that on.")

    def new_cat_item(self, word):
        self.dir_obj
        pass

"""Gets information about given words from SQL database."""


class PromptCreation:
    pass


class DBInteraction:
    pass


class PythonScriptCreator:
    pass

"""class CategorizableItem(Base):
    __tablename__ = 'KnownItems'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    is_operable = Column(Integer, nullable=True)

    def __init__(self, name, is_operable = False, ):
        self.name = name
        self.is_operable = is_operable"""

class CategorizableItem:
    def __init__(self, name, songlocation):
        pass

class MusicObject():
    from pygame import mixer  # Load the required library
    import time
    def play(self, location = '/home/Eredea/PycharmProjects/Donna/Hotel California- Eagles.mp3'):
        self.mixer.init()
        self.mixer.music.load(location)
        self.mixer.music.play()
        self.time.sleep(50)
        pass
class GameObject(CategorizableItem):
    def play(self):
        pass

class File():
    def __init__(self, location):
        self.location = location



don = Donna()
don.listen("play")