# Assignment #3

## Ashlynn Fuccello

#### BIOL5153, Spring 2023

1.  This command copies the mt_genomes folder from my local computer
    to the storage directory of my account on the server (this command is run from the
    directory on my local computer that contains the local copy of
    mt_genomes):
    `rsync -avz mt_genomes fuccello@hpc-portal2.hpc.uark.edu:/storage/fuccello`

2.  This command copies the unknwon.fa file from my local computer into
    the mt_genomes folder that the last command put on the server (this
    command is run from the directory on my local computer that contains
    unknown.fa):
    `scp unknown.fa fuccello@hpc-portal2.hpc.uark.edu:/storage/fuccello/mt_genomes`

3.  This command creates and lets me edit a file named genomes.slurm
    where I put the below information:`nano genomes.slurm`. Then this
    command submits the previously created file as a job on the cluster:
    `sbatch genomes.slurm`

    1.  #!/bin/bash

        #SBATCH --job-name=assn03\
        #SBATCH --partition comp72\
        #SBATCH --nodes=1\
        #SBATCH --tasks-per-node=1\
        #SBATCH --time=00:01:00\
        #SBATCH -o %assn03.out\
        #SBATCH -e %assn03.err\
        #SBATCH --mail-type=ALL\
        #SBATCH
        --[mail-user=fuccello\@uark.edu](mailto:mail-user=fuccello@uark.edu){.email}

        `cd \$SLURM_SUBMIT_DIR`

        \# job command here\
        `module purge`\
        `module load blast cat`\
        `mt_genomes/\*.fasta \> mt_genomes/genomes.fas makeblastdb -in mt_genomes/genomes.fas -dbtype nucl`\
        `blastn -query mt_genomes/unknown.fa -db mt_genomes/genomes.fas \> mt_genomes/unknown.vs.genomes.blastn`

4.  This command syncs the changes made to the mt_genomes folder on the
    server with the mt_genomes directory on my local computer (this
    command is run from the directory on my local computer that contains
    the local copy of mt_genomes):
    `rsync -avz fuccello@hpc-portal2.hpc.uark.edu:/storage/fuccello/mt_genomes .`

5.  Below are my answers to the parts of question 5:

    1.  My job ran in 00:00:03.
    2.  The closest match to the database is Cucurbita.
