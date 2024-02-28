#Write a Python Program to Illustrate Different Set Operations.
#our Output should look something like this
#Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8} Intersection of E and N is {2, 4} Difference of E and N is {8, 0, 6} Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}

E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}


union = E.union(N)
print(f"Union of E and N is {union}")


intersection = E.intersection(N)
print(f"Intersection of E and N is {intersection}")


difference = E.difference(N)
print(f"Difference of E and N is {difference}")


symmetric_difference = E.symmetric_difference(N)
print(f"Symmetric difference of E and N is {symmetric_difference}")
