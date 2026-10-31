from dataclasses import dataclass
from enum import Enum

from worlds.osfe import Artifact
from .spells import Spell


@dataclass
class HeroKitData:
    name: str
    starting_spells: list[Spell]
    starting_artifacts: list[Artifact]
    damaging_weapon: bool

class HeroKit(Enum):
    Saffron = HeroKitData(
        "Saffron - Default",
        [Spell.Thunder, Spell.KineticWave, Spell.StepSlash, Spell.FrostBolt],
        [Artifact.SubTank],
        True)
    SaffronChrono = HeroKitData(
        "Saffron - Chrono",
        [Spell.MinnieGun, Spell.Whirl, Spell.StepSlash, Spell.Thunder],
        [Artifact.HeartOfTheCards],
        False)
    SaffronSolo = HeroKitData(
        "Saffron - Solo",
        [Spell.Ragnarok],
        [Artifact.SoulFood],
        True)
    Reva = HeroKitData(
        "Reva - Shield",
        [Spell.ShieldCatch, Spell.ShieldThrow, Spell.ShieldBeam, Spell.DiagBeam],
        [Artifact.Eschaton],
        False)
    # None of Reva - Beat's starting spells are damaging, so for the sake of logic her weapon is considered sufficient
    RevaBeat = HeroKitData(
        "Reva - Beat",
        [Spell.Pinch, Spell.SteelSkin, Spell.Corset, Spell.Zenith],
        [Artifact.FlakJacket],
        True)
    Gunner = HeroKitData(
        "Gunner - Manafire",
        [Spell.Innervate, Spell.BombToss, Spell.PekayFire, Spell.BlueBullets],
        [Artifact.CoverFire],
        True)
    GunnerBullethell = HeroKitData(
        "Gunner - Bullethell",
        [Spell.BombToss],
        [Artifact.CoverFire],
        True)
    Selicy = HeroKitData(
        "Selicy - Snow",
        [Spell.IceNeedle, Spell.ColdMedicine, Spell.FateShield, Spell.Zenith],
        [Artifact.Bulwark],
        True)
    SelicyInvade = HeroKitData(
        "Selicy - Invade",
        [Spell.Frostbite, Spell.ColdMedicine, Spell.Zenith, Spell.Crossfire],
        [Artifact.CoolShoes],
        True)
    Hazel = HeroKitData(
        "Hazel - Build",
        [Spell.MinnieGun, Spell.GunTurret, Spell.PushUp, Spell.KnockDown],
        [Artifact.HexBadge],
        False)
    HazelTeardown = HeroKitData(
        "Hazel - Teardown",
        [Spell.Pull, Spell.Wall, Spell.BlastCrystals, Spell.MinnieGun],
        [Artifact.Fragment],
        False)
    Terra = HeroKitData(
        "Terra - Break",
        [Spell.Entangle, Spell.Flurry, Spell.Excavate, Spell.PoisonTails],
        [Artifact.Moonstone],
        True)
    TerraPyro = HeroKitData(
        "Terra - Pyro",
        [Spell.SwordRow, Spell.Combust, Spell.Meditate, Spell.PekayFire],
        [Artifact.Citrine],
        True)
    Shiso = HeroKitData(
        "Shiso - Execute",
        [Spell.OrbitalBeam, Spell.StepSlash, Spell.Align, Spell.ClawTraps],
        [],
        True)
    ShisoKunai = HeroKitData(
        "Shiso - Kunai",
        [Spell.Kunai, Spell.CollectRing, Spell.Doubletake, Spell.ShadowShift],
        [Artifact.Acupuncture],
        True)
    Violette = HeroKitData(
        "Violette - Doubletime",
        [Spell.Corset, Spell.IronWill, Spell.Frostbite, Spell.ManaSteal],
        [Artifact.Feather],
        True)
    VioletteAria = HeroKitData(
        "Violette - Aria",
        [Spell.Skewer, Spell.Incline, Spell.SludgeBomb, Spell.SapphireRing],
        [Artifact.Vaccine],
        False)
    Shopkeeper = HeroKitData(
        "Shopkeeper - Money",
        [Spell.HiredGun, Spell.BowSnipe, Spell.CounterStrike, Spell.Swipe],
        [Artifact.Beret],
        True)

class SpareableBoss(Enum):
    Saffron = "Saffron"
    Reva = "Reva"
    Gunner = "Gunner"
    Selicy = "Selicy"
    Hazel = "Hazel"
    Terra = "Terra"
    Shiso = "Shiso"
    Violette = "Violette"

class SpareonlyBoss(Enum):
    Terrable = "Terrable"

class KillonlyBoss(Enum):
    Gate = "Gate"
    Serif = "Serif"
    Shopkeeper = "Shopkeeper"

# TODO: Enemies if enemysanity