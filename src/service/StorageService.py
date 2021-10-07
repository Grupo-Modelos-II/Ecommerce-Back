from tempfile import SpooledTemporaryFile

from config.firebaseConfig import get_storage_client

def upload_file_service(file: SpooledTemporaryFile, destination: str, content_type: str) -> str:
    bucket = get_storage_client()
    blob = bucket.blob(destination)
    blob.upload_from_file(file, content_type = content_type)
    blob.make_public()
    return blob.public_url