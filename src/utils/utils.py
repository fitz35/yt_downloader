import re
from typing import Optional


def validate_youtube_link(test_str: str) -> Optional[str]:
    # ex : https://www.youtube.com/watch?v=P98CcsPx8Hk&t=1s
    pattern = r'https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9]+)(?:&t=[0-9]+s)?'
    match = re.match(pattern, test_str)
    if match:
        return match.group(1)
    return None