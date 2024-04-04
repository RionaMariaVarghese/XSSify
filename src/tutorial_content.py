from tutorial_db import Session, TutorialPageContent

session = Session()
session.query(TutorialPageContent).delete()

content_entries = [
    TutorialPageContent(title="INTRODUCTION", content="Cross-Site Scripting (XSS) is a vulnerability in web applications that allows attackers to inject malicious scripts into web pages viewed by other users. XSS attacks can lead to various consequences, including data theft, session hijacking, defacement, and malware distribution. This tutorial aims to introduce beginners to XSS, exploitation, commonly used apps vulnerable to XSS, and preventive measures to mitigate this threat."),
    TutorialPageContent(title="UNDERSTANDING", content="Content for Chapter 2"),
]

for entry in content_entries:
    session.add(entry)

session.commit()

session.close()
