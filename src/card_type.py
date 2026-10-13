from enum import Enum

class SuperType(Enum):
    BASIC = "basic"
    LEGENDARY = "legendary"
    SNOW = "snow"
    WORLD = "world"

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

