import os

from typing import Union
from typing import Dict
from typing import Any

# Firebase Admin
from firebase_admin import initialize_app  # type: ignore
from firebase_admin import credentials
from firebase_admin import firestore


service_account_path = os.path.join(os.path.dirname(__file__), '..', 'service-account.json')
credential = credentials.Certificate(service_account_path)
initialize_app(credential)

db = firestore.client()

# ============================================================
# Users
# ============================================================


def get_users():
    return db.collection('users').get()


def get_user(user_id: str):
    return db.collection('users').document(user_id).get()


def create_user(user_data: Union[Dict[str, Any], object]):

    if isinstance(user_data, object):
        collection_id = user_data.username  # type: ignore
        password = user_data.password  # type: ignore
    else:
        collection_id = user_data['username']
        password = user_data['password']

    user_ref = db.collection('users').document(collection_id)
    user_ref.set({ 'password': password })

# ============================================================
# Tasks
# ============================================================

def get_tasks(user_id: str):
    return db.collection('users')\
        .document(user_id)\
            .collection('tasks').get()

def get_task(user_id: str, task_id: str):
    return db.collection('users')\
        .document(user_id)\
            .collection('tasks').document(task_id).get()


def create_task(user_id: str, task_data: Union[Dict[str, Any], object]):

    if isinstance(task_data, dict):
        title = task_data['title']
        description = task_data['description']

        status = task_data['status']
    else:
        title = task_data.title  # type: ignore
        description = task_data.description  # type: ignore
        status = task_data.status  # type: ignore

    tasks_collection_ref = db.collection('users')\
        .document(user_id).collection('tasks')

    tasks_collection_ref.add({
        'title': title,
        'description': description,
        'status': status
    })


def update_task(user_id: str, task_id: str, task_data: Union[Dict[str, Any], object]):
        if isinstance(task_data, dict):
            title = task_data['title']
            description = task_data['description']
            status = task_data['status']
        else:
            title = task_data.title  # type: ignore
            description = task_data.description  # type: ignore
            status = task_data.status  # type: ignore

        tasks_collection_ref = db.collection('users')\
            .document(user_id).collection('tasks')

        tasks_collection_ref.document(task_id).update({
            'title': title,
            'description': description,
            'status': status
        })


def update_task_status(user_id: str, task_id: str, status: str):
    tasks_collection_ref = db.collection('users')\
        .document(user_id).collection('tasks')

    tasks_collection_ref.document(task_id).update({ 'status': status })


def delete_task(user_id: str, task_id: str):
    tasks_collection_ref = db.collection('users')\
        .document(user_id).collection('tasks')

    tasks_collection_ref.document(task_id).delete()
