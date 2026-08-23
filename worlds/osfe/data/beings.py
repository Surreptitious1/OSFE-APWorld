from dataclasses import dataclass
from enum import Enum

from .spells import Spell


@dataclass
class HeroKitData:
    name: str
    starting_spells: list[Spell]
    damaging_weapon: bool

class HeroKit(Enum):
    Saffron = HeroKitData("Saffron", [Spell.Thunder, Spell.KineticWave, Spell.StepSlash, Spell.FrostBolt], True)
    SaffronChrono = HeroKitData("Saffron - Chrono", [Spell.MinnieGun, Spell.Whirl, Spell.StepSlash, Spell.Thunder], False)
    SaffronSolo = HeroKitData("Saffron - Solo", [Spell.Ragnarok], True)
    Reva = HeroKitData("Reva", [Spell.ShieldCatch, Spell.ShieldThrow, Spell.ShieldBeam, Spell.DiagBeam], False)
    # None of Reva - Beat's starting spells are damaging, so for the sake of logic her weapon is considered sufficient
    RevaBeat = HeroKitData("Reva - Beat", [Spell.Pinch, Spell.SteelSkin, Spell.Corset, Spell.Zenith], True)
    Gunner = HeroKitData("Gunner", [Spell.Innervate, Spell.BombToss, Spell.PekayFire, Spell.BlueBullets], True)
    GunnerBullethell = HeroKitData("Gunner - Bullethell", [Spell.BombToss], True)
    Selicy = HeroKitData("Selicy", [Spell.IceNeedle, Spell.ColdMedicine, Spell.FateShield, Spell.Zenith], True)
    SelicyInvade = HeroKitData("Selicy - Invade", [Spell.Frostbite, Spell.ColdMedicine, Spell.Zenith, Spell.Crossfire], True)
    Hazel = HeroKitData("Hazel", [Spell.MinnieGun, Spell.GunTurret, Spell.PushUp, Spell.KnockDown], False)
    HazelTeardown = HeroKitData("Hazel - Teardown", [Spell.Pull, Spell.Wall, Spell.BlastCrystals, Spell.MinnieGun], False)
    Terra = HeroKitData("Terra", [Spell.Entangle, Spell.Flurry, Spell.Excavate, Spell.PoisonTails], True)
    TerraPyro = HeroKitData("Terra - Pyro", [Spell.SwordRow, Spell.Combust, Spell.Meditate, Spell.PekayFire], True)
    Shiso = HeroKitData("Shiso", [Spell.OrbitalBeam, Spell.StepSlash, Spell.Align, Spell.ClawTraps], True)
    ShisoKunai = HeroKitData("Shiso - Kunai", [Spell.Kunai, Spell.CollectRing, Spell.Doubletake, Spell.ShadowShift], True)
    Violette = HeroKitData("Violette", [Spell.Corset, Spell.IronWill, Spell.Frostbite, Spell.ManaSteal], True)
    VioletteAria = HeroKitData("Violette - Aria", [Spell.Skewer, Spell.Incline, Spell.SludgeBomb, Spell.SapphireRing], False)
    Shopkeeper = HeroKitData("Shopkeeper", [Spell.HiredGun, Spell.BowSnipe, Spell.CounterStrike, Spell.Swipe], True)

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

# TODO: Enemies for enemysanity