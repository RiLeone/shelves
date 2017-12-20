#!/usr/bin/env python3

"""
    Beam Nodes Class
    ----------------
        For the computation of interesting nodes of beams. All equations are
        taken from: https://de.wikipedia.org/wiki/Bessel-Punkt
"""

class BeamNodes:
    def __init__(self,length=1.0):
        self._L = length
        self._a_bessel = 0  # lead to minimum maximium deflection
        self._a_airy = 0    # lead to flat edges
        self._a_edge_stress_min = 0

        self.compute_bessel_points()
        self.compute_airy_points()
        self.compute_minimum_edge_stress_points()

    def compute_bessel_points(self):
        self._a_bessel = (1.5**0.5 - 1.) * self._L

    def compute_airy_points(self):
        self._a_airy = 0.5 * (1 - 1./3.**0.5) * self._L

    def compute_minimum_edge_stress_points(self):
        self._a_edge_stress_min = (2.**0.5 - 1) / 2. * self._L

    def get_bessel_point_distance_from_edge(self):
        return self._a_bessel

    def get_airy_point_distance_from_edge(self):
        return self._a_airy

    def get_minimum_edge_stress_points_distance_from_edge(self):
        return self._a_edge_stress_min

if __name__ == "__main__":

    L = 1.2
    test_beam = BeamNodes(L)
    a_bessel = test_beam.get_bessel_point_distance_from_edge()
    a_airy = test_beam.get_airy_point_distance_from_edge()
    a_mes = test_beam.get_minimum_edge_stress_points_distance_from_edge()

    print("Beam Nodes Test")
    print("----------------\n")

    print("Test beam length is: L = " + str(L) + " m")
    print("\t=> a_bessel = " + str(a_bessel) + " m")
    print("\t=> a_airy = " + str(a_airy) + " m")
    print("\t=> a_mes = " + str(a_mes) + " m")

    print("\n")
