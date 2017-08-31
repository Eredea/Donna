import Sentence

known_commands = {"open"  :open(),
                  }



def listen(user_response, admin=True, learn =False, **kwargs):
    """User input should first interact through this function. Begins syntactically analyzing user-given string, and controls flow through 'admin' and 'learn' args.
        PARAMS:
            user_response (str) - The sentence given by the user to be handled.
        RETURNS:
            None
            """
    if admin and learn:
        sentence = Sentence(user_response, environment, learn = True)

    if admin:
        sentence = Sentence(user_response, environment)
        handle(sentence)


def handle(self, sentence, admin = True, **kwargs):
    """Handle represents the execution of the natural language command proposed by the user.
     PARAMS:
        sentence (Sentence)- the user command converted to a sentence object.
     RETURNS:
         None"""

    operation = known_commands[sentence.verb.name]
    operation(sentence.dir_obj)
    todo_on = sentence.operated_word.bound_cat

    #This is a check to make sure the verb is known, otherwise a new sentence object is created to try and parse immediately.
    if sentence.verb.linked_operation in known_commands:
        sentence.operate = known_commands[sentence.verb.name]
            if sentence.dir_obj_is_known
                sentence.operate(sentence.dir_obj)

"""Here begins the list of things that Donna knows how to do. I am looking for a better way of storing these."""
def learn_to_handle(self):
    """PARAMS
         RETURNS"""

    self.listen(learn = True)

#This is for learning verbs. If no word linked with an operation is found in a sentence, she will try every command she knows on the dir_obj.

def open(self):

def Identify(self, string):
    """PARAMS
         RETURNS"""
    Sentence("string")
    print(xyz + "is a" + word.item_cat[Donna.environment] + word.item_cat.description)

def donnaTry(self, trying, trying_on,):
    """PARAMS
     RETURNS"""
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





don = Donna()
don.listen("play")