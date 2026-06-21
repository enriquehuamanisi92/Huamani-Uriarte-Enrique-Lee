from pathlib import Path

import numpy as np
import pandas as pd


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def build_zone_table(rng: np.random.Generator, n_zones: int) -> pd.DataFrame:
    sectors = np.array(
        [
            "collique",
            "la_libertad",
            "retablo",
            "tahuantinsuyo",
            "santa_luzmila",
            "zonal_14",
        ]
    )
    sector = rng.choice(sectors, size=n_zones, p=[0.22, 0.18, 0.18, 0.16, 0.14, 0.12])

    # Synthetic coordinates roughly around the district of Comas.
    latitude = rng.uniform(-11.965, -11.890, size=n_zones)
    longitude = rng.uniform(-77.085, -77.015, size=n_zones)

    vulnerability_base = {
        "collique": 0.72,
        "la_libertad": 0.66,
        "retablo": 0.48,
        "tahuantinsuyo": 0.55,
        "santa_luzmila": 0.34,
        "zonal_14": 0.58,
    }
    commercial_base = {
        "collique": 0.45,
        "la_libertad": 0.58,
        "retablo": 0.72,
        "tahuantinsuyo": 0.50,
        "santa_luzmila": 0.67,
        "zonal_14": 0.61,
    }

    socioeconomic_vulnerability = np.clip(
        np.array([vulnerability_base[s] for s in sector]) + rng.normal(0, 0.08, n_zones),
        0.05,
        0.95,
    )
    commercial_density = np.clip(
        np.array([commercial_base[s] for s in sector]) + rng.normal(0, 0.10, n_zones),
        0.05,
        0.95,
    )
    population_density_km2 = np.round(
        8500 + 14500 * socioeconomic_vulnerability + rng.normal(0, 1800, n_zones),
        0,
    ).astype(int)
    youth_share = np.clip(0.18 + 0.16 * socioeconomic_vulnerability + rng.normal(0, 0.025, n_zones), 0.12, 0.42)
    transit_access_index = np.clip(0.25 + 0.55 * commercial_density + rng.normal(0, 0.12, n_zones), 0.03, 0.98)
    road_connectivity_index = np.clip(0.20 + 0.50 * commercial_density + rng.normal(0, 0.10, n_zones), 0.03, 0.98)
    lighting_coverage = np.clip(0.88 - 0.38 * socioeconomic_vulnerability + rng.normal(0, 0.08, n_zones), 0.20, 0.98)
    cctv_density = np.clip(0.12 + 0.28 * commercial_density - 0.12 * socioeconomic_vulnerability + rng.normal(0, 0.05, n_zones), 0.01, 0.55)
    patrol_coverage = np.clip(0.25 + 0.26 * commercial_density - 0.16 * socioeconomic_vulnerability + rng.normal(0, 0.08, n_zones), 0.03, 0.85)
    distance_to_transit_corridor_km = np.clip(1.4 - 1.15 * transit_access_index + rng.normal(0, 0.18, n_zones), 0.05, 2.50)

    return pd.DataFrame(
        {
            "zone_id": [f"CZ-{i:03d}" for i in range(1, n_zones + 1)],
            "sector": sector,
            "latitude": np.round(latitude, 6),
            "longitude": np.round(longitude, 6),
            "population_density_km2": population_density_km2,
            "socioeconomic_vulnerability": np.round(socioeconomic_vulnerability, 4),
            "youth_share": np.round(youth_share, 4),
            "commercial_density": np.round(commercial_density, 4),
            "transit_access_index": np.round(transit_access_index, 4),
            "road_connectivity_index": np.round(road_connectivity_index, 4),
            "lighting_coverage": np.round(lighting_coverage, 4),
            "cctv_density": np.round(cctv_density, 4),
            "patrol_coverage": np.round(patrol_coverage, 4),
            "distance_to_transit_corridor_km": np.round(distance_to_transit_corridor_km, 4),
        }
    )


