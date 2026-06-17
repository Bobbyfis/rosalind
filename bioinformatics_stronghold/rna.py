def dna_to_rna(dna_seq):
    rna_seq = ""
    for i in range (0, len(dna_seq)):
        if dna_seq[i] == "T":
            rna_seq = rna_seq + "U"
        else:
            rna_seq = rna_seq + dna_seq[i]

    return rna_seq

def dna_to_rna_improved(dna_seq):
    return dna_seq.replace("T", "U")
# .replace is C code inside CPython, runs much faster


"""
dna_seq = input("Input DNA sequence\n")    
result = dna_to_rna(dna_seq)
print(result)
"""

# Importing file from data and saving output to files

from pathlib import Path
base = Path(__file__).parent

with open(base / "data" / "rosalind_rna.txt") as f:
    seq = f.read().strip()

result = dna_to_rna(seq)

out = base / "files" / "rna.txt"
if not out.exists():
    out.parent.mkdir(exist_ok=True)
    with open(out, "w") as f:
        f.write(result + "\n")
    print("wrote", out)
else:
    print(out, "already exists, skipped")

print(result)