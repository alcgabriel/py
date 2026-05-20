def get_quest_status(progress):
    print(progress["quests"]["bridge_run"])
    status = progress["quests"]["bridge_run"]["status"]
    return status
