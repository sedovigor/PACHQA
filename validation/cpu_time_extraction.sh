#!/bin/bash
echo "key,xtb2,r2scan,d4tzvp"

for d in */; do
    for sd in $d/*/; do
        key=$(echo $sd | cut -d'/' -f3)

        read m s <<< $(grep cpu-time $sd/xtb2.out | head -1 | awk '{print $7,$9}')
        xtb2=$(echo "print(60*$m + $s)" | python)

        n=$(grep 'nprocs' $sd/r2scan.out | awk '{print $5}')
        t=$(grep 'Sum of individual times' $sd/r2scan.out | tail -1 | awk '{print $6}')
        r2scan=$(echo "print($n*$t)" | python)

        n=$(grep 'nprocs' $sd/d4tzvp.out | awk '{print $5}')
        t=$(grep 'Sum of individual times' $sd/d4tzvp.out | tail -1 | awk '{print $6}')
        d4tzvp=$(echo "print($n*$t)" | python)

        echo "$key,$xtb2,$r2scan,$d4tzvp"
    done
done
