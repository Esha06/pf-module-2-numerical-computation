import math
import unittest

from physics import (G, displacement, final_velocity, projectile,
                     simulate_fall, velocity_from_displacement)
from report import format_report, summarize


class TestKinematics(unittest.TestCase):
    def test_final_velocity(self):
        self.assertAlmostEqual(final_velocity(0, 9.81, 2), 19.62)

    def test_displacement(self):
        self.assertAlmostEqual(displacement(5, 2, 3), 24.0)

    def test_velocity_from_displacement(self):
        self.assertAlmostEqual(velocity_from_displacement(0, 9.81, 20), math.sqrt(392.4))

    def test_unreachable_height_raises(self):
        with self.assertRaises(ValueError):
            velocity_from_displacement(1, -9.81, 10)

    def test_projectile_range_at_45_degrees(self):
        self.assertAlmostEqual(projectile(20, 45)["range"], 20 ** 2 / G)

    def test_simulation_matches_formula(self):
        t, _ = simulate_fall(20, dt=0.001)
        self.assertAlmostEqual(t, math.sqrt(2 * 20 / G), delta=0.01)


class TestReport(unittest.TestCase):
    def test_summarize(self):
        s = summarize([1.0, 2.0, 3.0])
        self.assertEqual(s["n"], 3)
        self.assertAlmostEqual(s["mean"], 2.0)
        self.assertAlmostEqual(s["std"], math.sqrt(2 / 3))

    def test_summarize_empty_raises(self):
        with self.assertRaises(ValueError):
            summarize([])

    def test_format_report(self):
        text = format_report("Run 1", {"Temperature": {"unit": "C", "values": [20.0, 22.5]}})
        self.assertIn("Run 1", text)
        self.assertIn("21.25", text)
        self.assertIn("2 readings", text)


if __name__ == "__main__":
    unittest.main()
