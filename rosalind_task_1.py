DNA_dic = {}
DNA_id = ""

def count_GC(dna_string):
     counter_G = dna_string.count("G")
     counter_C = dna_string.count("C")
     counter = counter_G + counter_C
     return(counter/len(dna_string))*100

with open("rosalind_1", 'r', encoding='utf-8') as file:
    for line in file:
         line = line.strip()
         if line.startswith(">"):
              DNA_id = line[1::]
              DNA_dic[DNA_id] = ""
         else:
              DNA_subsiquence = line
              DNA_dic[DNA_id] += DNA_subsiquence
max_id = ""
max_gc = -1.0

for d_id, DNA_subseq in DNA_dic.items():
     final = count_GC(DNA_subseq)
     if final > max_gc:
          max_id = d_id
          max_gc = final
print(max_id)
print(f"{max_gc:.6f}")

           


