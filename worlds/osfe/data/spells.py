from dataclasses import dataclass
from enum import Enum

@dataclass
class SpellData:
    name: str
    # TODO: track mana values to avoid relying on spells too expensive to cast
    is_damaging: bool  # Specifically, can this spell alone be used to kill enemies anywhere on the enemy grid

class Spell(Enum):
    # Anima
    Meltdown = SpellData("Meltdown", False)
    Firewall = SpellData("Firewall", True)
    Thunder = SpellData("Thunder", True)
    ColdMedicine = SpellData("Cold Medicine", True)
    PekayFire = SpellData("Pekay Fire", True)
    FrostBarrage = SpellData("Frost Barrage", True)
    FrostBolt = SpellData("Frost Bolt", True)
    MiniThunder = SpellData("Mini Thunder", True)
    Thunderstorm = SpellData("Thunderstorm", True)
    IceSpikes = SpellData("Ice Spikes", True)
    ColdSnap = SpellData("Cold Snap", True)
    BackBurner = SpellData("Back Burner", True)
    Twinferno = SpellData("Twinferno", True)
    Combust = SpellData("Combust", False)
    Frostbite = SpellData("Frostbite", True)
    Ember = SpellData("Ember", True)
    Cryokinesis = SpellData("Cryokinesis", True)
    Salamander = SpellData("Salamander", False)
    RingOfFire = SpellData("Ring of Fire", True)
    Brushfire = SpellData("Brushfire", False)
    Wildfire = SpellData("Wildfire", True)
    Hailstorm = SpellData("Hailstorm", True)
    IceHockey = SpellData("Ice Hockey", True)
    Rage = SpellData("Rage", True)
    Pyroblast = SpellData("Pyroblast", True)
    CarpetBomb = SpellData("Carpet Bomb", True)
    IceNeedle = SpellData("Ice Needle", True)
    Firestorm = SpellData("Firestorm", True)
    Sunder = SpellData("Sunder", False)
    Blizzard = SpellData("Blizzard", True)
    Flamberge = SpellData("Flamberge", True)
    Fimbulveter = SpellData("Fimbulveter", True)
    Explosion = SpellData("EXPLOSION!", True)

    # Convergence
    ManaPotion = SpellData("Mana Potion", False)
    ManaSteal = SpellData("Mana Steal", True)
    Boomerang = SpellData("Boomerang", True)
    HiredGun = SpellData("Hired Gun", True)
    TriShot = SpellData("Tri Shot", True)
    Meditate = SpellData("Meditate", False)
    Focus = SpellData("Focus", False)
    TriRag = SpellData("Tri Rag", True)
    Whirl = SpellData("Whirl", False)
    Sequencer = SpellData("Sequencer", True)
    Incline = SpellData("Incline", True)
    Amalgam = SpellData("Amalgam", True)
    ManaFusion = SpellData("Mana Fusion", False)
    SapphireRing = SpellData("Sapphire Ring", True)
    Ping = SpellData("Ping", True)
    LimitBreak = SpellData("Limit Break", True)
    Innervate = SpellData("Innervate", False)
    EmpowerRing = SpellData("Empower Ring", True)
    ChargeRing = SpellData("Charge Ring", True)
    TriForce = SpellData("Tri Force", False)
    SeraCannon = SpellData("Sera Cannon", True)
    Overload = SpellData("Overload", False)
    PowerSaws = SpellData("Power Saws", True)

    # Doublelift
    Ramjet = SpellData("Ramjet", True)
    Sleight = SpellData("Sleight", False)
    Skewer = SpellData("Skewer", True)
    AmbientBurst = SpellData("Ambient Burst", True)
    JamSlam = SpellData("Jam Slam", False)
    DeckSlam = SpellData("Deck Slam", False) # TODO: Does this do zero damage in 1-card decks?
    Cataclysm = SpellData("Cataclysm", False)
    Railgun = SpellData("Railgun", True)
    JamCannon = SpellData("Jam Cannon", False)
    TimeSlow = SpellData("Time Slow", False)
    Switchbait = SpellData("Switchbait", False)
    Viruspell = SpellData("Viruspell", True)
    Fling = SpellData("Fling", False)
    Echo = SpellData("Echo", False)
    Gambit = SpellData("Gambit", False) # That would be cruel
    Unleash = SpellData("Unleash", True)
    Sustain = SpellData("Sustain", False)
    TimeStop = SpellData("TimeStop", False)
    Preload = SpellData("Preload", True)
    Trisect = SpellData("Trisect", True)
    ChronoSphere = SpellData("Chrono Sphere", True)
    Wonder = SpellData("Wonder", True)
    Salvo = SpellData("Salvo", True)
    Midnight = SpellData("Midnight", False)

    # Glimmer
    Crossfire = SpellData("Crossfire", False)
    Shattersaw = SpellData("Shattersaw", True)
    ZigZag = SpellData("ZigZag", True)
    Paragon = SpellData("Paragon", True)
    SoulFire = SpellData("Soul Fire", True)
    Breakout = SpellData("Breakout", False)
    DiagBeam = SpellData("Diag Beam", True)
    Energizer = SpellData("Energizer", True)
    Zenith = SpellData("Zenith", False)
    Glaive = SpellData("Glaive", True)
    Shine = SpellData("Shine", True)
    Circuit = SpellData("Circuit", False)
    SolarCharge = SpellData("Solar Charge", True)
    EternityCannon = SpellData("Eternity Cannon", True)
    InfinityBeam = SpellData("Infinity Beam", True)
    SpiritSword = SpellData("Spirit Sword", True)
    Glitterbomb = SpellData("Glitterbomb", True)
    Glitterstorm = SpellData("Glitterstorm", True)
    Sunshine = SpellData("Sunshine", False) # Consume
    Sawstorm = SpellData("Sawstorm", True)

    # Hearth
    SwordRow = SpellData("Sword Row", True)
    EarthenArmor = SpellData("Earth Armor", False)
    RockCycle = SpellData("Rock Cycle", True)
    IonCannon = SpellData("Ion Cannon", True)
    TileFire = SpellData("Tile Fire", True)
    Tremor = SpellData("Tremor", True)
    Coldstone = SpellData("Coldstone", True)
    Fracture = SpellData("Fracture", True)
    OrbitalBeam = SpellData("Orbital Beam", True)
    Entangle = SpellData("Entangle", True)
    Barrier = SpellData("Barrier", False)
    Wreath = SpellData("Wreath", False)
    Missiletoe = SpellData("Missiletoe", True)
    EarthPrayer = SpellData("Earth Prayer", False)
    FlatEarth = SpellData("Flat Earth", False)
    Fissure = SpellData("Fissure", True)
    FlintShot = SpellData("Flint Shot", False) # No flow can lead to 0 damage
    EarthWyrm = SpellData("Earth Wyrm", False)
    Excavate = SpellData("Excavate", False)
    Waterfall = SpellData("Waterfall", False)
    Prophecy = SpellData("Prophecy", True)
    SwordsOfLight = SpellData("Swords of Light", True)
    RockTomb = SpellData("Rock Tomb", True)
    Jackhammer = SpellData("Jackhammer", False)
    Ambush = SpellData("Ambush", True)
    WeedWacker = SpellData("Weed Wacker", True)
    HolyGround = SpellData("Holy Ground", True)

    # Hexawan
    Minefield = SpellData("Minefield", True)
    Shotgun = SpellData("Shotgun", False)
    MinnieGun = SpellData("Minnie Gun", True)
    Volley = SpellData("Volley", False)
    ShardToss = SpellData("Shard Toss", True)
    GunTurret = SpellData("Gun Turret", True)
    Sunbeamer = SpellData("Sunbeamer", True)
    Bombard = SpellData("Bombard", False)
    Shieldgen = SpellData("Shieldgen", False)
    BombToss = SpellData("Bomb Toss", True)
    BlueBullets = SpellData("Blue Bullets", True)
    ManaLattice = SpellData("Mana Lattice", False)
    Beacon = SpellData("Beacon", True)
    Sweeper = SpellData("Sweeper", True)
    Wall = SpellData("Wall", False)
    Salvage = SpellData("Salvage", False)
    BeamCrystals = SpellData("Beam Crystals", True)
    BlastCrystals = SpellData("Blast Crystals", True)
    TurretSD = SpellData("Turret SD", False)
    Mine = SpellData("Mine", True)
    LaserTurret = SpellData("Laser Turret", True)
    Resonate = SpellData("Resonate", False)
    CrossTurret = SpellData("Cross Turret", True)
    Sidewinder = SpellData("Sidewinder", False)
    Monument = SpellData("Monument", False)
    Castle = SpellData("Castle", True)
    SuperMinnieGun = SpellData("Super Minnie Gun", True)
    Grail = SpellData("Grail", False)
    Silo = SpellData("Silo", True)

    # Kinesys
    Undertow = SpellData("Undertow", False)
    River = SpellData("River", True)
    KineticWave = SpellData("Kinetic Wave", True)
    AirSlash = SpellData("Air Slash", True)
    Upwind = SpellData("Upwind", True)
    Align = SpellData("Align", False)
    TractorBeam = SpellData("Tractor Beam", True)
    Flurry = SpellData("Flurry", False)
    Pull = SpellData("Pull", False)
    SpikeStrip = SpellData("Spike Strip", False)
    Caltrops = SpellData("Caltrops", False)
    Fadeaway = SpellData("Fadeaway", True)
    KnockDown = SpellData("Knock Down", True)
    Wobble = SpellData("Wobble", False)
    PushUp = SpellData("Push Up", True)
    ClawTraps = SpellData("Claw Traps", False)
    WarpRays = SpellData("Warp Rays", True)
    Blink = SpellData("Blink", False)
    BowSnipe = SpellData("Bow Snipe", True)
    Skipper = SpellData("Skipper", True)
    Northwind = SpellData("Northwind", True)
    Tsunami = SpellData("Tsunami", False)
    Inverter = SpellData("Inverter", True)
    HyperBeam = SpellData("Hyper Beam", True)
    Monsoon = SpellData("Monsoon", True)

    # Miseri
    Glassify = SpellData("Glassify", False)
    Anubis = SpellData("Anubis", True)
    Revenge = SpellData("Revenge", True)
    PoisonDart = SpellData("Poison Dart", True)
    BoosterShot = SpellData("Booster Shot", True)
    PoisonTails = SpellData("Poison Tails", False)
    SoulLink = SpellData("Soul Link", False)
    Pinch = SpellData("Pinch", False)
    Twoxin = SpellData("Twoxin", True)
    Detox = SpellData("Detox", False)
    Showdown = SpellData("Showdown", False)
    Rest = SpellData("Rest", False)
    Leech = SpellData("Leech", False)
    SludgeBomb = SpellData("Sludge Bomb", True)
    Backstab = SpellData("Backstab", True)
    Transfuse = SpellData("Transfuse", False)
    AcidRain = SpellData("Acid Rain", True)
    Smog = SpellData("Smog", True)
    Pandemic = SpellData("Pandemic", False)
    Corset = SpellData("Corset", False)
    Devour = SpellData("Devour", False)
    HealthPotion = SpellData("Health Potion", False)
    Venoshock = SpellData("Venoshock", False)
    DoubleTap = SpellData("Double Tap", True)
    Hellfire = SpellData("Hellfire", True)
    BloodShield = SpellData("Blood Shield", False)
    Cynet = SpellData("Cynet", False)

    # Phalanx
    Absorb = SpellData("Absorb", True)
    JamShield = SpellData("Jam Shield", False)
    Haven = SpellData("Haven", False)
    DeckShield = SpellData("Deck Shield", False)
    ShieldCatch = SpellData("Shield Catch", False)
    ShieldsUp = SpellData("Shields Up", False)
    FateShield = SpellData("Fate Shield", False)
    CounterStrike = SpellData("Counter Strike", True)
    ShieldThrow = SpellData("Shield Throw", False)
    Reflector = SpellData("Reflector", False)
    ShieldBeam = SpellData("Shield Beam", True)
    Entrench = SpellData("Entrench", False)
    MissMeShield = SpellData("Miss-Me Shield", False)
    SteelSkin = SpellData("Steel Skin", False)
    IronWill = SpellData("Iron Will", False)
    Forte = SpellData("Forte", False)
    DiamondRing = SpellData("Diamond Ring", True)
    SpellShield = SpellData("Spell Shield", False)
    BlessingOfSusanoo = SpellData("Blessing of Susano'o", False) # Consume
    IceShield = SpellData("Ice Shield", False)
    Stasis = SpellData("Stasis", False)
    Downfall = SpellData("Downfall", False)
    Stinger = SpellData("Stinger", False)

    # Slashfik
    Kunai = SpellData("Kunai", False)
    Slice = SpellData("Slice", False)
    Doubletake = SpellData("Doubletake", True)
    MagicClaw = SpellData("Magic Claw", True)
    Swipe = SpellData("Swipe", True)
    ShadowShift = SpellData("Shadow Shift", True)
    StepPierce = SpellData("Step Pierce", True)
    Knife = SpellData("Knife", True)
    BouncingBlade = SpellData("Bouncing Blade", True)
    StepSlash = SpellData("Step Slash", True)
    BladeBay = SpellData("Blade Bay", True)
    BladeRain = SpellData("Blade Rain", True)
    LastLetter = SpellData("Last Letter", False)
    CollectRing = SpellData("Collect Ring", True)
    Vivisection = SpellData("Vivisection", True)
    Blackout = SpellData("Blackout", True)
    Ragnarok = SpellData("Ragnarok", True)
    Guillotine = SpellData("Guillotine", True)
    Lifesword = SpellData("Lifesword", False)
    Excalibur = SpellData("Excalibur", True)
    Fury = SpellData("Fury", False) # Consume
    Scavenge = SpellData("Scavenge", False)
    Warpath = SpellData("Warpath", True)
    Bladeskrieg = SpellData("Bladeskrieg", True)

