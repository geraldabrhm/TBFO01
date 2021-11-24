terminals = ["pass", "continue", "break", "if", "elif", "else", "while", "for", "in", "range", "from", "import", "as", "def", "with", "class", "or", "and", "is", "None", "(", ")", ",", ":", "not", "True", "False", "return", "==", "<=", ">=", "!=", "<", ">", "<>", "+", "-", "*", "/", "**", "//", "%", "&", "|", "^", "~", "<<", ">>", "=", "+=", "-=", "*=", "/=", "**=", "//=", "%=", "&=", "|=", "^=", ">>=", "<<=", "."]

def cekAngka(char):
    if (ord(char)>=48) and (ord(char)<=57):
        return True
    else:
        return False

def cekLower(char):
    if (ord(char)>=97) and (ord(char)<=122):
        return True
    else:
        return False

def cekUpper(char):
    if (ord(char)>=65) and (ord(char)<=90):
        return True
    else:
        return False

def cekVariabel(variable):
    benar = True
    var = list(variable)
    i = 0
    while (benar == True) and (i<len(var)):
        if i == 0:
            if (not cekUpper(var[i])) and (not cekLower(var[i])) and (ord(var[i]) != 95):
              benar = False
        else:
            if (not cekUpper(var[i])) and (not cekLower(var[i])) and (not cekAngka(var[i])) and (ord(var[i]) != 95):
                benar = False
        i += 1
    return benar

# Split colon dengan spasi
def splitColon (array):
  j = 0
  for content in array:
    i = 0
    for char in content:
      if char == ":" and i != 0:
        temp = array[j]
        cut = content[:i]
        colon = content[i:i+1]
        tail = content[i+1:]
        array.insert(j,cut)
        array.insert(j+1,colon)
        if tail != '':
          array.insert(j+2,tail)
        array.remove(temp)
        break
      i += 1
    j += 1
  return array

# Split kurung buka dengan spasi
def splitKurungBuka (array):
  j = 0
  for content in array:
    i = 0
    for char in content:
      if char == "(" and i != 0:
        temp = array[j]
        cut = content[:i]
        buka = content[i:i+1]
        tail = content[i+1:]
        array.insert(j,cut)
        array.insert(j+1,buka)
        if tail != '':
          array.insert(j+2,tail)
        array.remove(temp)
        break
      i += 1
    j += 1
  return array

# Split kurung tutup dengan spasi
def splitKurungTutup (array):
  j = 0
  for content in array:
    i = 0
    for char in content:
      if char == ")" and i != 0:
        temp = array[j]
        cut = content[:i]
        tutup = content[i:i+1]
        tail = content[i+1:]
        array.insert(j,cut)
        array.insert(j+1,tutup)
        if tail != '':
          array.insert(j+2,tail)
        array.remove(temp)
        break
      i += 1
    j += 1
  return array

# Split koma dengan spasi
def splitKoma (array):
  j = 0
  for content in array:
    i = 0
    for char in content:
      if char == "," and i != 0:
        temp = array[j]
        cut = content[:i]
        tutup = content[i:i+1]
        tail = content[i+1:]
        array.insert(j,cut)
        array.insert(j+1,tutup)
        if tail != '':
          array.insert(j+2,tail)
        array.remove(temp)
        break
      i += 1
    j += 1
  return array

# Split titik dengan spasi
def splitTitik (array):
  j = 0
  for content in array:
    i = 0
    for char in content:
      if char == "." and i != 0:
        temp = array[j]
        cut = content[:i]
        tutup = content[i:i+1]
        tail = content[i+1:]
        array.insert(j,cut)
        array.insert(j+1,tutup)
        if tail != '':
          array.insert(j+2,tail)
        array.remove(temp)
        break
      i += 1
    j += 1
  return array

def cutMid(array,start,end):
  return array[:start] + array[end+1:]

#Hapus multiline comment
def delComment(array):
  benar = True
  first = -1
  second = -1
  i = 0
  for content in array:
    if content == "'''" and first == -1 and second == -1:
      first = i
    elif content == "'''" and first != -1 and second == -1:
      second = i
    i += 1
  if first != -1 and second != -1:
    array = cutMid(array,first,second)
  elif first == -1 and second != -1:
    benar = False
  elif first != -1 and second == -1:
    benar = False
  return array, benar

#pindah nonterm ke array sendiri
def getNonTerm(array):
  NonTerm = []
  i = 0 
  for content in array:
    if not (content in terminals):
      NonTerm.insert(i,content)
      i += 1
  return NonTerm

#pindah integer ke array sendiri
def getInt(array):
  angka = []
  i = 0
  for content in array:
    j = 0
    benar = True
    while benar and j<len(content):
      if (not cekAngka(content[j])):
        benar = False
      j += 1
    if benar:
      angka.insert(i,content)
      i += 1
  return angka

#pindah float ke array sendiri
def getFloat(array):
  desimal = []
  i = 0
  for content in array:
    j = 0
    ctr = 0
    benar = True
    while benar and j<len(content):
      if j == 0 or j == len(content)-1:
        if not cekAngka(content[j]):
          benar = False
      else:
        if (not cekAngka(content[j])) and content[j] != '.':
          benar = False
        if content[j] == '.':
          ctr += 1
      j += 1
    
    if benar and ctr == 1:
      desimal.insert(i,content)
      i += 1

  return desimal

#pindah string ke array sendiri
def getString(array):
  string = []
  i = 0
  for content in array:
    if content[0] == '"' and content[len(content)-1] == '"':
      string.insert(i,content)
      i += 1
    elif content[0] == "'" and content[len(content)-1] == "'":
      string.insert(i,content)
      i += 1
  return string

#pindah variable ke array sendiri
def getVariable(array,angka,kata):
  variable = []
  i = 0
  for content in array:
    if (not content in angka) and (not content in kata):
      variable.insert(i,content)
      i += 1
  return variable

def cekArrVar(array):
  for content in array:
    if not cekVariabel(content):
      return False
  return True

def getData(array):
  NonTerm = getNonTerm(array)
  angka = getInt(NonTerm)
  kata = getString(NonTerm)
  desimal = getFloat(NonTerm)
  angka = angka + desimal
  variable = getVariable(NonTerm,angka,kata)
  return angka,kata,variable

def split (array):
  array = splitColon(array)
  array = splitKurungBuka(array)
  array = splitKurungTutup(array)
  array = splitKoma(array)
  array = splitTitik(array)
  return array

def replace(non_term,angka,string,variable):
  i = 0
  for content in non_term:
    if content in angka:
      non_term[i] = 'num'
    elif content in variable:
      non_term[i] = 'var'
    elif content in string:
      non_term[i] = 'word'
    i += 1
  return non_term