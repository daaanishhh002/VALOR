import requests
import json

# Replace with your actual API key
API_KEY = GMaps_API_KEY  # <-- Add your API Key here

def compute_route(origin_latlng: tuple, destination_latlng: tuple, save_to_file: bool = True) -> dict:
    """
    Computes driving route between origin and destination using Google Maps Routes API.

    Parameters:
        origin_latlng (tuple): (latitude, longitude) of the origin.
        destination_latlng (tuple): (latitude, longitude) of the destination.
        save_to_file (bool): Whether to save the response as 'route.json'. Default is True.

    Returns:
        dict: Parsed JSON response from the API, or None if error occurs.
    """

    url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": (
            "routes.legs.steps.navigationInstruction.maneuver,"
            "routes.legs.steps.distanceMeters,"
            "routes.distanceMeters,"
            "routes.legs.steps.staticDuration,"
            "routes.duration,"
            "routes.legs.steps.endLocation"
        )
    }

    body = {
        "origin": {
            "location": {
                "latLng": {
                    "latitude": origin_latlng[0],
                    "longitude": origin_latlng[1]
                }
            }
        },
        "destination": {
            "location": {
                "latLng": {
                    "latitude": destination_latlng[0],
                    "longitude": destination_latlng[1]
                }
            }
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
        "computeAlternativeRoutes": False
    }

    try:
        response = requests.post(url, headers=headers, json=body)

        if response.status_code == 200:
            result = response.json()

            if save_to_file:
                with open("route.json", "w") as file:
                    json.dump(result, file, indent=4)

            return result
        else:
            print(f"[ERROR] Status Code: {response.status_code}")
            print(response.text)
            return None

    except requests.RequestException as e:
        print("[ERROR] Request failed:", e)
        return None

if __name__ == '__main__':
    origin = (17.427518238491608, 78.44467671445933)
    destination = (17.427635956429683, 78.44147952144611)

    route_data = compute_route(origin, destination)

    if route_data:
        print("[INFO] Route computed successfully.")
    else:
        print("[INFO] Failed to compute route.")


