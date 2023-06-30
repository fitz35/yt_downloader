import enum
import json
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
    
def save_list_of_videos(videos : list[VideoMetadata], file_path : str) :
    """
    save a list of videos metadata
    """
    with open(file_path, "w") as file:
        json.dump([video.to_dict() for video in videos], file, cls=EnumEncoder, indent=4)

def load_list_of_video(file_path : str) -> list[VideoMetadata]:
    """
    load a list of person
    """
    with open(file_path, "r") as file:
        json_str = file.read()
        if json_str == "":
            return []
        return [VideoMetadata.from_dict(data) for data in json.loads(json_str, object_hook=as_enum)]
    

# ----------- enum serialization ----------------------
# https://stackoverflow.com/questions/24481852/serialising-an-enum-member-to-json/24482806#24482806


ENUM_SERIALIZABLE = {
    "ImportanceLevel" : ImportanceLevel
}

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, enum.Enum):
            return {"__enum__": str(obj)}
        return json.JSONEncoder.default(self, obj)

def as_enum(d):
    if "__enum__" in d:
        # dynamically get the enum
        name, member = d["__enum__"].split(".")
        enum_class = ENUM_SERIALIZABLE[name]
        return enum_class[member]
    else:
        return d

