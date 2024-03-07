from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/mario/Project/SECURIX/XSSify/XSSify/xssify-firebase-adminsdk-twwbd-16832c5e50.json")
firebase_app = initialize_app(cred)
db = firestore.client()

def get_data_from_firestore():
    questions_ref = db.collection("levels")
    questions = questions_ref.get()
    return [question.to_dict() for question in questions]

