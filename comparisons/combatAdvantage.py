def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
        return advantage, disadvantage, evenly_matched
    elif player_power == enemy_defense:
        evenly_matched = True
        return advantage, disadvantage, evenly_matched
    else: 
        disadvantage = True
        return advantage, disadvantage, evenly_matched
    return advantage, disadvantage, evenly_matched

