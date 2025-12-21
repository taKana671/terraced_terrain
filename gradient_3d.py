import math


class Gradient3D:

    def __init__(self, max_length, gradient_size):
        self.max_length = max_length
        self.gradient_size = gradient_size

    def get_gradient(self, vert, center):
        norm = ((vert.x - center.x) ** 2 + (vert.y - center.y) ** 2 + (vert.z - center.z) ** 2) ** 0.5
        dist_to_center = norm / (2 ** 0.5 * self.max_length / self.gradient_size)

        if dist_to_center >= 1:
            return 1

        return 1 * dist_to_center


class GradientSphere(Gradient3D):

    def __init__(self, vert_value, bound, n_center, s_center, max_length=100, gradient_size=4):
        super().__init__(max_length, gradient_size)
        self.vert_value = vert_value
        self.bound = bound
        self.n_center = n_center
        self.s_center = s_center

    def get_center(self, vert):
        center = None

        match self.north_or_south(vert):
            case None:
                return center

            case 'n':
                center = self.n_center

            case 's':
                center = self.s_center

        return center


class GradientSphereNESW(GradientSphere):

    def __init__(self, vert_value, bound, n_center, s_center, max_length=100, gradient_size=4):
        super().__init__(vert_value, bound, n_center, s_center, max_length, gradient_size)

    def north_or_south(self, vert):
        # front
        if vert.x > -self.bound and \
                math.isclose(vert.y, self.vert_value, abs_tol=1e-5):
            return 'n'

        # right
        if math.isclose(vert.x, self.vert_value, abs_tol=1e-5) and \
                vert.y > -self.bound:
            return 'n'

        # top
        if vert.x > -self.bound and vert.y > -self.bound and \
                math.isclose(vert.z, self.vert_value, abs_tol=1e-5):
            return 'n'

        # back
        if vert.x < self.bound and \
                math.isclose(vert.y, -self.vert_value, abs_tol=1e-5):
            return 's'

        # left
        if math.isclose(vert.x, -self.vert_value, abs_tol=1e-5) and \
                vert.y < self.bound:
            return 's'

        # bottom
        if vert.x < self.bound and vert.y < self.bound and \
                math.isclose(vert.z, -self.vert_value, abs_tol=1e-5):
            return 's'

        return None


class GradientSphereNWSE(GradientSphere):

    def __init__(self, vert_value, bound, n_center, s_center, max_length=100, gradient_size=4):
        super().__init__(vert_value, bound, n_center, s_center, max_length, gradient_size)

    def north_or_south(self, vert):
        # front
        if vert.x < self.bound and \
                math.isclose(vert.y, self.vert_value, abs_tol=1e-5):
            return 'n'

        # left
        if math.isclose(vert.x, -self.vert_value, abs_tol=1e-5) and \
                vert.y > -self.bound:
            return 'n'

        # top
        if vert.x < self.bound and vert.y > -self.bound and \
                math.isclose(vert.z, self.vert_value, abs_tol=1e-5):
            return 'n'

        # back
        if vert.x > -self.bound and \
                math.isclose(vert.y, -self.vert_value, abs_tol=1e-5):
            return 's'

        # right
        if math.isclose(vert.x, self.vert_value, abs_tol=1e-5) and \
                vert.y < self.bound:
            return 's'

        # bottom
        if vert.x > -self.bound and vert.y < self.bound and \
                math.isclose(vert.z, -self.vert_value, abs_tol=1e-5):
            return 's'

        return None