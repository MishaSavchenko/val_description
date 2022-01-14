#!/bin/bash
for f in $(find ./model/ -name '*.dae' -or -name '*.ply');
do
    meshlabserver -i $f -o ${f%.*}.obj
done
