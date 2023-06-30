import enum
import json
import re
from typing import Optional

from youtube.VideoMetadata import ImportanceLevel, VideoMetadata


def validate_youtube_link(test_str: str) -> Optional[str]:
    # ex : https://www.youtube.com/watch?v=P98CcsPx8Hk&t=1s
    pattern = r'https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9]+)(?:&t=[0-9]+s)?'
    match = re.match(pattern, test_str)
    if match:
        return match.group(1)
    return None

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
