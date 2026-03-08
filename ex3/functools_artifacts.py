from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Dict, List

def spell_reducer(spells: List[int], operation: str) -> int:

    if operation == "add":
        return reduce(operator.add, spells)

    elif operation == "multiply":
        return reduce(operator.mul, spells)

    elif operation == "max":
        return reduce(max, spells)

    elif operation == "min":
        return reduce(min, spells)
    

def partial_enchanter(base_enchantment: callable) -> Dict[str, callable]:

    fire = partial(base_enchantment, 50, "Fire")
    ice = partial(base_enchantment, 50, "Ice")
    lightning = partial(base_enchantment, 50, "Lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning
    }

def base_enchantment(power, element, target):
    return f"{element} enchant {target} with power {power}"

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)



def spell_dispatcher() -> callable:

    @singledispatch
    def cast(spell):
        return "Unknown spell"

    @cast.register(int)
    def spell_int(spell: int):
        return f"Damage spell: {spell} "

    @cast.register(str)
    def spell_str(spell: str):
        return f"Enchantment: {spell}"

    @cast.register(list)
    def spell_list(spell: list):
        return f"Multi-cast  {len(spell)} "

    return cast
###################

dispatcher = spell_dispatcher()

print(dispatcher(50))
print(dispatcher("Fire Aura"))
print(dispatcher([10,20,30]))

print("Testing spell reducer...")
spells = [10,20,30,40]

print("Sum:", spell_reducer(spells,"add"))
print("Product:", spell_reducer(spells,"multiply"))
print("Max:", spell_reducer(spells,"max"))


partial_enchant =partial_enchanter(base_enchantment)
print(partial_enchant["fire_enchant"]("targ1"))
print(partial_enchant["ice_enchant"]("targ2"))
print(partial_enchant["lightning_enchant"]("targ3"))

print("\nTesting memoized fibonacci...")
print("Fib(10):", memoized_fibonacci(10))
print("Fib(15):", memoized_fibonacci(15))