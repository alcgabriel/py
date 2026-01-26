def does_attack_hit(attack_roll, armor_class):
    return (attack_roll >= armor_class) and attack_roll != 1 or (attack_roll == 20)

