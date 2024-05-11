from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class LevelPageContent(Base):
    __tablename__ = 'levels_ques_ans'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    option1 = Column(String)
    option2 = Column(String)
    option3 = Column(String)
    option4 = Column(String)
    answer = Column(String)
    requires_input = Column(Integer)

engine = create_engine('sqlite:///level_content.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
