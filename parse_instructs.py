import json
# import 
# as mc

# Open and read the JSON file
with open('route.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Now 'data' is a Python dictionary
# You can access elements like this:
steps = data["routes"][0]["legs"][0]["steps"]

# Print parsed steps
for i, step in enumerate(steps):
    maneuver = step["navigationInstruction"]["maneuver"]
    dist = step["distanceMeters"]
    duration = step["staticDuration"]
    if 'LEFT' or 'RIGHT' not in maneuver:
        # mc.go_forward()
        pass
    elif 'LEFT' in maneuver:
        # mc.turn_left()
        # mc.go_forward()
        pass
    elif 'RIGHT' in maneuver:
        # mc.turn_right()
        # mc.go_forward()
        pass
    else:
        # mc.stop()
        # mc.cleanup()
        pass
    print(f"Step {i+1}: Go {dist}m in ~{duration} → Action: {maneuver}")

print("Destination Reached")
print("Vehicle Stopped")