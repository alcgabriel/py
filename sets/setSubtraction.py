def find_missing_ids(first_ids, second_ids):
    new_ids = set()
    first_set = set()
    second_set = set()
    for id in first_ids:
        first_set.add(id)
        print(first_set)

    for id in second_ids:
        second_set.add(id)

    new_ids = first_set - second_set
    return new_ids
    
