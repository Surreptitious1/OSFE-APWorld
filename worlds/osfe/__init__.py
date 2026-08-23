from typing import Any

from BaseClasses import MultiWorld
from Options import OptionError
from worlds.AutoWorld import World
from .data.beings import HeroKit
from .data.spells import Spell
from . import items, locations, regions, rules # TODO: web_world
from . import options as osfe_options

class OSFEWorld(World):
    """One Step From Eden is roguelike Mega Man Battle Network"""
    game = "One Step From Eden"

    #web = web_world

    options_dataclass = osfe_options.OSFEOptions
    options: osfe_options.OSFEOptions

    location_name_to_id = locations.location_str_to_id
    item_name_to_id = items.item_str_to_id

    origin_region_name = "Menu"

    def __init__(self, mw: MultiWorld, player: int):
        super().__init__(mw, player)
        self.characters: list[HeroKit] = []
        self.start_characters: list[HeroKit] = []

    def generate_early(self) -> None:
        self._pick_characters()
        self._randomize_kits()
        self._validate_wincon()

    def _pick_characters(self) -> None:
        char_strs = sorted(self.options.included_herokits)
        char_pool: list[HeroKit] = [kit for kit in HeroKit if kit.value.name in char_strs]
        if len(char_pool) == 0:
            raise OptionError("At least one hero kit must be specified")
        if len(char_pool) != len(set(char_pool)):
            raise OptionError(f"Duplicate hero kit specified")
        if len(char_pool) < self.options.total_heroes.value:
            raise OptionError(f"Not enough hero kits provided ({len(char_pool)}) for the number requested {self.options.total_heroes.value}")
        if self.options.start_heroes.value > self.options.total_heroes.value:
            raise OptionError("Starter heroes exceeds total heroes")
        self.characters = self.random.sample(char_pool, self.options.total_heroes.value)
        self.start_characters = self.random.sample(self.characters, self.options.start_heroes.value)
        print(f"Selected characters {self.characters}; starting {self.start_characters}")

    def _randomize_kits(self) -> None:
        if self.options.randomize_starting_spells:
            spell_pool = [spell for spell in Spell]
            for char in self.characters:
                new_spells: list[Spell] = self.random.sample(spell_pool, len(char.value.starting_spells))
                # If the character's weapon can't kill, keep rerolling until we get at least one spell that can
                while (not char.value.damaging_weapon) and (sum(spell.value.is_damaging for spell in new_spells) == 0):
                    new_spells: list[Spell] = self.random.sample(spell_pool, len(char.value.starting_spells))
                char.value.starting_spells = new_spells

    def _validate_wincon(self) -> None:
        opt = self.options
        if (opt.pacifist_wins.value == 0 and
            opt.genocide_wins.value == 0 and
            opt.neutral_wins.value == 0 and
            opt.total_wins.value == 0):
            raise OptionError("No win condition specified")

        if opt.total_wins.value > 2 * opt.total_heroes and opt.genocide_wins.value == 0:
            raise OptionError(f"Required cumulative wins ({opt.total_wins.value}) exceeds possible pacifist and neutral wins ({opt.total_heroes * 2})")
        if opt.total_wins.value > 3 * opt.total_heroes and opt.genocide_wins.value == 1:
            raise OptionError(f"Required cumulative wins ({opt.total_wins.value}) exceeds possible unique wins ({opt.total_heroes * 3})")
        if opt.pacifist_wins.value > opt.total_heroes:
            raise OptionError(f"Required pacifist wins ({opt.pacifist_wins.value}) exceeds character count ({opt.total_heroes})")
        if opt.neutral_wins.value > opt.total_heroes:
            raise OptionError(f"Required neutral wins ({opt.neutral_wins.value}) exceeds character count ({opt.total_heroes})")
        if opt.genocide_wins.value > opt.total_heroes:
            raise OptionError(f"Required genocide wins ({opt.genocide_wins.value}) exceeds character count ({opt.total_heroes})")

    def create_regions(self) -> None:
        regions.create_regions_and_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.OSFEItem:
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_filler(self)

    def fill_slot_data(self) -> dict[str, Any]:
        data = self.options.as_dict(
            "hellpass_mode", "vanilla_hellpass_level", "total_wins",
            "pacifist_wins", "neutral_wins", "genocide_wins"
        )
        data['characters'] = []
        for kit in self.characters:
            data['characters'].append(kit.value.name)
            data[f"{kit.value.name}_starting_spells"] = [spell.value.name for spell in kit.value.starting_spells]
        return data