"""Definition of the supported bulb effects."""

from typing import Dict, Iterable, List, cast

from pywizlight.bulblibrary import BulbClass

SCENES = {
    1: "Ocean",
    2: "Romance",
    3: "Sunset",
    4: "Party",
    5: "Fireplace",
    6: "Cozy",
    7: "Forest",
    8: "Pastel colors",
    9: "Wake-up",
    10: "Bedtime",
    11: "Warm white",
    12: "Daylight",
    13: "Cool white",
    14: "Night light",
    15: "Focus",
    16: "Relax",
    17: "True colors",
    18: "TV time",
    19: "Plant growth",
    20: "Spring",
    21: "Summer",
    22: "Fall",
    23: "Deep dive",
    24: "Jungle",
    25: "Mojito",
    26: "Club",
    27: "Christmas",
    28: "Halloween",
    29: "Candlelight",
    30: "Golden white",
    31: "Pulse",
    32: "Steampunk",
    33: "Diwali",
    34: "White",
    35: "Alarm",
    1000: "Rhythm",
}
SCENE_NAME_TO_ID = {scene_name: scene_id for (scene_id, scene_name) in SCENES.items()}
TW_SCENES = [6, 9, 10, 11, 12, 13, 14, 29, 31, 32, 34, 35]
DW_SCENES = [9, 10, 14, 29, 31, 32, 34, 35]

SCENES_BY_CLASS: Dict[BulbClass, List[str]] = {
    BulbClass.RGB: list(cast(Iterable, SCENES.values())),
    BulbClass.TW: [SCENES[key] for key in TW_SCENES],
    BulbClass.DW: [SCENES[key] for key in DW_SCENES],
}


def get_id_from_scene_name(scene: str) -> int:
    """Return the id of an given scene name.

    :param scene: Name of the scene
    :raises ValueError: Return if not in scene list
    :return: ID of the scene
    """
    scene_id = SCENE_NAME_TO_ID.get(scene)
    if not scene_id:
        raise ValueError(f"Scene '{scene}' not in scene list.")
    return scene_id
