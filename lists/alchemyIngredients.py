def check_ingredient_match(recipe, inventory):
    missing_items = []
    item_count = 0
    for items in recipe:
        if items not in inventory:
           missing_items.append(items)
        if items in inventory:
            item_count = item_count + 1
            
    
    percentage = item_count / len(recipe) * 100
   
    
    
    return percentage, missing_items
