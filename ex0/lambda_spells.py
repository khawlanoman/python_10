artifacts = [
    {"name": "Flame Orb", "power": 85, "element": "fire"},
    {"name": "Aqua Trident", "power": 72, "element": "water"},
    {"name": "Thunder Amulet", "power": 90, "element": "lightning"},
    {"name": "Stone Guardian", "power": 65, "element": "earth"},
    {"name": "Wind Dagger", "power": 78, "element": "air"}
]
artifact_sorter = sorted(artifacts, key=lambda art:art["power"])

print(artifact_sorter)