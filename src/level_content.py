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
        question='What type of cross-site scripting (XSS) attack occurs when the injected script is reflected off the web server but originates from an external source, such as in a URL parameter?',
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
    ),
    LevelPageContent(
        question='Code sanitization converts the symbol, "<" to?',
        answer='&lt;',
        requires_input=1
    ),
    LevelPageContent(
        question='Full form of DOM?',
        answer='Document Object Model',
        requires_input=1
    ),
    LevelPageContent(
        question='Which of the following is NOT a common technique to prevent XSS attacks?',
        option1='Session management',
        option2='Input validation"',
        option3='Output encoding',
        option4='Content Security Policy (CSP)',
        answer='Session management',
        requires_input=0
    ),
    LevelPageContent(
        question='What does XSS stand for?',
        answer='Cross Site Scripting',
        requires_input=1
    ),
    LevelPageContent(
        question='Which type of XSS attack occurs when user input is reflected immediately without any sanitization?',
        option1='Stored XSS',
        option2='DOM-based XSS',
        option3='Reflected XSS',
        option4='Persistent XSS',
        answer='Reflected XSS',
        requires_input=0
    ),
    LevelPageContent(
        question='What does CSP stand for?',
        answer='Content Security Policy',
        requires_input=1
    ),
    LevelPageContent(
        question='Write a script that can pop up an alert message "1".',
        answer='<script>alert("1")</script>',
        requires_input=1
    ),
    LevelPageContent(
        question='Which HTML tag is commonly used to sanitize user input and prevent XSS attacks?',
        option1='<input>',
        option2='<div>',
        option3='<script>',
        option4='<textarea>',
        answer='<textarea>',
        requires_input=0
    ),
    LevelPageContent(
        question='In e-commerce websites, where are XSS vulnerabilities often found?',
        answer='Injection',
        requires_input=1
    ),
    LevelPageContent(
        question='Number of main types of XSS?',
        answer='3',
        requires_input=1
    ),
    LevelPageContent(
        question='Which type of XSS attack occurs when the attacker can manipulate client-side scripts to execute malicious code in the victim\'s browser?',
        option1='Reflected XSS',
        option2='DOM-based XSS',
        option3='Stored XSS',
        option4='Server-side XSS',
        answer='DOM-based XSS',
        requires_input=0
    ),
    LevelPageContent(
        question='What field is ususally targeted for XSS attack? (Input/Image/Database)',
        answer='input',
        requires_input=1
    )
]

for entry in content_entries:
    session.add(entry)

session.commit()

session.close()