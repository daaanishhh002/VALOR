import threading
import app
import time
from route import compute_route
from gps import get_gps_coordinates
import motor_control as mc
from dist import haversine_distance


def start_flask():
    app.run_server()


if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()
    print("[INFO] Flask server is running in a background thread.")
    time.sleep(30)

    latDest, lngDest = app.destination_coords['destination'].values()
    latNow, lngNow = get_gps_coordinates()
    route = compute_route((latNow, lngNow), (latDest, lngDest))
    steps = route["routes"][0]["legs"][0]["steps"]
    print(f"Destination is {route["routes"][0]["distanceMeters"]}m away.")
    print(f"Destination will be reached in {route["routes"][0]["duration"]} mins.")

    # Place your main application logic below
    while True:
        print("[INFO] Main application doing other tasks...")
        latNow, lngNow = get_gps_coordinates()

        for i, step in enumerate(steps):
            maneuver = step["navigationInstruction"]["maneuver"]
            stepDist = step["distanceMeters"]
            stepDuration = step["staticDuration"]
            stepEndLat, stepEndLng = step["endLocation"]["latLng"]

            print(f"Step {i+1}: Go {stepDist}m in ~{stepDuration} → Action: {maneuver}")
            
            if 'LEFT' or 'RIGHT' not in maneuver:
                while haversine_distance(*get_gps_coordinates(), stepEndLat, stepEndLng) >= 0:
                    mc.go_forward()
            elif 'LEFT' in maneuver:
                mc.turn_left()
                while haversine_distance(*get_gps_coordinates(), stepEndLat, stepEndLng) >= 0:
                    mc.go_forward()
            elif 'RIGHT' in maneuver:
                mc.turn_right()
                while haversine_distance(*get_gps_coordinates(), stepEndLat, stepEndLng) >= 0:
                    mc.go_forward()
            else:
                pass
                # mc.stop()
                # mc.cleanup()

        time.sleep(5)
        # compute_route()
        # while app.data is not None:
        #     compute_route(gps_lat, gps_lng, app.data, )
