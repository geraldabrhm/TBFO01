from process_file import split
from process_file import delComment
from process_file import getData
from process_file import cekArrVar
from process_file import replace
from cyk import cykAlgo

#x = input("Masukkan nama file: ")
f = open("test.py","r")
isi = f.read()
array = isi.split()
array = split(array)
array, comment = delComment(array)
angka, kata, variable = getData(array)
cekVar = cekArrVar(variable)

if comment and cekVar:
  replace(array,angka,kata,variable)
  cykAlgo(array)
else:
  print("Syntax error")