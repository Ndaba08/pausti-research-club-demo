attendance = (("Simba", True), ("Irene", False), ("Idris", False), ("Eline", True))

for name, present in attendance:
    print(f"{name} is present") if present else print(f"{name} is absent")