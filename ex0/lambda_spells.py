from typing import List,Dict

def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda art:art["power"], reverse=True)

def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:

    return list(filter(lambda mage: mage['power'] >= min_power, mages))

def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda spell: "*" + spell +"*", spells))

def mage_stats(mages: List[dict]) -> Dict:
    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = sum(m["power"] for m in mages) / len(mages)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": f"{avg_power:.2f}"
    }


artifacts = [
    {"name": "Crystal Orb", "power": 85, "element": "fire"},
    {"name": "Fire Staff", "power": 92, "element": "lightning"},
]

artifacts_sorter = artifact_sorter(artifacts)

str_list = ''
i = 0
for art in artifacts_sorter:
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

power_filters = power_filter(mages,78)

print(power_filters)

spells = ["fireball", "heal", "shield"]

spells_transformer =  spell_transformer(spells)


spell_str = " ".join(spells_transformer)
print("Testing spell transformer...")
print(spell_str)

mages = [
    {"name": "Gandalf", "power": 95},
    {"name": "Merlin", "power": 80},
    {"name": "Morgana", "power": 70},
]
stats = mage_stats(mages)
print(stats)