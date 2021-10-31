#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=36
#SBATCH --time=1:30:00
#SBATCH --out=python_job-%j.log

# load python interpreter
module load python/3.7.3 

# run the python script, given as command line argument
python $1