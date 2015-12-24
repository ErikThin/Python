"""
DNA Replicator
A - T
C - G
Daily Programmer #207 Easy
"""

def replication(sequence):
    """mirrors the sequence"""
    spliced = sequence.split(' ')
    DNA = {'A':'T',
           'T':'A',
           'C':'G',
           'G':'C',
           'U':'A'}
    mirror = [DNA[x] for x in spliced]
    return '%s\n%s'%(sequence, ' '.join(mirror))

def transcription(sequence):
    """Transcription is the copying of the DNA to an mRNA"""
    spliced = sequence.split(' ')
    RNA = {'A':'U',
           'T':'A',
           'C':'G',
           'G':'C'}
    mirror = [RNA[x] for x in spliced]
    return '%s\n%s'%(sequence, ' '.join(mirror))

print(replication('A A T G C C T A T G G C'))
print()
print(transcription('A A T G C C T A T G G C'))
