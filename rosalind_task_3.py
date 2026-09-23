def first_mendel_law(k, m, n):
    all = k+m+n
    all_pairs = (all*(all-1)) / 2
    aa_aa = 1*(n*(n-1)/2) #вероятность появления рецессивного потомка при скрещивании двух гомозигот - 100%
    Aa_Aa = 1/4*(m*(m-1)/2) #вероятность появления рецессивного потомка при скрещивании двух гетерозигот - 25%
    Aa_aa = 1/2*(m*n) #вероятность появления рецессивного потомка при скрещивании гомозиготы и гетерозиготы - 50%
    P_R = (aa_aa + Aa_Aa + Aa_aa) / all_pairs
    P_D = 1 - P_R
    return P_D

with open("rosalind_3", 'r') as file:
    k, m, n = map(int, file.readline().split())
print(round(first_mendel_law(k, m, n), 5))