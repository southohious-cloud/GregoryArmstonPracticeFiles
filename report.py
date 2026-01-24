AU_IN_METERS = 1.496e11   # meters per AU


def main():
    spacecrafts = [
        {"name": "Voyager 1", "distance": 163},
        {"name": "Voyager 2", "distance": 136},
        {"name": "Pioneer 10", "distance": 133},
        {"name": "New Horizons", "distance": 58}
    ]

    for craft in spacecrafts:
        print(create_report(craft))


def au_to_meters(au):
    return au * AU_IN_METERS


def create_report(spacecraft):
    distance_au = spacecraft["distance"]
    distance_m = int(au_to_meters(distance_au))

    return f"""
========= REPORT =========

Name:        {spacecraft["name"]}
Distance:    {distance_au} AU
Distance:    {distance_m:,} m

=========================
"""


if __name__ == "__main__":
    main()