class SpellBrand(Enum):
    Anima = [
        Spell.Meltdown,
        Spell.Firewall,
        Spell.Thunder,
        Spell.ColdMedicine,
        Spell.PekayFire,
        Spell.FrostBarrage,
        Spell.FrostBolt,
        Spell.MiniThunder,
        Spell.Thunderstorm,
        Spell.IceSpikes,
        Spell.ColdSnap,
        Spell.BackBurner,
        Spell.Twinferno,
        Spell.Combust,
        Spell.Frostbite,
        Spell.Ember,
        Spell.Cryokinesis,
        Spell.Salamander,
        Spell.RingOfFire,
        Spell.Brushfire,
        Spell.Wildfire,
        Spell.Hailstorm,
        Spell.IceHockey,
        Spell.Rage,
        Spell.Pyroblast,
        Spell.CarpetBomb,
        Spell.IceNeedle,
        Spell.Firestorm,
        Spell.Sunder,
        Spell.Blizzard,
        Spell.Flamberge,
        Spell.Fimbulveter,
        Spell.Explosion,
    ]
    Convergence = [
        Spell.ManaPotion,
        Spell.ManaSteal,
        Spell.Boomerang,
        Spell.HiredGun,
        Spell.TriShot,
        Spell.Meditate,
        Spell.Focus,
        Spell.TriRag,
        Spell.Whirl,
        Spell.Sequencer,
        Spell.Incline,
        Spell.Amalgam,
        Spell.ManaFusion,
        Spell.SapphireRing,
        Spell.Ping,
        Spell.LimitBreak,
        Spell.Innervate,
        Spell.EmpowerRing,
        Spell.ChargeRing,
        Spell.TriForce,
        Spell.SeraCannon,
        Spell.Overload,
        Spell.PowerSaws,

    ]
    Doublelift = [
        Spell.Ramjet,
        Spell.Sleight,
        Spell.Skewer,
        Spell.AmbientBurst,
        Spell.JamSlam,
        Spell.DeckSlam,
        Spell.Cataclysm,
        Spell.Railgun,
        Spell.JamCannon,
        Spell.TimeSlow,
        Spell.Switchbait,
        Spell.Viruspell,
        Spell.Fling,
        Spell.Echo,
        Spell.Gambit,
        Spell.Unleash,
        Spell.Sustain,
        Spell.TimeStop,
        Spell.Preload,
        Spell.Trisect,
        Spell.ChronoSphere,
        Spell.Wonder,
        Spell.Salvo,
        Spell.Midnight,
    ]
    Glimmer = [
        Spell.Crossfire,
        Spell.Shattersaw,
        Spell.ZigZag,
        Spell.Paragon,
        Spell.SoulFire,
        Spell.Breakout,
        Spell.DiagBeam,
        Spell.Energizer,
        Spell.Zenith,
        Spell.Glaive,
        Spell.Shine,
        Spell.Circuit,
        Spell.SolarCharge,
        Spell.EternityCannon,
        Spell.InfinityBeam,
        Spell.SpiritSword,
        Spell.Glitterbomb,
        Spell.Glitterstorm,
        Spell.Sunshine,
        Spell.Sawstorm,
    ]
    Hearth = [
        Spell.SwordRow,
        Spell.EarthenArmor,
        Spell.RockCycle,
        Spell.IonCannon,
        Spell.TileFire,
        Spell.Tremor,
        Spell.Coldstone,
        Spell.Fracture,
        Spell.OrbitalBeam,
        Spell.Entangle,
        Spell.Barrier,
        Spell.Wreath,
        Spell.Missiletoe,
        Spell.EarthPrayer,
        Spell.FlatEarth,
        Spell.Fissure,
        Spell.FlintShot,
        Spell.EarthWyrm,
        Spell.Excavate,
        Spell.Waterfall,
        Spell.Prophecy,
        Spell.SwordsOfLight,
        Spell.RockTomb,
        Spell.Jackhammer,
        Spell.Ambush,
        Spell.WeedWacker,
        Spell.HolyGround,
    ]
    Hexawan = [
        Spell.Minefield,
        Spell.Shotgun,
        Spell.MinnieGun,
        Spell.Volley,
        Spell.ShardToss,
        Spell.GunTurret,
        Spell.Sunbeamer,
        Spell.Bombard,
        Spell.Shieldgen,
        Spell.BombToss,
        Spell.BlueBullets,
        Spell.ManaLattice,
        Spell.Beacon,
        Spell.Sweeper,
        Spell.Wall,
        Spell.Salvage,
        Spell.BeamCrystals,
        Spell.BlastCrystals,
        Spell.TurretSD,
        Spell.Mine,
        Spell.LaserTurret,
        Spell.Resonate,
        Spell.CrossTurret,
        Spell.Sidewinder,
        Spell.Monument,
        Spell.Castle,
        Spell.SuperMinnieGun,
        Spell.Grail,
        Spell.Silo,
    ]
    Kinesys = [
        Spell.Undertow,
        Spell.River,
        Spell.KineticWave,
        Spell.AirSlash,
        Spell.Upwind,
        Spell.Align,
        Spell.TractorBeam,
        Spell.Flurry,
        Spell.Pull,
        Spell.SpikeStrip,
        Spell.Caltrops,
        Spell.Fadeaway,
        Spell.KnockDown,
        Spell.Wobble,
        Spell.PushUp,
        Spell.ClawTraps,
        Spell.WarpRays,
        Spell.Blink,
        Spell.BowSnipe,
        Spell.Skipper,
        Spell.Northwind,
        Spell.Tsunami,
        Spell.Inverter,
        Spell.HyperBeam,
        Spell.Monsoon,
    ]
    Miseri = [
        Spell.Glassify,
        Spell.Anubis,
        Spell.Revenge,
        Spell.PoisonDart,
        Spell.BoosterShot,
        Spell.PoisonTails,
        Spell.SoulLink,
        Spell.Pinch,
        Spell.Twoxin,
        Spell.Detox,
        Spell.Showdown,
        Spell.Rest,
        Spell.Leech,
        Spell.SludgeBomb,
        Spell.Backstab,
        Spell.Transfuse,
        Spell.AcidRain,
        Spell.Smog,
        Spell.Pandemic,
        Spell.Corset,
        Spell.Devour,
        Spell.HealthPotion,
        Spell.Venoshock,
        Spell.DoubleTap,
        Spell.Hellfire,
        Spell.BloodShield,
        Spell.Cynet,
    ]
    Phalanx = [
        Spell.Absorb,
        Spell.JamShield,
        Spell.Haven,
        Spell.DeckShield,
        Spell.ShieldCatch,
        Spell.ShieldsUp,
        Spell.FateShield,
        Spell.CounterStrike,
        Spell.ShieldThrow,
        Spell.Reflector,
        Spell.ShieldBeam,
        Spell.Entrench,
        Spell.MissMeShield,
        Spell.SteelSkin,
        Spell.IronWill,
        Spell.Forte,
        Spell.DiamondRing,
        Spell.SpellShield,
        Spell.BlessingOfSusanoo,
        Spell.IceShield,
        Spell.Stasis,
        Spell.Downfall,
        Spell.Stinger,
    ]
    Slashfik = [
        Spell.Kunai,
        Spell.Slice,
        Spell.Doubletake,
        Spell.MagicClaw,
        Spell.Swipe,
        Spell.ShadowShift,
        Spell.StepPierce,
        Spell.Knife,
        Spell.BouncingBlade,
        Spell.StepSlash,
        Spell.BladeBay,
        Spell.BladeRain,
        Spell.LastLetter,
        Spell.CollectRing,
        Spell.Vivisection,
        Spell.Blackout,
        Spell.Ragnarok,
        Spell.Guillotine,
        Spell.Lifesword,
        Spell.Excalibur,
        Spell.Fury,
        Spell.Scavenge,
        Spell.Warpath,
        Spell.Bladeskrieg,
    ]

