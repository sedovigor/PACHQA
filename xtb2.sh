obabel -i sdf pubchem_conf.sdf -o xyz -O mmff94.xyz --minimize --ff MMFF94 --steps 10000 --sd
otool_xtb mmff94.xyz -c 0 -u 0 --namespace xtb2 --ohess extreme --molden --esp > xtb2.log
for i in {0..99}
do
if grep -q significant xtb2.log; then
  otool_xtb xtb2.xtbhess.xyz -c 0 -u 0 --namespace xtb2 --ohess extreme --molden --esp > xtb2.log
fi
done
