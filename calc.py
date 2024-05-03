import random

DELTA = 0.00000001

initial_vol = random.randint(1000, 10000)
initial_solute = random.randint(50, 500)
initial_conc = initial_solute/initial_vol
print(f"Initial number of solute particles: {initial_solute} particles")
print(f"Initial volume of solution: {initial_vol} volume units")
print(f"Initial concentration of solution: {initial_conc} particles per volume volume unit")
print(f"Volume increase from {initial_vol} by (1/3) = {initial_vol} + {initial_vol*(1/3):.2f} = {initial_vol * (4/3):.2f}")
new_vol = initial_vol * (4/3)
print(f"New volume of solution: {new_vol:.2f} volume units")
new_conc = initial_solute / new_vol
print(f"New concentration = {new_conc:.2f} particles per volume unit, (initial concentration * (3/4)) = "
      f"{initial_conc*(3/4):.2f} particles per volume unit")
yes_no = "YES" if ((initial_solute / new_vol) - (initial_conc * 3/4) < DELTA) else "NO"
print(f"Is the (initial concentration * (3/4)) equal to the new concentration: {yes_no}")
