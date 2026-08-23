from typing import TYPE_CHECKING

from .options import SpellUnlockMethod
from .data.beings import HeroKit
from .data.consts import WORLDS_PER_RUN
from .data.spells import SpellBrand, SpellPack, Spell
from rule_builder.rules import Rule, True_, Has, HasAny, HasAllCounts, HasFromList, False_

if TYPE_CHECKING:
    from . import OSFEWorld

# Bosses should be in logic for world 1, since you can reset to get any boss first
# Remember basic gunner has 0 mana regen lol

def set_all_rules(world: "OSFEWorld"):
    _set_character_rules(world)
    _set_completion_rule(world)

def _set_character_rules(world: "OSFEWorld"):
    for kit in world.characters:
        hero_start = world.get_entrance(f"{world.origin_region_name} to [{kit.value.name}] World 1 Zones")
        hero_can_progress = Has(f"Hero Unlock: {kit.value.name}") & _hero_can_kill(kit, world.options.spell_unlock_method)
        world.set_rule(hero_start, hero_can_progress)

        # As a very coarse heuristic, assert at least one hell pass down must be acquired per boss,
        # starting at world 3 to keep sphere 0 a reasonable size
        if (world.options.hellpass_down and
            world.options.hellpass_mode.value != world.options.hellpass_mode.option_Disabled):
            worlds = WORLDS_PER_RUN if kit.value.name != "Shopkeeper" else WORLDS_PER_RUN + 1
            for world_no in range(3, worlds + 1):
                pass_down_count = world_no - 2
                if world.options.vanilla_hellpass_level.value >= pass_down_count:
                    boss_win = world.get_entrance(f"[{kit.value.name}] World {world_no} Zones to [{kit.value.name}] World {world_no} Boss")
                    world.set_rule(boss_win, HasFromList("Hell Pass Down", count=pass_down_count))

def _set_completion_rule(world: "OSFEWorld"):
    specific_win_counts: dict[str, int] = {}
    if world.options.pacifist_wins.value > 0:
        specific_win_counts["Pacifist Victory"] = world.options.pacifist_wins.value
    if world.options.neutral_wins.value > 0:
        specific_win_counts["Neutral Victory"] = world.options.neutral_wins.value
    if world.options.genocide_wins.value > 0:
        specific_win_counts["Genocide Victory"] = world.options.genocide_wins.value
    cond = (HasAllCounts(specific_win_counts) &
            HasFromList(
                *("Pacifist Victory", "Neutral Victory", "Genocide Victory"),
                count=world.options.total_wins.value
            ))

    world.set_completion_rule(cond)

def _hero_can_kill(kit: HeroKit, spell_mode: SpellUnlockMethod) -> Rule:
    if kit.value.damaging_weapon:
        return True_()

    # Individual card unlocks are valid regardless of mode, since they are used for starting inventory
    damage_spells: list[Spell] = [spell for spell in kit.value.starting_spells if spell.value.is_damaging]
    card_unlocks: list[str] = [f"Spell Card: {spell.value.name}" for spell in damage_spells]
    match spell_mode:
        case SpellUnlockMethod.option_Individual:
            return HasAny(*card_unlocks)
        case SpellUnlockMethod.option_Brand:
            damage_brands = []
            for damage_spell in damage_spells:
                for brand in SpellBrand:
                    if damage_spell in brand.value:
                        damage_brands.append(brand)
            brand_unlocks = [f"Brand Unlock: {brand.name}" for brand in damage_brands]
            return HasAny(*brand_unlocks) | HasAny(*card_unlocks)
        case SpellUnlockMethod.option_Pack:
            damage_packs = []
            for damage_spell in damage_spells:
                for pack in SpellPack:
                    if damage_spell in pack.value:
                        damage_packs.append(pack)
            pack_unlocks = [f"Spell Booster Pack: {pack.name}" for pack in damage_packs]
            return HasAny(*pack_unlocks) | HasAny(*card_unlocks)
    return False_()
