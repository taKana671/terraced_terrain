from enum import Enum


themes_sphere = {}
themes_flat = {}


class Theme(Enum):

    def __init__(self, rgba, threshold):
        self.rgba = [round(v / 255, 2) for v in rgba]
        self.threshold = threshold

    def __init_subclass__(cls):
        super().__init_subclass__()
        if 'flat_themes' in cls.__module__:
            themes_flat[cls.__name__.lower()] = cls
        elif 'sphere_themes' in cls.__module__:
            themes_sphere[cls.__name__.lower()] = cls

    @classmethod
    def color(cls, z):
        if z <= cls.LAYER_01.threshold:
            return cls.LAYER_01.rgba
        if z <= cls.LAYER_02.threshold:
            return cls.LAYER_02.rgba
        if z <= cls.LAYER_03.threshold:
            return cls.LAYER_03.rgba
        if z <= cls.LAYER_04.threshold:
            return cls.LAYER_04.rgba
        if z <= cls.LAYER_05.threshold:
            return cls.LAYER_05.rgba

        return cls.LAYER_06.rgba