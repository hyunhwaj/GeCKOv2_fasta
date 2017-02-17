from collections import defaultdict


def csv_to_fasta(csv_file):
    print("csv_to_fasta: {}".format(csv_file))
    sgRNA = defaultdict(list)
    with open(csv_file, "r") as inp:
        i = 0
        for line in inp:
            i += 1
            if i <= 1: continue
            line = line.strip().split(",")
            sgRNA[line[0]].append(line[2])

    fasta_file = csv_file.replace(".csv",".fasta")
    with open(fasta_file, "w") as oup:
        for gene in sorted(sgRNA):
            for i, seq in enumerate(sgRNA[gene]):
                oup.write(">{}_{}\n{}\n".format(gene,i+1, seq))

csv_to_fasta("Human_GeCKOv2_Library_A_09Mar2015.csv")
csv_to_fasta("Human_GeCKOv2_Library_B_09Mar2015.csv")
csv_to_fasta("Mouse_GeCKOv2_Library_A_09Mar2015.csv")
csv_to_fasta("Mouse_GeCKOv2_Library_B_09Mar2015.csv")

def merge_fasta(fasta_files, out_file):
    print("merge_fasta: {}".format(out_file))
    sgRNA = defaultdict(int)
    with open(out_file, "w") as oup:
        for fasta in fasta_files:
            print("reading {}...".format(fasta))
            with open(fasta,"r") as inp:
                while True:
                    first = inp.readline().strip()
                    if len(first)<=0: break
                    gene = first.replace(">","").split("_")[0]
                    seq = inp.readline().strip()
                    sgRNA[gene] += 1
                    oup.write(">{}_{}\n{}\n".format(gene, sgRNA[gene], seq))

                
from glob import glob
merge_fasta(sorted(glob("Human*.fasta")), "Human_GeCKOv2_Library_AB.fasta")
merge_fasta(sorted(glob("Mouse*.fasta")), "Mouse_GeCKOv2_Library_AB.fasta")
