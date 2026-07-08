# Program Assignment 7: Plastics Identification
plastics = {
    1: {"Polymer": "PET (Polyethylene Terephthalate)",
        "Products": "Soft drink bottles, food packaging",
        "Recyclability": "Widely recycled",
        "Remarks": "Can release microplastics if reused"},
    2: {"Polymer": "HDPE (High Density Polyethylene)",
        "Products": "Milk jugs, detergent bottles",
        "Recyclability": "Widely recycled",
        "Remarks": "Durable, low hazard"},
    3: {"Polymer": "PVC (Polyvinyl Chloride)",
        "Products": "Pipes, window frames",
        "Recyclability": "Limited recycling",
        "Remarks": "Can release toxic chlorine compounds"},
    4: {"Polymer": "LDPE (Low Density Polyethylene)",
        "Products": "Plastic bags, film wrap",
        "Recyclability": "Not widely recycled",
        "Remarks": "Lightweight, persistent in environment"},
    5: {"Polymer": "PP (Polypropylene)",
        "Products": "Food containers, bottle caps",
        "Recyclability": "Recyclable in some areas",
        "Remarks": "Heat resistant, safe for food"},
    6: {"Polymer": "PS (Polystyrene)",
        "Products": "Disposable cups, foam packaging",
        "Recyclability": "Rarely recycled",
        "Remarks": "Can leach styrene, environmental hazard"},
    7: {"Polymer": "Other (Polycarbonate, Nylon, etc.)",
        "Products": "Baby bottles, electronics",
        "Recyclability": "Varies",
        "Remarks": "May contain BPA, health concerns"}
}

code = int(input("Enter recycling code (1-7): "))
if code in plastics:
    for key, value in plastics[code].items():
        print(f"{key}: {value}")
else:
    print("Invalid recycling code.")
