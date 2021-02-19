import os
import time
from firebase_admin import credentials, firestore, initialize_app
from fastapi import FastAPI
# Initialize FastAPI
app = FastAPI()

# Initialize Firestore DB
cred = credentials.Certificate('poc-ops-rimac.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('ltmle')


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    start_time = time.time()
    todo = todo_ref.document(item_id).get()
    content = todo.to_dict()
    duration = str( time.time()- start_time)
    return {'data': content, 'duration': duration, 'version': '0.0.0_fastapi'}