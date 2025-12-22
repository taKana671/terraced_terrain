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


# class Mountain(Theme):

#     # sphere
#     LAYER_01_SPHERE = ([25, 47, 96, 255], 0.68)    # iron blue
#     LAYER_02_SPHERE = ([38, 73, 157, 255], 0.73)   # oriental blue
#     LAYER_03_SPHERE = ([111, 84, 54, 255], 0.75)   # burnt umber
#     LAYER_04_SPHERE = ([0, 51, 25, 255], 0.88)
#     LAYER_05_SPHERE = ([0, 102, 49, 255], 1.0)
#     LAYER_06_SPHERE = ([0, 133, 54, 255], None)

#     # flat
#     LAYER_01_FLAT = ([25, 47, 96, 255], 0.52)    # iron blue
#     LAYER_02_FLAT = ([38, 73, 157, 255], 0.6)   # oriental blue
#     LAYER_03_FLAT = ([111, 84, 54, 255], 0.63)  # burnt umber
#     LAYER_04_FLAT = ([0, 51, 25, 255], 0.76)
#     LAYER_05_FLAT = ([0, 102, 49, 255], 1.0)
#     LAYER_06_FLAT = ([0, 133, 54, 255], None)


# class Snow(Theme):

#     # sphere
#     # LAYER_01 = ([3, 51, 102, 255], 0.58)
#     # LAYER_02 = ([38, 73, 157, 255], 0.68)
#     # LAYER_03 = ([130, 205, 221, 255], 0.73)
#     # LAYER_04 = ([102, 102, 102, 255], 0.88)
#     # LAYER_05 = ([51, 51, 51, 255], 0.96)
#     # LAYER_06 = ([255, 255, 255, 255], None)

#     LAYER_01 = ([3, 51, 102, 255], 0.43)
#     LAYER_02 = ([38, 73, 157, 255], 0.5)
#     LAYER_03 = ([130, 205, 221, 255], 0.6)
#     LAYER_04 = ([102, 102, 102, 255], 0.78)
#     LAYER_05 = ([51, 51, 51, 255], 0.9)
#     LAYER_06 = ([255, 255, 255, 255], None)


# class Desert(Theme):

#     # LAYER_01 = ([237, 209, 142, 255], 0.52)
#     # LAYER_02 = ([237, 210, 143, 255], 0.62)
#     # LAYER_03 = ([250, 197, 89, 255], 0.78)
#     # LAYER_04 = ([153, 96, 49, 255], 0.88)
#     # LAYER_05 = ([108, 53, 36, 255], 1.0)
#     # LAYER_06 = ([51, 39, 16, 255], None)


#     LAYER_01 = ([237, 209, 142, 255], 0.45)
#     LAYER_02 = ([237, 210, 143, 255], 0.48)
#     LAYER_03 = ([250, 197, 89, 255], 0.58)
#     LAYER_04 = ([153, 96, 49, 255], 0.85)
#     LAYER_05 = ([108, 53, 36, 255], 1.1)
#     LAYER_06 = ([51, 39, 16, 255], None)



# class Island(Theme):
#     """
#     Island is only for flat terraced terrain at this time.
#     """

#     # LAYER_01 = ([0, 104, 183, 255], 0.5)
#     # LAYER_02 = ([255, 247, 153, 255], 0.65)
#     # LAYER_03 = ([128, 120, 92, 255], 0.72)
#     # LAYER_04 = ([0, 102, 46, 255], 0.9)
#     # LAYER_05 = ([0, 128, 57, 255], 1.46)
#     # LAYER_06 = ([0, 163, 88, 255], None)


#     LAYER_01 = ([0, 104, 183, 255], 0.0)
#     LAYER_02 = ([255, 247, 153, 255], 0.15)
#     LAYER_03 = ([128, 120, 92, 255], 0.22)
#     LAYER_04 = ([0, 102, 46, 255], 0.4)
#     LAYER_05 = ([0, 128, 57, 255], 0.96)
#     LAYER_06 = ([0, 163, 88, 255], None)

   