def simulate_monthly_incidents(zones: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    months = pd.date_range("2018-01-01", "2025-12-01", freq="MS")
    rows = []

    zone_effect = rng.normal(0, 0.25, len(zones))
    for zone_idx, zone in zones.reset_index(drop=True).iterrows():
        latent_base = (
            -0.45
            + 1.05 * zone["socioeconomic_vulnerability"]
            + 0.90 * zone["commercial_density"]
            + 0.55 * zone["transit_access_index"]
            + 0.45 * zone["road_connectivity_index"]
            + 0.35 * zone["youth_share"]
            - 0.50 * zone["lighting_coverage"]
            - 0.42 * zone["patrol_coverage"]
            - 0.25 * zone["cctv_density"]
            + zone_effect[zone_idx]
        )

        for month_idx, date in enumerate(months):
            seasonal = 0.22 * np.sin(2 * np.pi * date.month / 12) + (0.18 if date.month in [7, 12] else 0.0)
            long_term_pressure = 0.006 * month_idx
            weekend_night_activity = np.clip(
                0.32
                + 0.24 * zone["commercial_density"]
                + (0.08 if date.month in [7, 12] else 0.0)
                + rng.normal(0, 0.05),
                0.05,
                0.95,
            )
            latent_risk = latent_base + seasonal + long_term_pressure + 0.45 * weekend_night_activity
            expected_incidents = np.exp(0.65 + latent_risk)
            observed_incidents = rng.poisson(np.clip(expected_incidents, 0.2, 35))

            rows.append(
                {
                    **zone.to_dict(),
                    "year": date.year,
                    "month": date.month,
                    "month_index": month_idx,
                    "weekend_night_activity": round(float(weekend_night_activity), 4),
                    "seasonal_pressure": round(float(seasonal), 4),
                    "observed_incidents": int(observed_incidents),
                }
            )

    base = pd.DataFrame(rows).sort_values(["zone_id", "month_index"]).reset_index(drop=True)
    base["recent_incidents"] = base.groupby("zone_id")["observed_incidents"].shift(1)
    base["rolling_3m_incidents"] = base.groupby("zone_id")["observed_incidents"].transform(
        lambda values: values.shift(1).rolling(window=3, min_periods=1).mean()
    )
    base["incident_trend"] = base["recent_incidents"] - base.groupby("zone_id")["observed_incidents"].shift(4)
    base["next_month_incidents"] = base.groupby("zone_id")["observed_incidents"].shift(-1)

    modeling = base.dropna(subset=["recent_incidents", "rolling_3m_incidents", "incident_trend", "next_month_incidents"]).copy()
    threshold = modeling["next_month_incidents"].quantile(0.68)
    modeling["target_high_risk_next_month"] = (modeling["next_month_incidents"] >= threshold).astype(int)

    modeling = modeling.drop(columns=["observed_incidents", "next_month_incidents"])
    modeling["recent_incidents"] = modeling["recent_incidents"].astype(int)
    modeling["incident_trend"] = modeling["incident_trend"].astype(int)
    modeling["rolling_3m_incidents"] = modeling["rolling_3m_incidents"].round(3)

    return modeling.reset_index(drop=True)


def main():
    rng = np.random.default_rng(42)
    zones = build_zone_table(rng=rng, n_zones=64)
    df = simulate_monthly_incidents(zones=zones, rng=rng)

    out_path = Path(__file__).resolve().parent / "comas_urban_crime_synthetic.csv"
    df.to_csv(out_path, index=False)
    print(f"Dataset created at: {out_path}")
    print(f"Rows: {len(df)} | High-risk rate: {df['target_high_risk_next_month'].mean():.3f}")
    print(f"Years: {df['year'].min()}-{df['year'].max()} | Zones: {df['zone_id'].nunique()}")


if __name__ == "__main__":
    main()
