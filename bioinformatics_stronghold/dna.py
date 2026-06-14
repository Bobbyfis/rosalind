def count_nucs(seq):
    a_count = 0
    t_count = 0
    g_count = 0
    c_count = 0
    for nuc in seq:
        if nuc == "A":
            a_count += 1
        elif nuc == "T":
            t_count += 1
        elif nuc == "G":
            g_count += 1
        else:
            c_count += 1

    return f"{a_count} {c_count} {g_count} {t_count}"

def count_nucs_new(seq):
    return f'{seq.count("A")} {seq.count("C")} {seq.count("G")} {seq.count("T")}'


# seq = input("Give sequence as string \n")
# print(count_nucs(seq))

from pathlib import Path

base = Path(__file__).parent

with open(base / "data" / "rosalind_dna.txt") as f:
    seq = f.read().strip()

result = count_nucs(seq)

with open(base / "files" / "dna.txt", "w") as f:
    f.write(result + "\n")

print(result)