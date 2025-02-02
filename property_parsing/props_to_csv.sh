#!/bin/bash
path=$1
init_path=$(pwd)
echo "id,subset,key,smiles,level,E,H,S,G,zpe,homo,lumo,gap,Mu,alpha,tMu,rotA,rotB,rotC"

total=$(echo "print(($(ls $path/* | wc -w)-5)*3)" | python)

cd $path

j=1
for sup_dir in 'pubchemPAH' 'pubchemPCH' 'monoCl' 'polyCl' 'perCl'; do
    cd $sup_dir

    i=1
    for sub_dir in */; do
        cd $sub_dir

        smi=$(obabel r2scan.xyz -o smi --canonical 2> /dev/null | awk '{print $1}')

        for level in 'xtb2' 'r2scan' 'd4tzvp'; do

            if [ $level == 'xtb2' ]; then
                content=$(cat xtb2.log)

                E=$(echo "$content" | grep '| TOTAL ENERGY'    | awk '{print $4}')
                H=$(echo "$content" | grep 'TOTAL ENTHALPY'    | awk '{print $4}')
                G=$(echo "$content" | grep 'TOTAL FREE ENERGY' | awk '{print $5}')
                S=$(echo "print(round(($H - $G) / 298.15, 12))" | python)
                zpe=$(echo "$content" |grep 'zero point energy' | awk '{print $5}')


                homo=$(echo "$content"  | grep '(HOMO)'               | awk '{print $4}'      | tail -1)
                lumo=$(echo "$content"  | grep '(LUMO)'               | awk '{print $(NF-1)}' | tail -1)
                gap=$(echo "$content"   | grep 'HOMO-LUMO GAP'        | awk '{print $4}')


                Mu=$(echo "$content"    | grep 'molecular dipole' -A3 | awk '{print $5}'      | tail -1)
                alpha=$(echo "$content" | grep 'Mol. α(0) /au'        | awk '{print $5}')
                tMu=$(echo "$content" | grep 'molecular dipole' -A3 | awk '{print $2,$3,$4}'| tail -1)

                read rotA rotB rotC <<< $(echo "$content" | grep 'rotational constants/cm' | awk '{print $4,$5,$6}')

            elif [ $level == 'r2scan' ]; then
                content=$(cat r2scan.out)
                property=$(cat r2scan_property.txt)

                E=$(echo "$content" | grep 'FINAL SINGLE POINT ENERGY' | tail -1 | awk '{print $5}')
                H=$(echo "$property" | grep 'Enthalpy (Hartree)'       | awk '{print $4}')
                G=$(echo "$property" | grep 'Gibbs Energy (Hartree)'   | awk '{print $5}')
                S=$(echo "print(round(($H - $G) / 298.15, 10))" | python)
                zpe=$(echo "$property" | grep 'Zero Point Energy (Hartree)' | awk '{print $6}')


                homo=$(echo "$content" | grep 'ORBITAL ENERGIES' -A600 | tail -600 | grep '  2.0000  ' | tail -1 | awk '{print $4}')
                lumo=$(echo "$content" | grep 'ORBITAL ENERGIES' -A600 | tail -600 | grep '  0.0000  ' | head -1 | awk '{print $4}')
                gap=$(echo "print(round($lumo-$homo, 4))"| python)


                Mu=$(echo "$content"    | grep 'Magnitude (Debye)'        | awk '{print $4}')
                alpha=$(echo "$content" | grep 'Isotropic polarizability' | awk '{print $4}')
                tMu=$(echo "$content" | grep 'Total Dipole Moment' | awk '{print $5,$6,$7}')

                read rotA rotB rotC <<< $(echo "$content" | grep 'Rotational constants in cm-1' | tail -1 | awk '{print $5,$6,$7}')

                cE=$E
                cH=$H
                cG=$G

            else
                content=$(cat d4tzvp.out)

                E=$(echo "$content" | grep 'FINAL SINGLE POINT ENERGY' | tail -1 | awk '{print $5}')
                H=$(echo "print($cH - round($cE, 10) + round($E, 10))" | python)
                G=$(echo "print($cG - round($cE, 10) + round($E, 10))" | python)
                S=$(echo "print(round(($H - $G) / 298.15, 10))" | python)


                homo=$(echo "$content" | grep 'ORBITAL ENERGIES' -A600 | tail -600 | grep '  2.0000  ' | tail -1 | awk '{print $4}')
                lumo=$(echo "$content" | grep 'ORBITAL ENERGIES' -A600 | tail -600 | grep '  0.0000  ' | head -1 | awk '{print $4}')
                gap=$(echo "print(round($lumo-$homo, 4))" | python)


                Mu=$(echo "$content"    | grep 'Magnitude (Debye)'        | awk '{print $4}')
                alpha=$(echo "$content" | grep 'Isotropic polarizability' | awk '{print $4}')

                tMu=$(echo "$content" | grep 'Total Dipole Moment' | awk '{print $5,$6,$7}')
            fi

            printf "$j-%04d,${sup_dir%%/},${sub_dir%%/},$smi,$level,$E,$H,$S,$G,$zpe,$homo,$lumo,$gap,$Mu,$alpha,$tMu,$rotA,$rotB,$rotC\n" $i
        done

        cd ..
        ((i++))
    done

    cd ..
    ((j++))
done | tqdm --total $total

cd $init_path
