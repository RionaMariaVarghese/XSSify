from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

class TutorialPageContent(Base):
    __tablename__ = 'tutorial_page_content'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)

engine = create_engine('sqlite:///tutorial_content.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
