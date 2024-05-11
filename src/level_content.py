from level_db import Session, LevelPageContent

session = Session()
session.query(LevelPageContent).delete()

# Add content to the database
content_entries = [
    LevelPageContent(
        question='What is the primary goal of an XSS attack?',
        option1='Gain unauthorized access to a database',
        option2='Deface a website',
        option3='Execute arbitrary code in a victim\'s browser',
        option4='Create a denial-of-service attack',
        answer='Execute arbitrary code in a victim\'s browser',
        requires_input=0
    ),
    LevelPageContent(
        question='What is the primary goal of an XSS attack?',
        option1='Reflected XSS',
        option2='DOM XSS',
        option3='Refracted XSS',
        option4='Stored XSS',
        answer='Refracted XSS',
        requires_input=0
    ),
    LevelPageContent(
        question='Which programming language is commonly used for XSS payloads?',
        answer='JavaScript',
        requires_input=1
    )
]

for entry in content_entries:
    session.add(entry)

session.commit()

session.close()