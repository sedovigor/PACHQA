## Preparation of props.csv file from calculation results

### Working Environment
To set up the required environment, run:  
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Reproducing Data Extraction
To generate a `.csv` file with molecular properties, use:  
```bash
./props_to_csv.sh data > props_raw.csv
```
```bash
python process_csv.py props_raw.csv props.csv
```

**Note:** The script expects the first two parts of the dataset, `PACHQA1-main.7z` and `PACHQA2-full_outfiles.7z`, to be extracted into a common directory, e.g., `data`.

Extraction commands:
```bash
7z x PACHQA1-main.7z -odata
7z x PACHQA2-full_outfiles.7z -odata
```


### List of Extracted Properties
Below is the list of properties included in the extraction, along with their units:  

| **Designation** | **Property Description**                                    | **Units**            |
|-----------------|-------------------------------------------------------------|----------------------|
|  id             | Molecule identifier within the dataset                      |                      |
|  subset         | The subset to which the molecule belongs                    |                      |
|  key            | InChIKey                                                    |                      |
|  smiles         | SMILES                                                      |                      |
|  formula        | Molecular formula                                           |                      |
|  level          | Enthalpy of atomization at 298.15 K                         |                      |
|  mwt            | Molecular weight                                            | g/mol                |
|  nH             | Number of hydrogen atoms                                    |                      |
|  nC             | Number of carbon atoms                                      |                      |
|  nCl            | Number of chlorine atoms                                    |                      |
|  E              | Single-point energy                                         | Eh                   |
|  H              | Total enthalpy at 298.15 K                                  | Eh                   |
|  S              | Total entropy at 298.15 K                                   | Eh/K                 |
|  G              | Total Gibbs free energy at 298.15 K                         | Eh                   |
|  dE             | Energy of atomization                                       | Eh                   |
|  dH             | Enthalpy of atomization at 298.15 K                         | Eh                   |
|  dS             | Entropy of atomization at 298.15 K                          | Eh/K                 |
|  dG             | Gibbs free energy of atomization at 298.15 K                | Eh                   |
|  zpe            | Zero-point energy                                           | Eh                   |
|  homo           | Energy of the highest occupied molecular orbital (HOMO)     | eV                   |
|  lumo           | Energy of the lowest unoccupied molecular orbital (LUMO)    | eV                   |
|  gap            | HOMO–LUMO gap                                               | eV                   |
|  Mu             | Total dipole moment                                         | Debye                |
|  alpha          | Electronic polarizability                                   | a.u. (atomic units)  |
|  tMu            | The dipole moment components (x y z) (space delimiter)      | a.u.                 |
|  rotN           | Rotational constants (N = A, B, C)                          | 1/cm                 |
