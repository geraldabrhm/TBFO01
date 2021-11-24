from process_file import split
from process_file import delComment
from process_file import getData
from process_file import cekArrVar
from process_file import replace
from cyk import cykParser

x = input("Masukkan nama file: ")
f = open(x, "r")
isi = f.read()
array = isi.split()
array = split(array)
array, comment = delComment(array)
angka, kata, variable = getData(array)
cekVar = cekArrVar(variable)

if comment and cekVar:
  replace(array, angka, kata, variable)
  cykParser(array)
else:
  print("Syntax error")
