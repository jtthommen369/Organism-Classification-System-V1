movement = input("Movement detected? yes/no: ").lower()
heat = input("Heat detected? yes/no: ").lower()
color = input("Color: ").lower()
size = input("Size (small/medium/large): ").lower()
angularity = input("Angular? yes/no: ").lower()
shape = input("Shape (spherical/irregular/flat): ").lower()

animal_score = 0
plant_score = 0
inanimate_score = 0

# Animal rules
if movement == "yes":
    animal_score += 1

if heat == "yes":
    animal_score += 1

if size == "large":
    animal_score += 1

# Plant rules
if color == "green":
    plant_score += 1

if movement == "no":
    plant_score += 1

if heat == "no":
    plant_score += 1

# Inanimate rules
if angularity == "yes":
    inanimate_score += 1

if shape == "flat" or shape == "spherical":
    inanimate_score += 1

if heat == "no":
    inanimate_score += 1

# Final classification
if animal_score > plant_score and animal_score > inanimate_score:
    print("Likely Animal")

elif plant_score > animal_score and plant_score > inanimate_score:
    print("Likely Plant")

elif inanimate_score > plant_score and inanimate_score > animal_score:
    print("Likely Inanimate")

else:
    print("Classification uncertain")