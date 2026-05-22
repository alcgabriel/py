def remove_duplicates(spells):
    known_spells = set()
    unique_spells = []
    for spell in spells:
        known_spells.add(spell)
        print(known_spells)
        if spell not in unique_spells:
            unique_spells.append(spell)
        print(unique_spells)
    return(unique_spells)