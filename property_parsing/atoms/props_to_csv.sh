#!/bin/bash
echo "atom,level,E,H,G"

for d in 'h' 'c' 'cl'; do
    cd $d

    for level in 'xtb2' 'r2scan' 'd4tzvp'; do
        content=$(cat "$level.out")

        if [ $level == 'xtb2' ]; then
            E=$(echo "$content" | grep '| TOTAL ENERGY'    | awk '{print $4}')
            H=$(echo "$content" | grep 'TOTAL ENTHALPY'    | awk '{print $4}')
            G=$(echo "$content" | grep 'TOTAL FREE ENERGY' | awk '{print $5}')

        elif [ $level == 'r2scan' ]; then
            E=$(echo "$content" | grep 'FINAL SINGLE POINT ENERGY' | tail -1 | awk '{print $5}')
            H=$(cat "$level""_property.txt" | grep 'Enthalpy (Hartree)'       | awk '{print $4}')
            G=$(cat "$level""_property.txt" | grep 'Gibbs Energy (Hartree)'   | awk '{print $5}')

        else
            E=$(echo "$content" | grep 'FINAL SINGLE POINT ENERGY' | tail -1 | awk '{print $5}')
            H=$(cat "$level""_property.txt" | grep 'Enthalpy (Hartree)'       | awk '{print $4}')
            G=$(cat "$level""_property.txt" | grep 'Gibbs Energy (Hartree)'   | awk '{print $5}')
        fi

        echo "$d,$level,$E,$H,$G"
    done
    cd ..
done
