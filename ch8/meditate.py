def meditate(mana, max_mana, num_potions):
    while mana < max_mana:
        mana += 1
        num_potions -= 1
        if mana == max_mana:
            break
        if num_potions == 0:
            break
    return mana, num_potions
        
