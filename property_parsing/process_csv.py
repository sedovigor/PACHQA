import sys
import json

import numpy as np
import pandas as pd

from rdkit.Chem import AllChem as Chem
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import Descriptors


with open('atoms/atom_props.json') as file:
    atom_dict = json.loads(file.read())


def count_hydrogens(mol):
    mol = Chem.AddHs(mol)
    smi = Chem.MolToSmiles(mol)
    return smi.count('H')

def count_carbons(mol):
    hac = Descriptors.HeavyAtomCount(mol)
    han = Descriptors.NumHeteroatoms(mol)
    return hac - han

def get_atomiz_props(df, prop):
    prop_list = []

    for _, row in df.iterrows():
        sub_dict = atom_dict[prop][row.level]
        atomic_prop = row.nH*sub_dict['h'] + row.nC*sub_dict['c'] + row.nCl*sub_dict['cl']

        if row.level == 'xtb2' or prop == 'E':
            atomic_prop = round(atomic_prop, 12)
            atomiz_prop = atomic_prop - row[prop]
            atomiz_prop = round(atomiz_prop, 12)
        else:
            atomic_prop = round(atomic_prop, 10)
            atomiz_prop = atomic_prop - row[prop]
            atomiz_prop = round(atomiz_prop, 10)

        prop_list.append(atomiz_prop)
    return prop_list

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    df = pd.read_csv(input_path)

    df['mol'] = df.smiles.map(Chem.MolFromSmiles)
    df['mwt'] = df.mol.map(Descriptors.MolWt).round(3)

    df['nH'] = df.mol.map(count_hydrogens)
    df['nC'] = df.mol.map(count_carbons)
    df['nCl'] = df.smiles.str.count('Cl')


    for prop in ('E', 'H', 'S', 'G'):
        prop_list = get_atomiz_props(df, prop)
        df[f'd{prop}'] = prop_list

    df['formula'] = df.mol.map(rdMolDescriptors.CalcMolFormula)

    df = df['id subset key smiles formula level mwt nH nC nCl E H S G dE dH dS dG zpe homo lumo gap Mu alpha tMu rotA rotB rotC'.split()]
    df.to_csv('props.csv', index=False)
