import time
import functools


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(arg1=None, arg2=None):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(arg1, arg2)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(self, spell_name, power):
            if power >= min_power:
                return func(self, spell_name, power)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(arg1, arg2):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(arg1, arg2)
                except Exception:
                    attempts += 1
                    print(f"Spell failed, retrying... (attempt {attempts}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return name.replace(" ", "").isalpha() and len(name) >= 3

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def fireball(arg1, arg2):
        time.sleep(0.1)
        return f"Fireball cast with {arg1} and {arg2}!"

    print(fireball(5, 10))

    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf")) 
    print(MageGuild.validate_mage_name("Al"))      

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5)) 