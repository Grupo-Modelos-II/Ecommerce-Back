from tempfile import SpooledTemporaryFile

from config.firebaseConfig import get_storage_client

def upload_file_service(file: SpooledTemporaryFile, destination: str, content_type: str) -> str:
    bucket = get_storage_client()
    blob = bucket.blob(destination)
    blob.upload_from_file(file, content_type = content_type)
    blob.make_public()
    return blob.public_url

def get_file_url_service(file_name: str) -> str:
    listUrl = get_list_file_url_service(file_name, 1)
    return listUrl[0] if len(listUrl) > 0 else None

def get_list_file_url_service(folder_location: str, max_results: int = None) -> list[str]:
    bucket = get_storage_client()
    blobs = bucket.list_blobs(prefix=folder_location, max_results=max_results)
    listUrl = [blob.public_url for blob in blobs]
    return listUrl[1:] if max_results is None else listUrl