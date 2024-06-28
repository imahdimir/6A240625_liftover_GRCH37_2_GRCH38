from pathlib import Path

PROJ = '2564_liftover_GRCH37_2_GRCH38'

class Dir :
    prj_data = Path(f'/var/genetics/ws/mahdimir/local/prj_data/{PROJ}')

    inp = prj_data / 'inp'
    med = prj_data / 'med'
    out = prj_data / 'out'

    snps_by_chr = inp / 'snps_by_chr'


D = Dir()

class FilePattern :
    snps_by_chr = str(D.snps_by_chr / 'c{chr_num}.txt')

FP = FilePattern()

class Files :
    all_snps = D.med / 'snps.lift.bed'

F = Files()
