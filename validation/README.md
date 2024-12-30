## PACHQA validation

### Working Environment

Create python environment and install requirements.txt
```bash
python3 -m venv venv
source venv/bin/activate
pip3 intstall -r requirements.txt
```

### Extract `PACHQA1-main.7z` to `data`.

```bash
tar xvf PACHQA1-main.7z -C data
```

### Clone COMPAS data to `compas` directory.

```bash
git clone --depth=1 https://gitlab.com/porannegroup/compas
rm -rf compas/.git
```

### Clone QMUGS data to `qmugs` directory.

Download from (libdrive)[https://libdrive.ethz.ch/index.php/s/X5vOBNSITAG5vzM] `structures.tar.gz` and `summary.csv` and extract this files.
