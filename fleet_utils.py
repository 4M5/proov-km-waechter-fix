# fleet_utils.py
# Utility helpers for KM-Waechter. Dead code removed 2025.

KM_PER_MILE = 1.60934          # 1 mile = 1.60934 km, so km ÷ 1.60934 = miles
MILES_PER_KM = 1 / KM_PER_MILE  # ≈ 0.6214


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles for the UK partner report."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a float to one decimal place."""
    return f"{value:.1f}"
