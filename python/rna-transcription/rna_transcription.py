def to_rna(dna_strand):
    rna_strand = ''
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for nucleo in dna_strand:
        if nucleo not in dna_to_rna.keys():
            rna_strand += nucleo
        else:
            rna_strand += dna_to_rna[nucleo]
    return rna_strand
    pass
