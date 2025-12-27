def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp
    real_damage = total_damage - resist
    new_health = real_damage - health
    return new_health
