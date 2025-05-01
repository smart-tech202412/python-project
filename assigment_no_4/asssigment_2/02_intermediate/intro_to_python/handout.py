def main():
    # Dictionary of planetary gravity as a percentage of Earth's
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Prompt user for weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt user for planet
    planet = input("Enter a planet: ")

    # Calculate weight on the selected planet
    if planet in gravity_factors:
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Unknown planet.")

if __name__ == '__main__':
    main()
