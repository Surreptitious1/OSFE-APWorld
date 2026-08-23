from BaseClasses import Location
from .data.beings import HeroKit, KillonlyBoss, SpareableBoss, SpareonlyBoss
from .data.consts import WORLDS_PER_RUN, ZONES_PER_WORLD

class OSFELocation(Location):
    game = "One Step From Eden"

def _propagate_location_table() -> tuple[dict[str, int], dict[HeroKit, list[str]]]:
    location_id: int = 1
    _location_str_to_id: dict[str, int] = {}
    _location_str_by_hero: dict[HeroKit, list[str]] = {}
    for kit in HeroKit:
        _location_str_by_hero[kit] = []

    def _append_location(hero: HeroKit, where: str):
        nonlocal location_id
        location_str = f"[{hero.value.name}] {where}"
        _location_str_to_id[location_str] = location_id
        _location_str_by_hero[hero].append(location_str)
        location_id += 1

    for hero in HeroKit:
        # Shopkeeper goes through 8 normal worlds instead of 7
        worlds = WORLDS_PER_RUN if hero.value.name != "Shopkeeper" else WORLDS_PER_RUN + 1
        for world_no in range(1, worlds + 1):
            for zone_no in range(1, ZONES_PER_WORLD + 1):
                _append_location(hero, f"World {world_no}, Zone {zone_no}")
        for zone_no in range(1, ZONES_PER_WORLD + 1):
            _append_location(hero, f"Eden, Zone {zone_no}")
        for boss in SpareableBoss:
            if not boss.name in hero.name:
                _append_location(hero, f"Kill {boss.value}")
                _append_location(hero, f"Spare {boss.value}")
        for boss in KillonlyBoss:
            # No shopkeeper suicide
            if not boss.name in hero.name:
                _append_location(hero, f"Kill {boss.value}")
        for boss in SpareonlyBoss:
            # Special case for Terrable so you don't have to do a whole extra pacifist run just to kill her
            _append_location(hero, f"Spare {boss.value}")

    return _location_str_to_id, _location_str_by_hero

location_str_to_id, location_str_by_hero = _propagate_location_table()