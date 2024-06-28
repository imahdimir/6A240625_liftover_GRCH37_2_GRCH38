"""

    This module makes a list compatible with/suitable for $liftover program
    that Aysu told us.

    This module reads all snps from all chromosomes and writes them to a file
    with this format (without header):

    # chr    start    end    rsid
    chr1    10000    10001    rs123

    Then I use output file as input for $liftover program to
    convert from GRCH37 to GRCH38.

    The list consists of all SNPs previously randomly selected
    from the UK Biobank data. 1k SNPs were selected from each info score with
    info score between .3 to 1 with .01 increments.

"""

import pandas as pd

from prj.lib import F
from prj.lib import FP

def main() :
    pass

    ##
    df_all = pd.DataFrame()

    for cn in range(1 , 22 + 1) :
        fn = FP.snps_by_chr.format(chr_num = cn)
        print(fn)

        df = pd.read_csv(fn , sep = '\t' , header = None)

        df['chr'] = f'chr{cn}'

        df['pos-1'] = df[2] - 1

        df = df[['chr' , 'pos-1' , 2 , 1]]

        df_all = pd.concat([df_all , df])

    ##
    df_all.to_csv(F.all_snps , sep = '\t' , header = None , index = None)

    ##

def _test() :
    pass

    ##
    fn1 = '/var/genetics/ws/mahdimir/local/prj_data/2564_liftover_GRCH37_2_GRCH38/out/snps.lifted'
    df1 = pd.read_csv(fn1 , sep = '\t' , header = None)

    ##
    fn2 = '/var/genetics/ws/mahdimir/local/prj_data/2564_liftover_GRCH37_2_GRCH38/out/snps.unlifted'
    df2 = pd.read_csv(fn2 , sep = '\t' , header = None)

    ##


    ##
