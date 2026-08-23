from dataclasses import dataclass
from Options import Choice, Range, DefaultOnToggle, OptionSet, PerGameCommonOptions

from .data.beings import HeroKit


# TODO: Is a global system even worth entertaining? The location counts end up problematically small for many configs
#class LocationSystem(Choice):
#    """
#    Determine whether locations should be global or per-herokit. If per-herokit, each additional herokit will multiply
#    the total number of locations.
#    """
#    display_name = "Location System"
#    option_Global = 0
#    option_PerHero = 1
#    default = 0

class IncludedHeroKits(OptionSet):
    """
    Which HeroKits to shuffle into the pool as unlockable. Valid kits are:
      "Saffron"
      "Saffron - Chrono"
      "Saffron - Solo"
      "Reva"
      "Reva - Beat"
      "Gunner"
      "Gunner - Bullethell"
      "Selicy"
      "Selicy - Invade"
      "Hazel"
      "Hazel - Teardown"
      "Terra"
      "Terra - Pyro"
      "Shiso"
      "Shiso - Kunai"
      "Violette"
      "Violette - Aria"
      "Shopkeeper"
    """
    display_name = "Herokits"
    valid_keys = [char.value.name for char in HeroKit]
    default = ["Saffron", "Reva", "Gunner", "Selicy", "Hazel", "Terra", "Shiso", "Violette"]

class TotalHeroes(Range):
    """
    Choose how many hero kits to include in the multiworld. Note that each additional hero will multiply the
    number of locations in HeroZone mode. Reducing this number may necessitate spell and artifact unlock methods which
    reduce the total item count.
    """
    display_name = "Total Heroes"
    range_start = 1
    range_end = len(HeroKit)
    default = 3

class StarterHeroes(Range):
    """
    Choose how many hero kits should be unlocked at the start of the run.
    """
    display_name = "Starter Heroes"
    range_start = 1
    range_end = len(HeroKit)
    default = 1

class FullyUnlockStarterKit(DefaultOnToggle):
    """
    Unlock your starting herokit(s)' spells and artifacts at the start of the run. Recommended for casual runs and high
    starting hell pass levels.
    """
    display_name = "Fully Unlock Starter Kit"

class RandomizeStartingSpells(Choice):
    """
    Randomize all herokits(s)' starting spells. Currently only "true" randomization with minimal guard rails is
    supported, but a later version intends to support a more thematic randomization scheme
    """
#   """
#   Randomize all herokit(s)' starting spells. "Thematic" randomization preserves brand and approximate rarity of
#   spells, while "True" randomization can fill any spell slot with any spell. Note that if "Fully Unlock Starter Kit"
#   is disabled, these spells will need to be unlocked before becoming usable.
#   """
    display_name = "Randomize Starting Spells"
    option_Off = 0
    #option_Thematic = 1
    option_True = 2
    default = 0

class SpellUnlockMethod(Choice):
    """
    Choose if spell cards should be unlocked individually (254 items), by brand (10 items), or in thematic packs (32 items)
    Note that there are 254 spell cards, so the individual unlock method requires multiple additional heroes for enough
    locations to exist.
    """
    display_name = "Spell Unlock Method"
    option_Individual = 0
    option_Brand = 1
    option_Pack = 2
    default = 2

# TODO: themed artifact packs
#class ArtifactUnlockMethod(Choice):
#    """
#    Choose if artifacts should be unlocked individually or by thematic packs
#    """

class HellPassMode(Choice):
    """
    Determine which style of hell passes to use
    - Disabled: No hell passes will be used
    - Vanilla: Base game hell passes are enabled, based on the "Vanilla Hell Pass Level" option
    - Modded: Custom hell passes are enabled, which allow for more granular buffs/debuffs which vanilla hell passes do not support
    === Modded currently not implemented, and will fallback to vanilla ===
    """
    display_name = "Hell Pass Mode"
    option_Disabled = 0
    option_Vanilla = 1
    option_Modded = 2

class VanillaHellPassLevel(Range):
    """
    Select which level of vanilla hell pass to enable at the start of a run (all lower passes will also be enabled). Has
    no effect if HellPassMode is not set to Vanilla
    https://onestepfromeden.fandom.com/wiki/Hell_Pass
    """
    display_name = "Vanilla Hell Pass Level"
    range_start = 0
    range_end = 14
    default = 1

class HellPassDown(DefaultOnToggle):
    """
    Choose whether items should be shuffled into the multiworld which reduce the hell pass level when found. If this
    option is disabled, be prepared for a difficult run at high hell pass levels
    """
    display_name = "Hell Pass Down"

class RequiredCumulativeWins(Range):
    """
    Number of character wins of any ending required to goal. Each character can contribute up to 3 wins towards this
    total (one for each route). Has no effect if the required pacifist, neutral, or genocide wins are greater than this
    number.

    If RequiredGenocideWins is set to zero, logic will never require genocide victories to reach this total.
    """
    range_start = 0
    range_end = 3 * len(HeroKit)
    default = 1

class RequiredPacifistWins(Range):
    """
    Number of pacifist-ending character wins required to goal. Can be combined with any number of neutral or genocide wins.

    If at least one pacifist win is required, spare Terrable locations will be shuffled into the pool for each character.
    """
    range_start = 0
    range_end = len(HeroKit)
    default = 0

class RequiredNeutralWins(Range):
    """
    Number of neutral-ending character wins required to goal. Can be combined with any number of pacifist or genocide wins.

    If at least one neutral win is required, kill Wall locations will be shuffled into the pool for each character.
    """
    range_start = 0
    range_end = len(HeroKit)
    default = 0

class RequiredGenocideWins(Range):
    """
    Number of genocide-ending character wins required to goal. Can be combined with any number of pacifist or neutral wins.

    If at least one genocide win is required, Eden zone, kill Shopkeeper, and kill Serif locations will be shuffled into
    the pool for each character, and genocide victories will be included in logic for RequiredCumulativeWins.
    """
    range_start = 0
    range_end = len(HeroKit)
    default = 0

#class ShopSanity(DefaultOffToggle):
#    """
#    === NOT YET IMPLEMENTED ===
#    Shuffle multiworld items into shops
#    """
#    display_name = "ShopSanity"

#class DropSanity(DefaultOffToggle):
#    """
#    === NOT YET IMPLEMENTED ===
#    Shuffle multiworld items into item/artifact drops
#    """
#    display_name = "DropSanity"

@dataclass
class OSFEOptions(PerGameCommonOptions):
    included_herokits: IncludedHeroKits
    total_heroes: TotalHeroes
    start_heroes: StarterHeroes
    unlock_starter_kit: FullyUnlockStarterKit
    randomize_starting_spells: RandomizeStartingSpells
    spell_unlock_method: SpellUnlockMethod
    # TODO: artifact unlock method
    hellpass_mode: HellPassMode
    vanilla_hellpass_level: VanillaHellPassLevel
    hellpass_down: HellPassDown
    total_wins: RequiredCumulativeWins
    pacifist_wins: RequiredPacifistWins
    neutral_wins: RequiredNeutralWins
    genocide_wins: RequiredGenocideWins

# TODO: option groups