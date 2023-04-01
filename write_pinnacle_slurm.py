#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="This script produces a slurm script")

parser.add_argument("job_name", help="", type=str)

parser.add_argument("-q", "--queue", help="Which queue the slurm job will be submitted to, default is comp72", default="comp72")
parser.add_argument("-n", "--nodes", help="How many nodes the job will require, default is 1", default="1")
parser.add_argument("-p", "--processors", help="Number of processors required by the job, default is 1", default="1")
parser.add_argument("-w", "--walltime", help="Amount of time after which the job will be killed if it is still running, default is 01:00:00", default="01:00:00")

args = parser.parse_args()

print("#!/bin/bash")
print("")
print("#SBATCH --job-name=" + args.job_name)
print("#SBATCH --partition", args.queue)
print("#SBATCH --nodes=" + args.nodes)
print("#SBATCH --tasks-per-node=" + args.processors)
print("#SBATCH --time=" + args.walltime)
print("#SBATCH -o %" + args.job_name + ".out")
print("#SBATCH -e %" + args.job_name + ".out")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=fuccello@uark.edu")
print("")
print("cd $SLURM_SUBMIT_DIR")
print("")
print("# Commands go here")
