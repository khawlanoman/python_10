artifacts = [
    {"name": "Crystal Orb", "power": 85, "element": "fire"},
    {"name": "Fire Staff", "power": 92, "element": "lightning"},
]
artifact_sorter = sorted(artifacts, key=lambda art:art["power"], reverse=True)

str_list = ''
i = 0
for art in artifact_sorter:
    str_list +=(f"{art['name']} ({art['power']} power)")
    if i == 0:
        str_list += " comes before "
        i += 1
print("\nTesting artifact sorter...")
print(str_list,"\n")

mages = [
    {"name": "Arion", "power": 90, "element": "fire"},
    {"name": "Selene", "power": 85, "element": "water"},
    {"name": "Zephyr", "power": 78, "element": "air"},
    {"name": "Terran", "power": 80, "element": "earth"}
]
min_power = min(mages, key=lambda mage: mage['power'])['power']
power_filter = list(filter(lambda mage: mage['power'] >= min_power, mages))

#print(power_filter)

spells = ["fireball", "heal", "shield"]

spell_transformer = list(map(lambda spell: "*" + spell +"*", spells))

spell_str = " ".join(spell_transformer)
print("Testing spell transformer...")
print(spell_str)