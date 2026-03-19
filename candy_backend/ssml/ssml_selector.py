from datetime import datetime, time
from .ssml_presets import SSML_PRESETS

def is_night():
    now = datetime.now().time()
    return now >= time(23,0) or now <= time(5,0)

def select_ssml_preset(emotion, intensity):
    if is_night():
        return SSML_PRESETS["night"]
    return SSML_PRESETS.get(emotion, SSML_PRESETS["calm"])
