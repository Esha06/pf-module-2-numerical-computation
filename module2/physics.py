"""Basic kinematics for constant acceleration (SI units: m, s, m/s, m/s^2)."""
import math

G = 9.81  # gravitational acceleration, m/s^2


def final_velocity(u, a, t):
    """v = u + a*t"""
    return u + a * t


def displacement(u, a, t):
    """s = u*t + 1/2*a*t^2"""
    return u * t + 0.5 * a * t ** 2


def velocity_from_displacement(u, a, s):
    """v = sqrt(u^2 + 2*a*s)"""
    v_squared = u ** 2 + 2 * a * s
    if v_squared < 0:
        raise ValueError("u**2 + 2*a*s is negative: the object never reaches s")
    return math.sqrt(v_squared)


def projectile(speed, angle_deg, g=G):
    """Launch from ground level; return time of flight, max height and range."""
    theta = math.radians(angle_deg)
    vx = speed * math.cos(theta)
    vy = speed * math.sin(theta)
    time_of_flight = 2 * vy / g
    return {
        "time_of_flight": time_of_flight,
        "max_height": vy ** 2 / (2 * g),
        "range": vx * time_of_flight,
    }


def simulate_fall(height, dt=0.01, g=G):
    """Step a dropped object forward in small time steps until it lands.

    Returns (time, speed). This is how a physics engine works.
    """
    t, y, v = 0.0, height, 0.0
    while y > 0:
        v += g * dt
        y -= v * dt
        t += dt
    return t, v
