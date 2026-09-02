class Starship:

    def __init__(self, base_weight, cargo_weight, final_fuel):
        self.base_weight = base_weight(50000)
        self.cargo_weight = cargo_weight
        self.final_fuel = final_fuel

    def load_cargo(cargo_weight, base_weight):
        cargo_weight = cargo_weight + 1000
        
    def starship_calculate(final_fuel, cargo_weight, base_weight):
        final_fuel = (cargo_weight + base_weight) * 3

Starship.load_cargo
Starship.load_cargo
Starship.load_cargo

print("The final fuel needed is", Starship.starship_calculate)