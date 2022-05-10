import argparse
import numpy as np
from tqdm import tqdm

argparser = argparse.ArgumentParser(description='Subset a fasta file')
argparser.add_argument('fasta', help='Fasta file')
argparser.add_argument('--accessions', help='.txt-file with accessions to keep')
argparser.add_argument('--output', help='Output file')
args = argparser.parse_args()

from Bio import SeqIO

accessions = np.loadtxt(args.accessions, dtype=str)
accessions = set(accessions)
print(accessions)

records=[]
for record in tqdm(SeqIO.parse(args.fasta, 'fasta')):
    if record.id in accessions:
        records.append(record)
SeqIO.write(records, args.output, 'fasta')
