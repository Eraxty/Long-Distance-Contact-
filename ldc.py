import math


def dms_to_decimal(deg, minutes, seconds, direction):
    decimal = deg + minutes / 60 + seconds / 3600
    if direction in ("S", "W"):
        decimal *= -1
    return decimal


print("Enter your location (DMS format): ")
lat_deg = int(input("Latitude degrees: "))
lat_min = int(input("Latitude minutes: "))
lat_sec = float(input("Latitude seconds: "))
lat_dir = input("Latitude direction (N/S): ").upper()

lon_deg = int(input("Longitude degrees: "))
lon_min = int(input("Longitude minutes: "))
lon_sec = float(input("Longitude seconds: "))
lon_dir = input("Longitude direction (E/W): ").upper()

lat1 = dms_to_decimal(lat_deg, lat_min, lat_sec, lat_dir)
lon1 = dms_to_decimal(lon_deg, lon_min, lon_sec, lon_dir)


print("\nEnter FRIEND'S location (DMS format):")
lat_deg = int(input("Latitude degrees: "))
lat_min = int(input("Latitude minutes: "))
lat_sec = float(input("Latitude seconds: "))
lat_dir = input("Latitude direction (N/S): ").upper()

lon_deg = int(input("Longitude degrees: "))
lon_min = int(input("Longitude minutes: "))
lon_sec = float(input("Longitude seconds: "))
lon_dir = input("Longitude direction (E/W): ").upper()

lat2 = dms_to_decimal(lat_deg, lat_min, lat_sec, lat_dir)
lon2 = dms_to_decimal(lon_deg, lon_min, lon_sec, lon_dir)


def bearing(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    diff_lon = lon2 - lon1

    x = math.sin(diff_lon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(diff_lon)

    angle_rad = math.atan2(x, y)
    angle_deg = (math.degrees(angle_rad) + 360) % 360

    return angle_deg

def great_circle_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

distance = great_circle_distance(lat1, lon1, lat2, lon2)
you_look = bearing(lat1, lon1, lat2, lon2)
friend_look = bearing(lat2, lon2, lat1, lon1)
    
print("\nResults:")

if lat1 == lat2 and lon1 == lon2:
    print("Both locations are the same. No direction exists.")
else:    
    print("Great-circle distance:", round(distance, 2), "km")
    print("You should look at:", round(you_look, 1), "degrees")
    print("Your friend should look at:", round(friend_look, 1), "degrees")
