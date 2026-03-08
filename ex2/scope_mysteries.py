from typing import Dict
def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def add_power(amount):
        nonlocal total_power
        total_power += amount
        return total_power

    return add_power

def enchantment_factory(enchantment_type: str) -> callable:
    
    def enchant(item_name):
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, callable]:
    memory = {} 

    def store(key, value):
        memory[key] = value
        return f"Stored {key}"

    def recall(key):
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


#######################
print("Testing mage counter...")

counter = mage_counter()

print("Call 1:", counter())
print("Call 2:", counter())
print("Call 3:", counter())


print("\nTesting enchantment factory...")

flaming = enchantment_factory("Flaming")
frozen = enchantment_factory("Frozen")

print(flaming("Sword"))
print(frozen("Shield"))

vault = memory_vault()
print(vault['store']("name","secret_spell"))
print(vault['recall']("name"))