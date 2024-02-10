locations = ["sofa", "garage", "chair", "table", "closet"]

key_location = "chair"

for location in locations:
    if location == key_location:
        print("key is found at", location)
        break
    else:
        print("key is not found at ", location)
