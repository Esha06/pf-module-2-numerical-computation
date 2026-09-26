# Module 2 - Part 10: Physics engine fundamentals
import math

import physics

t = 3.0
v = physics.final_velocity(0, physics.G, t)
s = physics.displacement(0, physics.G, t)
print(f"Free fall for {t} s: v = {v:.2f} m/s, distance = {s:.2f} m")
print(f"Speed after falling 20 m: {physics.velocity_from_displacement(0, physics.G, 20):.2f} m/s")

u, a = 25.0, -6.0                 # braking car
stop_time = -u / a
print(f"Braking: stops after {stop_time:.2f} s and {physics.displacement(u, a, stop_time):.1f} m")

print()
print("Projectile launched at 20 m/s")
print(f"{'Angle':>5} | {'Flight (s)':>10} | {'Height (m)':>10} | {'Range (m)':>9}")
for angle in range(15, 90, 15):
    r = physics.projectile(20, angle)
    print(f"{angle:>5} | {r['time_of_flight']:>10.2f} | {r['max_height']:>10.2f} | {r['range']:>9.2f}")

print()
exact = math.sqrt(2 * 20 / physics.G)
for dt in (0.1, 0.01, 0.001):
    t_sim, v_sim = physics.simulate_fall(20, dt)
    print(f"dt = {dt:<6} -> t = {t_sim:.4f} s (exact {exact:.4f} s, error {abs(t_sim - exact):.4f} s)")
