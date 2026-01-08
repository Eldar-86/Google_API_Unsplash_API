from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Spreadsheet import test_order_values
from Authenticate import authenticate

############################################################################################################################################
#Drive functions

def test_create_order_folder():                                             #Creates folder named after the pending order number and returns the folder id
    creds, _, drive_service = authenticate()
    order_list = test_order_values()

    service = build("drive", "v3", credentials=creds)
    file_metadata = {
        "name": f"Order: {order_list[0]}",
        "parents": ["folder_id"],
        "mimeType": "application/vnd.google-apps.folder",
    }

    file = service.files().create(body=file_metadata, fields="id").execute()
    order_folder_id = file.get("id")
    return order_folder_id


def test_uploading_photos():                                                #Uploads photos from ___API to the order# folder
    #           If ___API handles multiple photos, it can return the amount of photos, which can then be used for naming by numbering -- check comment below

    creds, _, drive_service = authenticate()
    folder_id = test_create_order_folder()

    service = build("drive", "v3", credentials=creds)

    file_metadata = {"name": "photo.jpg", "parents": [folder_id]}               #[f"photo_{num+1}.jpg" for num in range(number_of_photos)]
    media = MediaFileUpload("download.jpeg", mimetype="image/jpeg", resumable=True)

    file = (service.files().create(body=file_metadata, media_body=media, fields="id").execute())
    print(f'File ID: "{file.get("id")}".')
    return file.get("id")
