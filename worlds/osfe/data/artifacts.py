from dataclasses import dataclass
from enum import Enum

@dataclass
class ArtifactData:
    name: str
    is_damaging: bool

class Artifact(Enum):
    # Base
    ManaGem = ArtifactData("Mana Gem", False)
    ManaVein = ArtifactData("Mana Vein", False)
    Medkit = ArtifactData("Medkit", False)

    # Common
    AdaptiveArmor = ArtifactData("Adaptive Armor", False)
    Anvil = ArtifactData("Anvil", False)
    BlazeOfGlory = ArtifactData("Blaze Of Glory", False)
    BlueBlood = ArtifactData("Blue Blood", False)
    BoltAction = ArtifactData("Bolt Action", False)
    Bubble = ArtifactData("Bubble", False)
    CensorBar = ArtifactData("Censor Bar", False)
    ChocoMintChip = ArtifactData("Choco Mint Chip", False)
    Citrine = ArtifactData("Citrine", False)
    Cryophage = ArtifactData("Cryophage", False)
    Curacao = ArtifactData("Curacao", False)
    Delta = ArtifactData("Delta", False)
    EmptyBottle = ArtifactData("Empty Bottle", False)
    ExplosiveTendons = ArtifactData("Explosive Tendons", False)
    GlassCannon = ArtifactData("Glass Cannon", False)
    Harpoon = ArtifactData("Harpoon", False)
    HeartOfTheCards = ArtifactData("Heart of the Cards", False)
    HitSeeker = ArtifactData("Hit Seeker", False)
    IceFloe = ArtifactData("Ice Floe", False)
    IceSculpture = ArtifactData("Ice Sculpture", False)
    Kabob = ArtifactData("Kabob", False)
    KnifeBelt = ArtifactData("Knife Belt", False)
    LifeJacket = ArtifactData("Life Jacket", False)
    Manajam = ArtifactData("Manajam", False)
    MicroMissiles = ArtifactData("Micro Missiles", False)
    MintTea = ArtifactData("Mint Tea", False)
    Monocle = ArtifactData("Monocle", False)
    Moonstone = ArtifactData("Moonstone", False)
    Multitool = ArtifactData("Multitool", False)
    MuzzleBrake = ArtifactData("Muzzle Brake", False)
    NerveGas = ArtifactData("Nerve Gas", False)
    Pendulum = ArtifactData("Pendulum", False)
    Pinwheel = ArtifactData("Pinwheel", False)
    PoisonVial = ArtifactData("Poison Vial", False)
    Riffle = ArtifactData("Riffle", False)
    RockTumbler = ArtifactData("Rock Tumbler", False)
    Scales = ArtifactData("Scales", False)
    SecondBreakfast = ArtifactData("Second Breakfast", False)
    Sinkhole = ArtifactData("Sinkhole", False)
    SnowBoots = ArtifactData("Snow Boots", False)
    SpikeProtein = ArtifactData("Spike Protein", False)
    Stoplight = ArtifactData("Stoplight", False)
    SugarGlass = ArtifactData("Sugar Glass", False)
    SurvivalKit = ArtifactData("Survival Kit", False)
    Symbiosis = ArtifactData("Symbiosis", False)
    Tessellate = ArtifactData("Tessellate", False)
    Thermophage = ArtifactData("Thermophage", False)
    Thornmail = ArtifactData("Thornmail", False)
    ThreeDPrinter = ArtifactData("3D Printer", True)
    Trident = ArtifactData("Trident", False)
    Tutu = ArtifactData("Tutu", False)
    Umbrella = ArtifactData("Umbrella", False)
    ViralTransmitter = ArtifactData("Viral Transmitter", False)
    WaterWheel = ArtifactData("Water Wheel", False)
    XD40 = ArtifactData("XD-40", False)

    # Rare
    Acupuncture = ArtifactData("Acupuncture", False)
    Adamantium = ArtifactData("Adamantium", False)
    Adrenaline = ArtifactData("Adrenaline", False)
    Amethyst = ArtifactData("Amethyst", False)
    Bandage = ArtifactData("Bandage", False)
    Beaker = ArtifactData("Beaker", False)
    Bismuth = ArtifactData("Bismuth", False)
    BlueberryJam = ArtifactData("Blueberry Jam", False)
    BlueFlame = ArtifactData("Blue Flame", False)
    Bulwark = ArtifactData("Bulwark", False)
    CandyWrapper = ArtifactData("Candy Wrapper", False)
    CardThrower = ArtifactData("Card Thrower", False)
    CassidyScarf = ArtifactData("Cassidy's Scarf", False)
    Champagne = ArtifactData("Glass Flute", False)
    ChaosFrag = ArtifactData("Chaos Fragment", False)
    CobraCare = ArtifactData("Cobra Care", False)
    ColdBlooded = ArtifactData("Cold Blooded", False)
    CreditCard = ArtifactData("Credit Card", False)
    DoubleEdge = ArtifactData("Double Edge", False)
    DuctTape = ArtifactData("Duct Tape", False)
    Feather = ArtifactData("Feather", False)
    Flechette = ArtifactData("Flechette", False)
    Gelatin = ArtifactData("Gelatin", False)
    GoldenCat = ArtifactData("Golden Cat", False)
    Granite = ArtifactData("Granite", False)
    GunnerFrontAll = ArtifactData("M1 Liofire", False)
    GunnerHoming = ArtifactData("M2 Hunter Seeker", False)
    HardenedShields = ArtifactData("Hardened Shields", False)
    HoningSteel = ArtifactData("Honing Steel", False)
    KineticShield = ArtifactData("Kinetic Shields", False)
    LaserPointer = ArtifactData("Laser Pointer", False)
    LuckBox = ArtifactData("Luck Box", False)
    MagnifyingGlass = ArtifactData("Magnifying Glass", False)
    MiningRig = ArtifactData("Mining Rig", False)
    Mitosis = ArtifactData("Mitosis", False)
    PantherHabit = ArtifactData("Panther Habit", False)
    PaperWallet = ArtifactData("Paper Wallet", False)
    PiggyBank = ArtifactData("Piggy Bank", False)
    PowerShard = ArtifactData("Power Shard", False)
    ResistantStrain = ArtifactData("Resistant Strain", False)
    Rose = ArtifactData("Rose", False)
    ShieldBattery = ArtifactData("Shield Battery", False)
    Static = ArtifactData("Static", False)
    Stimpack = ArtifactData("Stimpack", False)
    Sunglasses = ArtifactData("Sunglasses", False)
    Transmission = ArtifactData("Transmission", False)
    Undershirt = ArtifactData("Undershirt", False)
    Vaccine = ArtifactData("Vaccine", False)
    Violet = ArtifactData("Violet", False)
    ZCell = ArtifactData("Z-Cell", False)

    # Epic
    Aether = ArtifactData("Aether", False)
    Anthrax = ArtifactData("Anthrax", False)
    BloodMoney = ArtifactData("Blood Money", False)
    Chalice = ArtifactData("Chalice", False)
    ColdPressedJuice = ArtifactData("Cold Pressed Juice", False)
    CoverFire = ArtifactData("Cover Fire", False)
    Daffodil = ArtifactData("Daffodil", False)
    Elysium = ArtifactData("Elysium", False)
    FlakJacket = ArtifactData("Flak Jacket", False)
    FlashLoader = ArtifactData("Flash Loader", False)
    Fragment = ArtifactData("Fragment", False)
    GhostCostume = ArtifactData("Ghost Costume", False)
    GiantArmor = ArtifactData("Giant Armor", False)
    Goldfish = ArtifactData("Goldfish", False)
    GripTape = ArtifactData("Grip Tape", False)
    HexBadge = ArtifactData("Hex Badge", False)
    Icing = ArtifactData("Icing", False)
    ImmuneSystem = ArtifactData("Immune System", False)
    Lily = ArtifactData("Lily", False)
    LinkCable = ArtifactData("Link Cable", False)
    LongSleeves = ArtifactData("Long Sleeves", False)
    LuckyCoin = ArtifactData("Lucky Coin", False)
    Luna = ArtifactData("Luna", False)
    Masonjar = ArtifactData("Masonjar", False)
    MeatShield = ArtifactData("Meat Shield", False)
    Miracle = ArtifactData("Miracle", False)
    MoltenCore = ArtifactData("Molten Core", False)
    PetFox = ArtifactData("Pet Fox", False)
    PetPuppy = ArtifactData("Pet Puppy", False)
    PetSoulGun = ArtifactData("Soul Gun", True)
    PetTurtle = ArtifactData("Pet Turtle", False)
    PocketSand = ArtifactData("Pocket Sand", False)
    PocketWatch = ArtifactData("Pocket Watch", False)
    RemoveOne = ArtifactData("Remove One", False)
    RescueBadge = ArtifactData("Rescue Badge", False)
    RollerBlades = ArtifactData("Roller Blades", False)
    Ruby = ArtifactData("Ruby", False)
    SaigonArmor = ArtifactData("Saigon Armor", False)
    Satellite = ArtifactData("Satellite", False)
    ShadowToxin = ArtifactData("Shadow Toxin", False)
    SoulFood = ArtifactData("Soul Food", False)
    SpeedLoader = ArtifactData("Speed Loader", False)
    SpellthiefLicense = ArtifactData("Spellthief License", False)
    StepDrone = ArtifactData("Step Drone", True)
    Thermite = ArtifactData("Thermite", False)
    Trifrost = ArtifactData("Trifrost", False)
    Trinket = ArtifactData("Tri-nket", False)
    UpgradeOne = ArtifactData("Upgrade One", False)
    Uranium = ArtifactData("Uranium", False)
    Virtue = ArtifactData("Virtue", False)

    # Legendary
    BazsWhip = ArtifactData("Baz's Whip", False)
    Beret = ArtifactData("Beret", False)
    CoolShoes = ArtifactData("Cool Shoes", False)
    DartFrog = ArtifactData("Dart Frog", False)
    DoubleMint = ArtifactData("Double Mint", False)
    DuelDisk = ArtifactData("Duel Disk", False)
    Eschaton = ArtifactData("Eschaton", False)
    FreezerBurn = ArtifactData("Freezer Burn", False)
    Frostmail = ArtifactData("Frostmail", False)
    HeartOfGold = ArtifactData("Heart of Gold", False)
    Lilac = ArtifactData("Lilac", False)
    MeritBadge = ArtifactData("Merit Badge", False)
    Mirror = ArtifactData("Mirror", False)
    Mjolnir = ArtifactData("Mjolnir", False)
    Mother = ArtifactData("Mother", False)
    Ninjutsu = ArtifactData("Ninjutsu", False)
    PetDragon = ArtifactData("Pet Dragon", False)
    PetKitty = ArtifactData("Pet Kitty", False)
    PetLiger = ArtifactData("Pet Liger", False)
    PhasePlates = ArtifactData("Phase Plates", False)
    SubTank = ArtifactData("Second Soul", False)
    Thorn = ArtifactData("Thorn", False)
    TightPants = ArtifactData("Tight Pants", False)
    Tinder = ArtifactData("Tinder", False)
    Transcendence = ArtifactData("Transcendence", False)
    TrapCard = ArtifactData("Trap Card", True) # Only slightly evil
    UnicornBomb = ArtifactData("Unicorn Bomb", False)
    VGunMod = ArtifactData("VGun", False)
    Wings = ArtifactData("Wings", False)

