# VARIABLES-------------------------------------------------

my_var = 10 + 4 / 2
my_name = "DJ"
is_true = not False
none_type_variable = None
sword_name, sword_damage, sword_length = "Slayer", 15, 8
number_flooring = 7 // 3
number_exponent = 3 ** 2
another_number = 16_000_000  # underscore for readability

# PRINTING-------------------------------------------------

print(f"my name is {type(my_name)}")
print(f"my var is {my_var}")
print(none_type_variable is None)  # default value to be replaced later
print(round(my_var))  # avg
print(16e3)  # 16000.0
print(7.1e-2)  # 0.071


# FUNCTIONS-------------------------------------------------


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


def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched


# LOOPS-------------------------------------------------


def print_numbers():
    for i in range(0, 5, 1):  # 3rd number is increment
        print(i)


def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total


def regenerate(current_health, max_health, enemy_distance):
    while enemy_distance > 3 and current_health < max_health:
        current_health += 1
        enemy_distance -= 2
    return current_health


def calculate_experience_points(level):
    total_exp = 0
    while level > 1:
        level -= 1
        total_exp += exp_per_lvl(level)

    return total_exp


def exp_per_lvl(level):
    exp = level * 5
    return exp


# MAIN-------------------------------------------------


def main():  # clear entry points and defined vars/functions
    print("Running Cheat Sheet!\n-------------------")
    print_numbers()
    print(f"Exp needed for lvl 2: {calculate_experience_points(2)}")


main()
