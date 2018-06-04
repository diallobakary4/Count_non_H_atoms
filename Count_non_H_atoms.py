import os
def count_non_H(molecule_mol2):
  """
  Count the number of non H atom in a mol2 file
  """
  file = open(molecule_mol2, "r")
  file = file.readlines()
  mol = 0 #tracking when line is still in @<TRIPOS>ATOM section
  for line in file:
  #print line
  if "@<TRIPOS>ATOM" in line:
    non_H = 0
    mol = 1
  if "@<TRIPOS>BOND" in line:
    mol = 0
  if mol == 1:
  #print line[8:11]
    if line[8:11] != " H ":
      non_H +=1
  return non_H - 1 # -1 because the first atom doesnt include any h atom and is not part of the molecule