class ArtifactRarities(Enum):
    Base = [
        Artifact.ManaGem,
        Artifact.ManaVein,
        Artifact.Medkit,
    ],
    Common = [
        Artifact.AdaptiveArmor,
        Artifact.Anvil,
        Artifact.BlazeOfGlory,
        Artifact.BlueBlood,
        Artifact.BoltAction,
        Artifact.Bubble,
        Artifact.CensorBar,
        Artifact.ChocoMintChip,
        Artifact.Citrine,
        Artifact.Cryophage,
        Artifact.Curacao,
        Artifact.Delta,
        Artifact.EmptyBottle,
        Artifact.ExplosiveTendons,
        Artifact.GlassCannon,
        Artifact.Harpoon,
        Artifact.HeartOfTheCards,
        Artifact.HitSeeker,
        Artifact.IceFloe,
        Artifact.IceSculpture,
        Artifact.Kabob,
        Artifact.KnifeBelt,
        Artifact.LifeJacket,
        Artifact.Manajam,
        Artifact.MicroMissiles,
        Artifact.MintTea,
        Artifact.Monocle,
        Artifact.Moonstone,
        Artifact.Multitool,
        Artifact.MuzzleBrake,
        Artifact.NerveGas,
        Artifact.Pendulum,
        Artifact.Pinwheel,
        Artifact.PoisonVial,
        Artifact.Riffle,
        Artifact.RockTumbler,
        Artifact.Scales,
        Artifact.SecondBreakfast,
        Artifact.Sinkhole,
        Artifact.SnowBoots,
        Artifact.SpikeProtein,
        Artifact.Stoplight,
        Artifact.SugarGlass,
        Artifact.SurvivalKit,
        Artifact.Symbiosis,
        Artifact.Tessellate,
        Artifact.Thermophage,
        Artifact.Thornmail,
        Artifact.ThreeDPrinter,
        Artifact.Trident,
        Artifact.Tutu,
        Artifact.Umbrella,
        Artifact.ViralTransmitter,
        Artifact.WaterWheel,
        Artifact.XD40,
    ]
    Rare = [
        Artifact.Acupuncture,
        Artifact.Adamantium,
        Artifact.Adrenaline,
        Artifact.Amethyst,
        Artifact.Bandage,
        Artifact.Beaker,
        Artifact.Bismuth,
        Artifact.BlueberryJam,
        Artifact.BlueFlame,
        Artifact.Bulwark,
        Artifact.CandyWrapper,
        Artifact.CardThrower,
        Artifact.CassidyScarf,
        Artifact.Champagne,
        Artifact.ChaosFrag,
        Artifact.CobraCare,
        Artifact.ColdBlooded,
        Artifact.CreditCard,
        Artifact.DoubleEdge,
        Artifact.DuctTape,
        Artifact.Feather,
        Artifact.Flechette,
        Artifact.Gelatin,
        Artifact.GoldenCat,
        Artifact.Granite,
        Artifact.GunnerFrontAll,
        Artifact.GunnerHoming,
        Artifact.HardenedShields,
        Artifact.HoningSteel,
        Artifact.KineticShield,
        Artifact.LaserPointer,
        Artifact.LuckBox,
        Artifact.MagnifyingGlass,
        Artifact.MiningRig,
        Artifact.Mitosis,
        Artifact.PantherHabit,
        Artifact.PaperWallet,
        Artifact.PiggyBank,
        Artifact.PowerShard,
        Artifact.ResistantStrain,
        Artifact.Rose,
        Artifact.ShieldBattery,
        Artifact.Static,
        Artifact.Stimpack,
        Artifact.Sunglasses,
        Artifact.Transmission,
        Artifact.Undershirt,
        Artifact.Vaccine,
        Artifact.Violet,
        Artifact.ZCell,
    ]
    Epic = [
        Artifact.Aether,
        Artifact.Anthrax,
        Artifact.BloodMoney,
        Artifact.Chalice,
        Artifact.ColdPressedJuice,
        Artifact.CoverFire,
        Artifact.Daffodil,
        Artifact.Elysium,
        Artifact.FlakJacket,
        Artifact.FlashLoader,
        Artifact.Fragment,
        Artifact.GhostCostume,
        Artifact.GiantArmor,
        Artifact.Goldfish,
        Artifact.GripTape,
        Artifact.HexBadge,
        Artifact.Icing,
        Artifact.ImmuneSystem,
        Artifact.Lily,
        Artifact.LinkCable,
        Artifact.LongSleeves,
        Artifact.LuckyCoin,
        Artifact.Luna,
        Artifact.Masonjar,
        Artifact.MeatShield,
        Artifact.Miracle,
        Artifact.MoltenCore,
        Artifact.PetFox,
        Artifact.PetPuppy,
        Artifact.PetSoulGun,
        Artifact.PetTurtle,
        Artifact.PocketSand,
        Artifact.PocketWatch,
        Artifact.RemoveOne,
        Artifact.RescueBadge,
        Artifact.RollerBlades,
        Artifact.Ruby,
        Artifact.SaigonArmor,
        Artifact.Satellite,
        Artifact.ShadowToxin,
        Artifact.SoulFood,
        Artifact.SpeedLoader,
        Artifact.SpellthiefLicense,
        Artifact.StepDrone,
        Artifact.Thermite,
        Artifact.Trifrost,
        Artifact.Trinket,
        Artifact.UpgradeOne,
        Artifact.Uranium,
        Artifact.Virtue,
    ]
    Legendary = [
        Artifact.BazsWhip,
        Artifact.Beret,
        Artifact.CoolShoes,
        Artifact.DartFrog,
        Artifact.DoubleMint,
        Artifact.DuelDisk,
        Artifact.Eschaton,
        Artifact.FreezerBurn,
        Artifact.Frostmail,
        Artifact.HeartOfGold,
        Artifact.Lilac,
        Artifact.MeritBadge,
        Artifact.Mirror,
        Artifact.Mjolnir,
        Artifact.Mother,
        Artifact.Ninjutsu,
        Artifact.PetDragon,
        Artifact.PetKitty,
        Artifact.PetLiger,
        Artifact.PhasePlates,
        Artifact.SubTank,
        Artifact.Thorn,
        Artifact.TightPants,
        Artifact.Tinder,
        Artifact.Transcendence,
        Artifact.TrapCard,
        Artifact.UnicornBomb,
        Artifact.VGunMod,
        Artifact.Wings,
    ]