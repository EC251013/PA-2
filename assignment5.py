# Program Assignment 5: Periodic Element Information
elements = {
    "Na": {
        "Atomic Number": 11,
        "Atomic Mass": 22.99,
        "Group": 1,
        "Period": 3,
        "Electronic Configuration": "1s2 2s2 2p6 3s1",
        "Oxidation State": "+1",
        "Engineering Application": "Used in street lighting (sodium vapor lamps)"
    },
    "Fe": {
        "Atomic Number": 26,
        "Atomic Mass": 55.85,
        "Group": 8,
        "Period": 4,
        "Electronic Configuration": "[Ar] 3d6 4s2",
        "Oxidation State": "+2, +3",
        "Engineering Application": "Structural material in construction (steel)"
    },
    "Cu": {
        "Atomic Number": 29,
        "Atomic Mass": 63.55,
        "Group": 11,
        "Period": 4,
        "Electronic Configuration": "[Ar] 3d10 4s1",
        "Oxidation State": "+1, +2",
        "Engineering Application": "Electrical wiring due to high conductivity"
    }
}

symbol = input("Enter element symbol (Na, Fe, Cu): ")
if symbol in elements:
    for key, value in elements[symbol].items():
        print(f"{key}: {value}")
else:
    print("Element not available in database.")
