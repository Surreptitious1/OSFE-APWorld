from typing import TYPE_CHECKING

from BaseClasses import Region
from .data.beings import SpareableBoss
from .locations import location_str_by_hero, OSFELocation, location_str_to_id
from .data.consts import WORLDS_PER_RUN
from .items import OSFEItem

if TYPE_CHECKING:
    from . import OSFEWorld

def create_regions_and_locations(world: "OSFEWorld"):
    def _add_locations_by_pattern(pattern: str, region: Region):
        nonlocal locations
        matches = [l for l in locations if pattern in l]
        for loc_str in matches:
            region.add_locations({loc_str: location_str_to_id[loc_str]})
            locations.remove(loc_str)

    def _add_spareable_boss_locations(region: Region):
        nonlocal locations
        for boss in SpareableBoss:
            if boss.value in kit.value.name:
                continue
            matches = [l for l in locations if boss.value in l]
            for loc_str in matches:
                region.add_locations({loc_str: location_str_to_id[loc_str]})
                locations.remove(loc_str)

    world.multiworld.regions += [Region(world.origin_region_name, world.player, world.multiworld)]
    for kit in world.characters:
        prev: Region = world.get_region(world.origin_region_name)
        locations = location_str_by_hero[kit]
        worlds = WORLDS_PER_RUN if kit.value.name != "Shopkeeper" else WORLDS_PER_RUN + 1
        for world_no in range(1, worlds + 1):
            region_zones = Region(f"[{kit.value.name}] World {world_no} Zones", world.player, world.multiworld)
            region_boss = Region(f"[{kit.value.name}] World {world_no} Boss", world.player, world.multiworld)
            world.multiworld.regions += [region_zones, region_boss]
            _add_locations_by_pattern(f"World {world_no}, Zone", region_zones)
            if world_no == 1:
                _add_spareable_boss_locations(region_boss)
            prev.connect(region_zones, f"{prev.name} to {region_zones.name}")
            region_zones.connect(region_boss, f"{region_zones.name} to {region_boss.name}")
            prev = region_boss
        if world.options.pacifist_wins.value > 0:
            terrable = Region(f"[{kit.value.name}] Terrable", world.player, world.multiworld)
            world.multiworld.regions += [terrable]
            _add_locations_by_pattern("Terrable", terrable)
            terrable.add_event(f"[{kit.value.name}] Pacifist Victory", "Pacifist Victory", location_type=OSFELocation, item_type=OSFEItem)
            prev.connect(terrable, f"{prev.name} to {terrable.name}")
        if world.options.neutral_wins.value > 0:
            gate = Region(f"[{kit.value.name}] Eden Gate", world.player, world.multiworld)
            world.multiworld.regions += [gate]
            _add_locations_by_pattern("Gate", gate)
            gate.add_event(f"[{kit.value.name}] Neutral Victory", "Neutral Victory", location_type=OSFELocation, item_type=OSFEItem)
            prev.connect(gate, f"{prev.name} to {gate.name}")
        if world.options.genocide_wins.value > 0:
            eden = Region(f"[{kit.value.name}] Eden (genocide)", world.player, world.multiworld)
            serif = Region(f"[{kit.value.name}] Serif", world.player, world.multiworld)
            # For when real logic gets added, assume you need to be strong enough to beat the game to kill shopkeep
            shopkeep_kill = Region(f"[{kit.value.name}] Kill Shopkeeper", world.player, world.multiworld)
            world.multiworld.regions += [eden, serif, shopkeep_kill]
            _add_locations_by_pattern("Eden", eden)
            _add_locations_by_pattern("Serif", serif)
            serif.add_event(f"[{kit.value.name}] Genocide Victory", "Genocide Victory", location_type=OSFELocation, item_type=OSFEItem)
            _add_locations_by_pattern("Shopkeeper", shopkeep_kill)
            prev.connect(eden, f"{prev.name} to {eden.name}")
            eden.connect(serif, f"{eden.name} to {serif.name}")
            shopkeep_kill.connect(serif, f"{serif.name} to {shopkeep_kill.name}")
        # Pacifist and Neutral victories are always in logic, genocide is only expected if enabled in options
        if world.options.total_wins.value > 0 and world.options.pacifist_wins.value == 0:
            prev.add_event(f"[{kit.value.name}] Pacifist Victory", "Pacifist Victory", location_type=OSFELocation, item_type=OSFEItem)
        if world.options.total_wins.value > 0 and world.options.neutral_wins.value == 0:
            prev.add_event(f"[{kit.value.name}] Neutral Victory", "Neutral Victory", location_type=OSFELocation, item_type=OSFEItem)
