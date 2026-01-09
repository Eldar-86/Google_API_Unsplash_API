from googleapiclient.discovery import build
from Unsplash_image_get import test_get_images
from Spreadsheet import test_order_values
from Authenticate import authenticate
import requests
from io import BytesIO
from googleapiclient.http import MediaIoBaseUpload

############################################################################################################################################
#Drive functions

def test_create_order_folder():                                             #Creates folder named after the pending order number and returns the folder id
    creds, _, drive_service = authenticate()
    order_list = test_order_values()

    service = build("drive", "v3", credentials=creds)
    file_metadata = {
        "name": f"Order: {order_list[0]}",
        "parents": ["set_id_of_drive_here"],                    ###You can use the function to create the folder, and it will return the folder id.
        "mimeType": "application/vnd.google-apps.folder",
    }

    file = service.files().create(body=file_metadata, fields="id").execute()
    order_folder_id = file.get("id")
    return order_folder_id


def test_uploading_photos():                                                #Uploads photos from ___API to the order# folder
    creds, _, drive_service = authenticate()
    folder_id = test_create_order_folder()

    list_of_photo_links_unsplash, query = test_get_images()
    number_of_remaining_photos = len(list_of_photo_links_unsplash)

    service = build("drive", "v3", credentials=creds)

    for num, link in enumerate(list_of_photo_links_unsplash):
        url = link
        response = requests.get(url)
        file_data = BytesIO(response.content)
        media = MediaIoBaseUpload(file_data, mimetype="image/jpeg", resumable=True)

        file_metadata = {"name": f"photo{num+1}.jpg", "parents": [folder_id]}
        file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
        print(f"{num+1} out of {number_of_remaining_photos} photo(s) completed...")
#        print(file.get("id")) you can create a log.txt file and store file ids per order

############################################################################################################################################
