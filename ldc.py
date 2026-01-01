import math

print("Enter your location:")
lat1 = float(input("Latitude: "))
lon1 = float(input("Longitude: "))

print("\nEnter friend'S location:")
lat2 = float(input("Latitude: "))
lon2 = float(input("Longitude: "))



def bearing(lat1_deg, lon1_deg, lat2_deg, lon2_deg):
    # convert degrees to radians
    lat1 = math.radians(lat1_deg)
    lon1 = math.radians(lon1_deg)
    lat2 = math.radians(lat2_deg)
    lon2 = math.radians(lon2_deg)

    dlon = lon2 - lon1

    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)

    angle_rad = math.atan2(x, y)
    angle_deg = (math.degrees(angle_rad) + 360) % 360

    return angle_deg

you_look = bearing(lat1, lon1, lat2, lon2)
friend_look = bearing(lat2, lon2, lat1, lon1)

print("\nResults:")
if lat1 == lat2 and lon1 == lon2:
    print("Both locations are the same. No direction exists.")
else:
    print("You should look at:", round(you_look, 1), "degrees")
    print("Your friend should look at:", round(friend_look, 1), "degrees")
