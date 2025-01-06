## PACHQA validation

### Working Environment

Create python environment and install requirements.txt
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Extract `PACHQA1-main.7z` to `data`.

```bash
mkdir data
7z x PACHQA1-main.7z -odata
```

### Extract COMPAS data to `compas` directory and prepare structures.

```bash
for required_file in COMPAS-1/compas-1x.tar.gz \
                     COMPAS-1/compas-1x.csv \
                     COMPAS-2/compas-2x.sdf.gz \
                     COMPAS-2/compas-2x.csv \
                     COMPAS-3/compas-3x.tar.gz \
                     COMPAS-3/compas-3x.csv
do 
    mkdir -p compas/$(dirname $required_file)
    curl "https://gitlab.com/porannegroup/compas/-/raw/main/$required_file" --output compas/$required_file
done
cd compas
cd COMPAS-1
tar xvf compas-1x.tar.gz
mv pahs-cata-34072-xyz compas-1x.csv_structures
cd ../COMPAS-2
gzip -dk compas-2x.sdf.gz
mv compas-2x.sdf compas-2x.csv_structures
cd ../COMPAS-3
tar xvf compas-3x.tar.gz
mv compas3x-xyzs compas-3x.csv_structures
```

### Extract QMUGS data to `qmugs` directory and prepare structures.

Download from the [QMugs repository](https://libdrive.ethz.ch/index.php/s/X5vOBNSITAG5vzM) `structures.tar.gz` and `summary.csv` and extract these files.

```bash
mkdir qmugs
curl 'https://libdrive.ethz.ch/index.php/s/X5vOBNSITAG5vzM/download?path=%2F&files=summary.csv' --output qmugs/summary.csv
curl 'https://libdrive.ethz.ch/index.php/s/X5vOBNSITAG5vzM/download?path=%2F&files=structures.tar.gz' --output qmugs/structures.tar.gz
cd qmugs
tar xvf structures.tar.gz
mv structures summary.csv_structures
```
