# PACHQA dataset of quantum chemical properties of chlorinated polycyclic aromatic hydrocarbons (Cl-PAHs)
The dataset_generation.ipynb notebook was used to prepare the input molecules for the dataset generation. The files `chcl.sdf` and `ArCH.sdf` used by the notebook contain the structures of all Cl-PAHs and PAHs extracted from the PubChem database. They must be unpacked with 7z:
```bash
7z x chcl.7z
7z x ArCH.7z
```

The code filters the selected molecules by applying additional restrictions and generates new molecules not present in PubChem by adding chlorine atoms.

All the molecules were minimized in the MMFF94 force field and optimized with GFN2-xTB using the bash script `xtb2.sh`. The DFT calculations were performed with ORCA 5.0.4 using the input files `r2scan.inp` and `d4tzvp.inp`. The output was parsed for the calculated properties as described in `./property_parsing`. The dataset validation scripts are available in `./validation`.
