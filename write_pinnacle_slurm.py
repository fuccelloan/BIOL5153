#! /usr/bin/env python3

job_name = "test"
queue = "comp72"
nodes = "1"
processors = "1"
walltime = "00:01:00"

print("#!/bin/bash")
print("")
print("#SBATCH --job-name=" + job_name)
print("#SBATCH --partition", queue)
print("#SBATCH --nodes=" + nodes)
print("#SBATCH --tasks-per-node=" + processors)
print("#SBATCH --time=" + walltime)
print("#SBATCH -o %" + job_name + ".out")
print("#SBATCH -e %" + job_name + ".out")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=fuccello@uark.edu")
print("")
print("cd $SLURM_SUBMIT_DIR")
print("")
print("# Commands go here")
