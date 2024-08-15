my_var = 10 + 4 / 2
my_name = "DJ"
is_true = True
none_type_variable = None
sword_name, sword_damage, sword_length = "Slayer", 15, 8
number_flooring = 7 // 3
number_exponent = 3 ** 2
another_number = 16_000_000  # underscore for readability
# comment

print(f"my name is {type(my_name)}")
print(f"my var is {my_var}")
print(none_type_variable is None)  # default value to be replaced later
print(round(my_var))  # avg
print(16e3)  # 16000.0
print(7.1e-2)  # 0.071


def area_of_circle(radius):
    pi = 3.14
    area = pi * radius ** 2  # ex of number exponents
    return area


sword_area = area_of_circle(sword_length)
print(sword_area)


def take_magic_damage(health, resist, amp, spell_power):
    amped_dmg = spell_power * amp
    reduced_dmg = amped_dmg - resist
    return health - reduced_dmg


def main():  # clear entry points and defined vars/functions
    print("Running Cheat Sheet!")


main()
