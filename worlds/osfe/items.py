from dataclasses import dataclass
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from Options import OptionError
from .data.artifacts import Artifact
from .data.spells import Spell, SpellBrand, SpellPack
from . import HeroKit

if TYPE_CHECKING:
    from . import OSFEWorld


class OSFEItem(Item):
    game = "One Step From Eden"

@dataclass
class ItemData:
    classification: ItemClassification

def _propagate_item_table() -> tuple[dict[str, int], dict[str, ItemData]]:
    item_id: int = 1
    _item_str_to_id: dict[str, int] = {}
    _item_str_to_data: dict[str, ItemData] = {}

    def _append_item(item: str, classification: ItemClassification) -> None:
        nonlocal item_id
        _item_str_to_id[item] = item_id
        _item_str_to_data[item] = ItemData(classification)
        item_id += 1

    for kit in HeroKit:
        _append_item(f"Hero Unlock: {kit.value.name}", ItemClassification.progression)
    for spell in Spell:
        _append_item(f"Spell Card: {spell.value.name}", ItemClassification.progression)
    for brand in SpellBrand:
        _append_item(f"Brand Unlock: {brand.name}", ItemClassification.progression)
    for pack in SpellPack:
        _append_item(f"Spell Booster Pack: {pack.name}", ItemClassification.progression)
    _append_item("Hell Pass Down", ItemClassification.progression)
    for artifact in Artifact:
        _append_item(f"Artifact Unlock: {artifact.name}", ItemClassification.useful)
    _append_item("Filler", ItemClassification.filler) # TODO: better filler

    return _item_str_to_id, _item_str_to_data

def create_all_items(world: "OSFEWorld") -> None:
    items: list[OSFEItem] = []

    for kit in world.characters:
        if kit in world.start_characters:
            world.push_precollected(world.create_item(f"Hero Unlock: {kit.value.name}"))
        else:
            items.append(world.create_item(f"Hero Unlock: {kit.value.name}"))

    match world.options.spell_unlock_method.value:
        case world.options.spell_unlock_method.option_Individual:
            for spell in Spell:
                items.append(world.create_item(f"Spell Card: {spell.value.name}"))
        case world.options.spell_unlock_method.option_Brand:
            for brand in SpellBrand:
                items.append(world.create_item(f"Brand Unlock: {brand.name}"))
        case world.options.spell_unlock_method.option_Pack:
            for pack in SpellPack:
                items.append(world.create_item(f"Spell Booster Pack: {pack.name}"))

    if world.options.unlock_starter_kit.value == world.options.unlock_starter_kit.option_true:
        precollect_spells: list[str] = []
        for kit in world.start_characters:
            for spell in kit.value.starting_spells:
                item_str = f"Spell Card: {spell.value.name}"
                precollect_spells.append(item_str)
                world.push_precollected(world.create_item(item_str))
        items = list(filter(lambda i: i.name not in precollect_spells, items))

    match world.options.hellpass_mode.value:
        case world.options.hellpass_mode.option_Disabled:
            pass
        case world.options.hellpass_mode.option_Vanilla | world.options.hellpass_mode.option_Modded:
            # Until custom hell passes are implemented, fall back to vanilla
            if world.options.hellpass_down.value == world.options.hellpass_down.option_true:
                items += [world.create_item(f"Hell Pass Down") for _ in range(world.options.vanilla_hellpass_level.value)]

    item_slots = len(world.multiworld.get_unfilled_locations(world.player))
    if len(items) > item_slots:
        raise OptionError(f"YAML config generates more items ({len(items)}) than locations ({item_slots}). Either enable more characters or generate fewer items.")

    # TODO: useful filler
    filler_slots = item_slots - len(items)
    items += [world.create_item(world.get_filler_item_name()) for _ in range(filler_slots)]

    world.multiworld.itempool += items

def create_item(world: "OSFEWorld", name: str) -> OSFEItem:
    return OSFEItem(name, item_str_to_data[name].classification, item_str_to_id[name], world.player)

def get_filler(world: "OSFEWorld") -> str:
    return "Filler"

item_str_to_id, item_str_to_data = _propagate_item_table()
