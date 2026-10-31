from dataclasses import dataclass
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from Options import OptionError
from .data.consts import ALL_RARITIES
from .data.artifacts import Artifact, ArtifactRarities
from .data.spells import Spell, SpellBrand
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
        for rarity in ALL_RARITIES:
            _append_item(f"Brand Rarity Unlock: {rarity} {brand.name}", ItemClassification.progression)
    for i in range(1, 15):
        _append_item(f"Hell Pass {i} Relief", ItemClassification.progression)
    for artifact in Artifact:
        _append_item(f"Artifact Unlock: {artifact.value.name}", ItemClassification.useful)
    for art_rarity in ArtifactRarities:
        _append_item(f"Artifact Rarity Unlock: {art_rarity.name}", ItemClassification.progression if art_rarity.name == "Basic" else ItemClassification.useful)
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
        case world.options.spell_unlock_method.option_Brand_Rarity:
            for brand in SpellBrand:
                for rarity in ALL_RARITIES:
                    items.append(world.create_item(f"Brand Rarity Unlock: {rarity} {brand.name}"))

    match world.options.artifact_unlock_method:
        case world.options.artifact_unlock_method.option_Individual:
            for artifact in Artifact:
                items.append(world.create_item(f"Artifact Unlock: {artifact.value.name}"))
        case world.options.artifact_unlock_method.option_Rarity:
            for art_rarity in ArtifactRarities:
                items.append(world.create_item(f"Artifact Rarity Unlock: {art_rarity.name}"))

    if world.options.starter_basic_artifacts == world.options.starter_basic_artifacts.option_true:
        precollect_arts: list[str] = []
        match world.options.artifact_unlock_method:
            case world.options.artifact_unlock_method.option_Individual:
                precollect_arts.append(f"Artifact Unlock: {Artifact.ManaGem.value.name}")
                precollect_arts.append(f"Artifact Unlock: {Artifact.ManaVein.value.name}")
                precollect_arts.append(f"Artifact Unlock: {Artifact.Medkit.value.name}")
            case world.options.artifact_unlock_method.option_Rarity:
                precollect_arts.append(f"Artifact Rarity Unlock: {ArtifactRarities.Base.name}")
        for art in precollect_arts:
            world.push_precollected(world.create_item(art))
        items = list(filter(lambda i: i.name not in precollect_arts, items))

    if world.options.unlock_starter_kit.value == world.options.unlock_starter_kit.option_true:
        precollect_items: list[str] = []
        for kit in world.start_characters:
            for spell in kit.value.starting_spells:
                item_str = f"Spell Card: {spell.value.name}"
                precollect_items.append(item_str)
                world.push_precollected(world.create_item(item_str))
            for art in kit.value.starting_artifacts:
                item_str = f"Artifact Unlock: {art.value.name}"
                precollect_items.append(item_str)
                world.push_precollected(world.create_item(item_str))
        items = list(filter(lambda i: i.name not in precollect_items, items))

    match world.options.hellpass_mode.value:
        case world.options.hellpass_mode.option_Disabled:
            pass
        case world.options.hellpass_mode.option_Vanilla | world.options.hellpass_mode.option_Modded:
            # Until custom hell passes are implemented, fall back to vanilla
            if world.options.hellpass_relief.value == world.options.hellpass_relief.option_true:
                items += [world.create_item(f"Hell Pass {i} Relief") for i in world.options.vanilla_hellpasses_enabled.value]

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
