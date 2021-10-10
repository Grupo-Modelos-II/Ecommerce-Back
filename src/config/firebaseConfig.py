from os import getenv

from firebase_admin import credentials, initialize_app, storage

def init_firebase():
    _ecommerce_credentials = credentials.Certificate('../private/secret.json')
    initialize_app(_ecommerce_credentials, {
        'storageBucket': getenv('FIREBASE_BUCKET')
    })

def get_storage_client():
    return storage.bucket()