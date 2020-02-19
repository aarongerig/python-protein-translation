def proteins(strand):
    polypeptides = {
        'AUG': 'Methionine',
        'UAA': 'STOP',
        'UAC': 'Tyrosine',
        'UAG': 'STOP',
        'UAU': 'Tyrosine',
        'UCA': 'Serine',
        'UCC': 'Serine',
        'UCG': 'Serine',
        'UCU': 'Serine',
        'UGA': 'STOP',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UGU': 'Cysteine',
        'UUA': 'Leucine',
        'UUC': 'Phenylalanine',
        'UUG': 'Leucine',
        'UUU': 'Phenylalanine',
    }
    codons = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    result = []

    for codon in codons:
        polypeptide = polypeptides[codon]

        if polypeptide == 'STOP':
            break

        if polypeptide not in result:
            result.append(polypeptide)

    return result
