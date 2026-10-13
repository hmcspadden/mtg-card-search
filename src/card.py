from enum import Enum

class SuperType(Enum):
    BASIC = "basic"
    LEGENDARY = "legendary"
    SNOW = "snow"
    WORLD = "world"


class ManaPips(Enum):
    W = "W"
    U = "U"
    B = "B"
    R = "R"
    G = "G"
    

class ManaCost():
    def __init__(
        self,
        generic_mana: int | None = None,
        mana_pips: 
    ):


class TypeLine():
    def __init__(
        self,
        primary_type: str,
        permanent: bool,
        super_type: SuperType | None = None,
        secondary_type: str | None = None,
        subtypes: list[str] | None = None,
    ):
        self.primary_type = primary_type
        self.permanent = permanent
        self.super_type = super_type
        self.secondary_type = secondary_type
        self.subtypes = subtypes




class Card():
    def __init__(
        self,
        name: str,
        type_line: TypeLine,

    ):