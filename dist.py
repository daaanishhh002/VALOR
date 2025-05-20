import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth 
    using the Haversine formula.
    
    Parameters:
        lat1, lon1: Latitude and Longitude of point A (in degrees)
        lat2, lon2: Latitude and Longitude of point B (in degrees)
    
    Returns:
        Distance in kilometers (float)
    """
    # Radius of Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

# Example usage
if __name__ == "__main__":
    # Replace these with your actual coordinates
    lat1, lon1 = 17.385044, 78.486671  # Hyderabad
    lat2, lon2 = 12.971599, 77.594566  # Bangalore

    distance_km = haversine_distance(lat1, lon1, lat2, lon2)
    print(f"Distance: {distance_km} km")
