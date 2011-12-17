'''
Created on Dec 16, 2011

@author: mkiyer
'''

chrom_names = [["chr1", "1"],
               ["chr2", "2"],
               ["chr3", "3"],
               ["chr4", "4"],
               ["chr5", "5"],
               ["chr6", "6"],
               ["chr7", "7"],
               ["chr8", "8"],
               ["chr9", "9"],
               ["chr10", "10"],
               ["chr11", "11"],
               ["chr12", "12"],
               ["chr13", "13"],
               ["chr14", "14"],
               ["chr15", "15"],
               ["chr16", "16"],
               ["chr17", "17"],
               ["chr18", "18"],
               ["chr19", "19"],
               ["chr20", "20"],
               ["chr21", "21"],
               ["chr22", "22"],
               ["chrX", "X"],
               ["chrY", "Y"],
               ["chrM", "MT"]]

ucsc_to_ensembl_dict = dict(chrom_names)
ensembl_to_ucsc_dict = dict((v,k) for k,v in ucsc_to_ensembl_dict.iteritems())

conversion_dicts = {("ucsc","ensembl"): ucsc_to_ensembl_dict,
                    ("ensembl","ucsc"): ensembl_to_ucsc_dict}

def convert(chrom, from_chrom="ensembl", to_chrom="ucsc"):
    return conversion_dicts[(from_chrom,to_chrom)][chrom]

def ucsc_to_ensemble(chrom):
    return ucsc_to_ensembl_dict[chrom]
def ensembl_to_ucsc(chrom):
    return ensembl_to_ucsc_dict[chrom]