from typing import List
def spell_combiner(spell1: callable, spell2: callable) -> callable:

    def combined_spell(arg1,arg2):
        res1 = spell1(arg1,arg2)
        res2= spell2(arg1,arg2)

        return (res1,res2)
    
    return(combined_spell)

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def base_spells(arg1,arg2):
        return base_spell(arg1,arg2) * multiplier
    
    return(base_spells)

def conditional_caster(condition: callable, spell: callable) -> callable:
    def get_spell(arg1,arg2):
        if condition(arg1,arg2):
            return spell(arg1,arg2)
        else:
            return "Spell fizzled"
    return (get_spell)

def spell_sequence(spells: List[callable]) -> callable:
    def casts_spells(arg1,arg2):
      results = []
      for spell in spells:
         results.append(spell(arg1,arg2))
      return results
    return casts_spells



    return(casts_spells)
########################
def fireball1(x,y):
    return x + y

def heal(x,y):
    return x *y

combined = spell_combiner(fireball1, heal)
print(combined(5, 6))

########################
def fireball(x,y):
    return x+y

mega_fireball = power_amplifier(fireball, 3)

print(f"Original: {fireball(5,5)}, Amplified: {mega_fireball(10,3)}")

########################

def condition(x,y):
    return x+y > 10

def spell(x,y):
    return(f"good")

mana_gated_fireball = conditional_caster(condition, spell)
print(mana_gated_fireball(5,3))

########################
def spell1(x,y):
    return f"spell1"

def spell2(x,y):
    return f"spell2"

def spell3(x,y):
    return f"spell3"

battle_combo = spell_sequence([spell1, spell2, spell3])

print(battle_combo("hi","dragon"))