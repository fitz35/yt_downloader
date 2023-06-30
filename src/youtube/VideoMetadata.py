import enum
from dataclasses import dataclass

class ImportanceLevel(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class VideoMetadata:
    uuid : str
    resolution : int
    importance_level : ImportanceLevel
    already_download : bool = False

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dict : dict):
        dict["importance_level"] = ImportanceLevel(dict["importance_level"])
        return cls(**dict)
    


