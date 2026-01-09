import requests
from Spreadsheet import test_order_values


############################################################################################################################################
#Function that gets images from Unsplash based on order(s) on spreadsheet via test_order_values() function in Spreadsheet.py:


def test_get_images():                                                  #Returns a list of download links for images
    order_no, year, make, model, trim = test_order_values()
    photo_query = f"{make.lower()} {model.lower()}"
    response = requests.get(
        "https://api.unsplash.com/search/photos",
        params={"query": photo_query,
                "per_page": 30,
                "page": 1,
                "order_by": "relevant",
                "content_filter": "high",
                "client_id": "your_client_id_here"})            ###You will first need to create an app on Unsplash
    content = response.json()

    photo_links = []

    for item in content["results"]:
        description = (item.get("description") or "").lower()
        alt_description = (item.get("alt_description") or "").lower()
        slug = (item.get("slug") or "").lower()
        alt_slug_en = (item.get("alternative_slugs", {}).get("en") or "").lower()

        if (
            make.lower() in description
            or model.lower() in description
            or make.lower() in slug
            or model.lower() in slug
            or make.lower() in alt_slug_en
            or model.lower() in alt_slug_en
            or make.lower() in alt_description
            or model.lower() in alt_description
        ):
            photo_links.append(item["urls"]["regular"])

    return photo_links, photo_query

############################################################################################################################################