# Thematic packs used for the pack-based SpellUnlockMethod option
class SpellPack(Enum):
    AoE = [
        Spell.Explosion,
        Spell.Pyroblast,
        Spell.Shotgun,
        Spell.Twinferno,
    ]
    Beam = [
        Spell.HyperBeam,
        Spell.InfinityBeam,
        Spell.ShieldBeam,
        Spell.TractorBeam,
    ]
    Blade = [
        Spell.BouncingBlade,
        Spell.Blackout,
        Spell.BladeRain,
        Spell.Bladeskrieg,
        Spell.Excalibur,
        Spell.Kunai,
        Spell.Lifesword,
        Spell.SpiritSword,
        Spell.Vivisection,
    ]
    Chrono = [
        Spell.TimeSlow,
        Spell.TimeStop,
        Spell.ChronoSphere,
    ]
    Crack = [
        Spell.Ambush,
        Spell.Cataclysm,
        Spell.EarthWyrm,
        Spell.Excavate,
        Spell.Fissure,
        Spell.FlatEarth,
        Spell.HolyGround,
        Spell.IonCannon,
        Spell.Jackhammer,
        Spell.OrbitalBeam,
        Spell.Prophecy,
        Spell.Ramjet,
        Spell.TileFire,
    ]
    BigDeck = [
        Spell.DeckShield,
        Spell.DeckSlam,
        Spell.Gambit,
        Spell.Midnight,
    ]
    Bouncy = [
        Spell.DiagBeam,
        Spell.IceHockey,
        Spell.ZigZag,
    ]
    Flame = [
        Spell.BackBurner,
        Spell.Brushfire,
        Spell.CarpetBomb,
        Spell.Combust,
        Spell.Ember,
        Spell.Firestorm,
        Spell.Firewall,
        Spell.Flamberge,
        Spell.PekayFire,
        Spell.Rage,
        Spell.RingOfFire,
        Spell.Salamander,
        Spell.Wildfire,
    ]
    Fling = [
        Spell.Echo,
        Spell.Fling,
        Spell.SpellShield,
        Spell.Switchbait,
    ]
    Flow = [
        Spell.Barrier,
        Spell.Coldstone,
        Spell.EarthPrayer,
        Spell.EarthenArmor,
        Spell.EternityCannon,
        Spell.FlintShot,
        Spell.Fracture,
        Spell.KineticWave,
        Spell.River,
        Spell.RockCycle,
        Spell.RockTomb,
        Spell.Tremor,
        Spell.Tsunami,
        Spell.Undertow,
        Spell.Waterfall,
    ]
    Fragile = [
        Spell.Entrench,
        Spell.Glassify,
        Spell.IceShield,
        Spell.Knife,
        Spell.LimitBreak,
        Spell.MagicClaw,
        Spell.Showdown,
    ]
    Frost = [
        Spell.Blizzard,
        Spell.ColdMedicine,
        Spell.ColdSnap,
        Spell.Cryokinesis,
        Spell.Fimbulveter,
        Spell.FrostBarrage,
        Spell.Frostbite,
        Spell.FrostBolt,
        Spell.Hailstorm,
        Spell.IceNeedle,
        Spell.IceSpikes,
        Spell.Meltdown,
        Spell.Sunder,
    ]
    Health = [
        Spell.Cynet,
        Spell.Devour,
        Spell.HealthPotion,
        Spell.Leech,
        Spell.Pinch,
        Spell.Rest,
        Spell.Revenge,
        Spell.SoulLink,
    ]
    Indirect = [
        Spell.Glitterbomb,
        Spell.Glitterstorm,
        Spell.Guillotine,
        Spell.Hellfire,
        Spell.LastLetter,
        Spell.MiniThunder,
        Spell.Paragon,
        Spell.Ragnarok,
        Spell.Shine,
        Spell.Thunder,
        Spell.Thunderstorm,
        Spell.Whirl,
    ]
    Invade = [
        Spell.Breakout,
        Spell.Circuit,
        Spell.Crossfire,
        Spell.Fury,
        Spell.StepPierce,
        Spell.StepSlash,
        Spell.Warpath,
        Spell.Zenith,
    ]
    Jam = [
        Spell.Innervate,
        Spell.JamCannon,
        Spell.JamShield,
        Spell.JamSlam,
        Spell.Railgun,
        Spell.Salvo,
        Spell.Skewer,
    ]
    Kunai = [
        Spell.CounterStrike,
        Spell.Doubletake,
        Spell.Scavenge,
        Spell.ShadowShift,
        Spell.Swipe,
    ]
    Mana = [
        Spell.BlueBullets,
        Spell.Boomerang,
        Spell.Focus,
        Spell.ManaFusion,
        Spell.ManaPotion,
        Spell.Overload,
        Spell.Transfuse,
        Spell.Unleash,
    ]
    Mine = [
        Spell.BombToss,
        Spell.Caltrops,
        Spell.Mine,
        Spell.Minefield,
        Spell.SpikeStrip,
        Spell.Sweeper,
    ]
    Poison = [
        Spell.AcidRain,
        Spell.Anubis,
        Spell.Backstab,
        Spell.BloodShield,
        Spell.BoosterShot,
        Spell.Detox,
        Spell.Pandemic,
        Spell.PoisonDart,
        Spell.PoisonTails,
        Spell.Slice,
        Spell.SludgeBomb,
        Spell.Smog,
        Spell.Twoxin,
        Spell.Venoshock,
    ]
    Projectile = [
        Spell.Amalgam,
        Spell.BowSnipe,
        Spell.DoubleTap,
        Spell.HiredGun,
        Spell.Incline,
        Spell.Ping,
        Spell.Skipper,
        Spell.SuperMinnieGun,
    ]
    Relocation = [
        Spell.AirSlash,
        Spell.Align,
        Spell.Fadeaway,
        Spell.Flurry,
        Spell.Inverter,
        Spell.KnockDown,
        Spell.Monsoon,
        Spell.Northwind,
        Spell.Pull,
        Spell.PushUp,
        Spell.Upwind,
        Spell.WarpRays,
        Spell.Wobble,
    ]
    Ring = [
        Spell.ChargeRing,
        Spell.CollectRing,
        Spell.DiamondRing,
        Spell.EmpowerRing,
        Spell.SapphireRing,
    ]
    Root = [
        Spell.ClawTraps,
        Spell.Entangle,
        Spell.Missiletoe,
        Spell.SwordRow,
        Spell.SwordsOfLight,
        Spell.WeedWacker,
        Spell.Wreath,
    ]
    Sawblade = [
        Spell.Glaive,
        Spell.PowerSaws,
        Spell.Sawstorm,
        Spell.Shattersaw,
    ]
    Scaling = [
        Spell.AmbientBurst,
        Spell.Energizer,
        Spell.SeraCannon,
        Spell.SoulFire,
        Spell.Viruspell,
    ]
    Shield = [
        Spell.Absorb,
        Spell.BlessingOfSusanoo,
        Spell.Blink,
        Spell.Corset,
        Spell.Downfall,
        Spell.FateShield,
        Spell.Forte,
        Spell.Haven,
        Spell.IronWill,
        Spell.MissMeShield,
        Spell.Reflector,
        Spell.ShieldCatch,
        Spell.ShieldsUp,
        Spell.ShieldThrow,
        Spell.Stasis,
        Spell.SteelSkin,
        Spell.Stinger,
    ]
    Shuffle = [
        Spell.BladeBay,
        Spell.Preload,
        Spell.Sleight,
    ]
    Solar = [
        Spell.SolarCharge,
        Spell.Sunshine,
        Spell.Sunbeamer,
    ]
    Summon = [
        Spell.Beacon,
        Spell.BeamCrystals,
        Spell.BlastCrystals,
        Spell.Bombard,
        Spell.Castle,
        Spell.CrossTurret,
        Spell.Grail,
        Spell.GunTurret,
        Spell.LaserTurret,
        Spell.ManaLattice,
        Spell.Monument,
        Spell.Resonate,
        Spell.Salvage,
        Spell.ShardToss,
        Spell.Shieldgen,
        Spell.Sidewinder,
        Spell.Silo,
        Spell.TurretSD,
        Spell.Volley,
        Spell.Wall
    ]
    Trinity = [
        Spell.ManaSteal,
        Spell.Meditate,
        Spell.MinnieGun,
        Spell.Sequencer,
        Spell.Sustain,
        Spell.TriForce,
        Spell.TriRag,
        Spell.TriShot,
        Spell.Trisect,
    ]
    Wonder = [
        Spell.Wonder,
    ]