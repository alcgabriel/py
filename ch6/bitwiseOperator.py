can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    user_can_create_bits = can_create_guild & can_delete_guild


def get_review_bits(user_permissions):
    user_can_review_bits = can_review_guild & can_delete_guild

def get_delete_bits(user_permissions):
    pass


def get_edit_bits(user_permissions):
    pass
