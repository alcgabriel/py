def merge(dict1, dict2):

    guild_merged = {
        
    }
    for players in dict1:
        guild_merged[players] = dict1[players]
    for players in dict2:
        guild_merged[players] = dict2[players]
    for players in dict2:
        print(guild_merged,"guild2")
    return guild_merged
