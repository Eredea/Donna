from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///Donna.db')
Session = sessionmaker(bind=engine)
session = Session()

def LearnNewWord(word):
    session.add(word)

def MakeWordObj(word):
    word_obj = session.query(InterpretedWord).filter(InterpretedWord.name == word)
    return word_obj[0]

def SearchKnownWords(result_as = None, searching_for = None, ):
    if searching_for == None && result_as == None:
        known_words = session.query(InterpretedWord.name)

        return known_words

    elif result_as == None:
        known_words = session.query(InterpretedWord.name).filter(InterpretedWord.searching_for == "1")
        pass


    return known_words

class InterpretedWord(Base):
    """Word Objects are SQLalchemy database objects worked with- and usually created within- Sentence objects."""
    __tablename__ = 'KnownWords'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    is_operative = Column(Integer)
    linked_operation = Column(Integer)
    operated_by = Column(String(250))
    cat_item = Column(Integer,)

"""class Songs(Base):
    __tablename__ = 'Songs'
    name = Column(Integer)
    album = Column(Integer)
    desc = Column(Integer)
    genre = Column(Integer)
    artist = Column(Integer)


    def extend_info(self, id, info):
        pass
    def NewCatItem(self, *args):
        #return something(Donna.word_item_DB[self.string])
        pass"""




Base.metadata.create_all(engine)

play = InterpretedWord(name = "play", is_operative = 1)
session.add(play)

for word in SearchKnownWords():
    print(word.name)
print(SearchKnownWords())




