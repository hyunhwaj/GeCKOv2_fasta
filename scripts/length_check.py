def fasta_check(fasta_file):
    with open(fasta_file, "r") as inp:
        length = -1
        while True:
            line = inp.readline().strip()
            if len(line) <=0: break
            assert line.startswith(">")
            assert len(line[1:].split("_")) >= 2, (fasta_file, line)
            line = inp.readline().strip()    
            if length == -1: length = len(line)
            else: assert length == len(line)
    print "{}: OK!".format(fasta_file)

from glob import glob

for fasta in glob("*.fasta"):
    fasta_check(fasta)

