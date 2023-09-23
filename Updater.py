import requests

API_KEY = "" # https://create.roblox.com/docs/cloud/open-cloud/managing-api-keys
UNIVERSE_ID = 0 # Universe ID not GAME PLACE ID

COOKIES = {
    ".ROBLOSECURITY": "" # Roblox Cookie
}

def get_and_publish_place(place):
    print("Getting place file for", place["name"], place["id"])
    
    place_data = requests.get(f"https://assetdelivery.roblox.com/v1/asset/?id={place['id']}", cookies=COOKIES)
    version = int(place_data.history[0].headers["roblox-assetversionnumber"])
    
    print("Publishing version", version, "as version", version + 1)
    
    response = requests.post(
        f"https://apis.roblox.com/universes/v1/{UNIVERSE_ID}/places/{place['id']}/versions?versionType=Published",
        data=place_data.content,
        headers={"x-api-key": API_KEY}
    )
    
    print("Published", response.text)
    print()

def main():
    try:
        places_url = f"https://develop.roblox.com/v1/universes/{UNIVERSE_ID}/places?sortOrder=Asc&limit=100"
        places_response = requests.get(places_url).json()
        places = places_response.get("data", [])

        for place in places:
            get_and_publish_place(place)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
