# 20171211_target_capture_panel
To run the scripts:

python GC_content.py genomic_MTM1.fasta
This script generate %GC on 200 base window size with 1 base step size. The output of this script is a plot of %GC per 200base across the input sequencde.

python homopolymer_dist.py genomic_MTM1.fasta
The script generate all homopolymers (>=2 mers) that are present in the input sequence. The output of this script is four bar plots for the "log10(occurence)" (Y-axis) vs "number of homopolymers" (X-axis), each plot for one of the four bases.
