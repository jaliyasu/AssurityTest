import json

def extract_element_from_array():
    import json

    # Sample JSON Data
    data = {
        "Promotions": [
            {"Id": 1, "Name": "Basic", "Description": "Lowest position in category", "Price": 0.0000,
             "MinimumPhotoCount": 0},
            {"Id": 2, "Name": "Gallery", "Description": "Good position in category", "Price": 0.5500,
             "OriginalPrice": 0.5500, "MinimumPhotoCount": 0, "GoodFor2RelistsFee": 0.3500},
            {"Id": 3, "Name": "Feature", "Description": "Better position in category", "Price": 3.4500,
             "OriginalPrice": 3.4500, "Recommended": True, "MinimumPhotoCount": 0, "GoodFor2RelistsFee": 1.9000},
            {"Id": 4, "Name": "Feature Combo",
             "Description": "Best position in category \nIncludes benefits of Feature \nHighlights listing in search results",
             "Price": 3.9500, "OriginalPrice": 3.9500, "MinimumPhotoCount": 0, "GoodFor2RelistsFee": 2.0000}
        ]
    }

    gallery_promotion = list(
        filter(lambda p: p["Name"] == "Gallery" and "Good position in category" in p["Description"],
               data["Promotions"]))