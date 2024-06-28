#!/usr/bin/bash

# This script is used to convert the hg19 coordinates to hg38 coordinates

liftover="/disk/genetics/ukb/aokbay/bin/liftOver"
chain_hg19toHg38="/disk/genetics/ukb/aokbay/reffiles/hg19ToHg38.over.chain.gz"

file_in="/var/genetics/ws/mahdimir/local/prj_data/2564_liftover_GRCH37_2_GRCH38/med/snps.lift.bed"
file_out_pat="/var/genetics/ws/mahdimir/local/prj_data/2564_liftover_GRCH37_2_GRCH38/out/snps"

# Convert the coordinates
$liftover -bedPlus=3 $file_in ${chain_hg19toHg38} ${file_out_pat}.lifted ${file_out_pat}.unlifted
