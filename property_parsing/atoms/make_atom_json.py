import json
import pandas as pd


df = pd.read_csv('props.csv')
df.insert(loc=4, column='S', value=((df.H - df.G) / 298.15))


atom_dict = {}

for prop in ('E', 'H', 'S', 'G'):
    atom_dict[prop] = {}

    for level in ('xtb2', 'r2scan', 'd4tzvp'):
        atom_dict[prop][level] = {}

        for atom in ('h', 'c', 'cl'):
            atom_dict[prop][level][atom] = float(df[(df.atom == atom) & (df.level == level)][prop].iloc[0])


for level in ('xtb2', 'r2scan', 'd4tzvp'):
    r = 12 if level == 'xtb2' else 10

    for atom, value in atom_dict['S'][level].items():
        atom_dict['S'][level][atom] = round(value, r)


with open('atom_props.json', 'w') as file:
    json.dump(atom_dict, file, indent=4)
