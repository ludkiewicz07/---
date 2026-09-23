def translating_RNA_into_protein(s):
   protein = ""
   for z in range(0, len(s), 3):
       codon = s[z:z+3]
       if len(codon) < 3:
           break
       amino_acid = gen_code[codon]
       if amino_acid == "Stop":
           break
       protein += amino_acid
   return protein

gen_code = {}
with open("RNA_codon_table") as file:
    for line in file:
        letters = line.split()
        for i in range(len(letters)):
            if len(letters[i]) == 3:
                codon = letters[i]
                amino_acid = letters[i+1]
                gen_code[codon] = amino_acid

with open("rosalind6") as f:
    s = f.read().strip()

final_protein = translating_RNA_into_protein(s)
print(final_protein)
            
