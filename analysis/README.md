## DatCl

### Working Environment
To set up the required environment, run:  
```bash
conda env create -f environment.yml
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
|  E              | Total energy                                                | Eh                   |
|  H              | Total enthalpy at 298.15 K                                  | Eh                   |
|  S              | Total entropy at 298.15 K                                   | Eh/K                 |
|  G              | Total Gibbs free energy at 298.15 K                         | Eh                   |
|  dE             | Energy of atomization                                       | Eh                   |
|  dH             | Enthalpy of atomization at 298.15 K                         | Eh                   |
|  dS             | Entropy of atomization at 298.15 K                          | Eh/K                 |
|  dG             | Gibbs free energy of atomization at 298.15 K                | Eh                   |
|  zpe            | Zero point energy                                           | Eh                   |
|  homo           | Energy of the highest occupied molecular orbital            | eV                   |
|  lumo           | Energy of the lowest unoccupied molecular orbital           | eV                   |
|  gap            | Difference between LUMO and HOMO energies                   | eV                   |
|  Mu             | Total dipole moment                                         | Debye                |
|  alpha          | Isotropic polarizability                                    | a.u. (atomic units)  |
|  tMu            | Dipole moment tensor (space delimeter)                      | Debye                |
|  rotN           | Rotational constants (N = A B C)                            | 1/cm                 |
