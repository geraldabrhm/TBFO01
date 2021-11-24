R = {
    "SEC" : [["IF","SEC"], ["DEF","SEC"], ["IMPORT","SEC"], ["WITH","SEC"], ["CLASS","SEC"], ["WHILE","SEC"], ["FOR","SEC"], ["IFF","IFTAIL"], ["IFF","STATEMENT"], ["DEF_VARIABLE_PARAM","STATEMENT_RETURN"], ["DEF_VARIABLE_PARAM","STATEMENT"], ["FROM_IMPORT_VARIABLE","AS"], ["FROM","IMPORT_VARIABLE"], ["IMPORT_VARIABLE","AS"], ["IMPORTT","VARIABLE"], ["WITH_FUNCTION_AS_VARIABLE:","STATEMENT"], ["CLASS_VARIABLE_PARAM","SECCLASS"], ["WHILEF","CONTENTLOOP"], ["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"], ["FUNCTIONCALL","STATEMENT"], ["ASSIGNMENT","STATEMENT"], ["IF","STATEMENT"], ["WHILE","STATEMENT"], ["FOR","STATEMENT"], ["VARIABLE_ASSIGN","VALUE"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"], ["VARIABLE_DOT_VARIABLE","(ARGUMENTSOFFUNCCALL)"],["VARIABLE_DOT_VARIABLE","()"]],
    "STATEMENT" : [["PASS","STATEMENT"], ["FUNCTIONCALL","STATEMENT"], ["ASSIGNMENT","STATEMENT"], ["IF","STATEMENT"], ["WHILE","STATEMENT"], ["FOR","STATEMENT"], ["VARIABLE_ASSIGN","VALUE"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"], ["VARIABLE_DOT_VARIABLE","(ARGUMENTSOFFUNCCALL)"],["VARIABLE_DOT_VARIABLE","()"], ["IFF","IFTAIL"], ["IFF","STATEMENT"], ["WHILEF","CONTENTLOOP"], ["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"], ["RET","R_LOOP"], ["RET","VALUE"], ["pass"]],
    "CONTENTLOOP" : [["PASS","CONTENTLOOP"], ["FUNCTIONCALL","CONTENTLOOP"], ["ASSIGNMENT","CONTENTLOOP"], ["IF","CONTENTLOOP"], ["WHILE","CONTENTLOOP"], ["FOR","CONTENTLOOP"], ["BREAK","CONTENTLOOP"], ["CONTINUE","CONTENTLOOP"], ["VARIABLE_ASSIGN","VALUE"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE"," ()"], ["VARIABLE_DOT_VARIABLE","(ARGUMENTSOFFUNCCALL)"],["VARIABLE_DOT_VARIABLE","()"], ["IFF","IFTAIL"], ["IFF","STATEMENT"], ["WHILEF","CONTENTLOOP"], ["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"], ["RET","R_LOOP"], ["RET","VALUE"], ["pass"], ["break"], ["continue"]],
    "FUNCTIONCALL" : [["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["VARIABLE_DOT_VARIABLE","(ARGUMENTSOFFUNCCALL)"],["VARIABLE_DOT_VARIABLE","()"]],
    "VARIABLE_DOT_VARIABLE" : [["VARIABLE","DOT_LOOP"]],
    "DOT_LOOP" : [["DOT_VARIABLE","DOT_LOOP"],["DOT","VARIABLE"]],
    "DOT_VARIABLE" : [["DOT","VARIABLE"]],
    "DOT": [["."]],
    "(ARGUMENTSOFFUNCCALL)" : [["(ARGUMENTSOFFUNCCALL","CLOSE"]],
    "(ARGUMENTSOFFUNCCALL" : [["OPEN","ARGUMENTSOFFUNCCALL"]],
    "ARGUMENTSOFFUNCCALL" : [["DATA","LOOPFUNC"], ["NONE","LOOPFUNC"], ["STRING","LOOPFUNC"], ["INT", "DOT_INT"], ["word"], ["num"], ["var"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["NOTT","(BOOLEAN)"], ["NOTT","BOOLEAN"], ["NOTT","(BOOLEANBASE)"], ["NOTT","BOOLEANBASE"], ["(BOOLEAN","CLOSE"], ["(BOOLEANBASE","CLOSE"], ["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["True"], ["False"]],
    "LOOPFUNC" : [["COMMA_DATA","LOOPFUNC"], ["COMMA","DATA"], ["COMMA","NONE"], ["COMMA","STRING"]],
    "COMMA_DATA" : [["COMMA","DATA"], ["COMMA","NONE"], ["COMMA","STRING"]],
    "ARGUMENTSOFFUNC" : [["VARIABLE","LOOPFUNCDEF"], ["var"]],
    "LOOPFUNCDEF" : [["COMMA_VARIABLE","LOOPFUNCDEF"],["COMMA","VARIABLE"]],
    "COMMA_VARIABLE"  : [["COMMA","VARIABLE"]],
    "DATA" : [["INT", "DOT_INT"], ["num"], ["var"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["NOTT","(BOOLEAN)"], ["NOTT","BOOLEAN"], ["NOTT","(BOOLEANBASE)"], ["NOTT","BOOLEANBASE"], ["(BOOLEAN","CLOSE"], ["(BOOLEANBASE","CLOSE"], ["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["True"], ["False"]],
    "ASSIGNMENT" : [["VARIABLE_ASSIGN","VALUE"]],
    "VARIABLE_ASSIGN" : [["VARIABLE","ASSIGN"]],
    "RETURN" : [["RET","R_LOOP"], ["RET","VALUE"]],
    "R_LOOP" : [["VALUE","LOOPRET"]],
    "LOOPRET" : [["COMMA","R_LOOP"], ["COMMA","VALUE"]],
    "RET" : [["return"]],
    "OPERATOR" : [["=="], ["<="], [">="], ["!="], ["<"], [">"], ["<>"], ["+"], ["-"], ["*"], ["/"], ["**"], ["//"], ["%"], ["&"], ["|"], ["^"], ["~"], ["<<"], [">>"]],
    "LOGIC" : [["=="], ["<="], [">="], ["!="], ["<"], [">"], ["<>"]],
    "ASSIGN" : [["="], ["+="], ["-="], ["*="], ["/="], ["**="], ["//="], ["%="], ["&="], ["|="], ["^="], [">>="], ["<<="]],
    "VALUE" : [["DATA_OPERATOR","VALUE"], ["DATA_OPERATOR","DATA"], ["DATA_OPERATOR","STRING"], ["INT", "DOT_INT"], ["num"], ["var"], ["word"], ["None"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["NOTT","(BOOLEAN)"], ["NOTT","BOOLEAN"], ["NOTT","(BOOLEANBASE)"], ["NOTT","BOOLEANBASE"], ["(BOOLEAN","CLOSE"], ["(BOOLEANBASE","CLOSE"], ["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["True"], ["False"]],
    "DATA_OPERATOR" : [["DATA","OPERATOR"]],
    "BOOLEANBASE" : [["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"], ["True"], ["False"], ["NOT_(DATA)_LOGIC","NOT_(DATA)"], ["(DATA)_LOGIC","NOT_(DATA)"], ["NOT_(DATA)_LOGIC","(DATA)"], [" (DATA)_LOGIC","(DATA)"], ["NOT_DATA_LOGIC","NOT_(DATA)"], ["NOT_DATA_LOGIC","(DATA)"], ["DATA_LOGIC","NOT_(DATA)"], ["DATA_LOGIC","(DATA)"], ["NOT_(DATA)_LOGIC","NOT_DATA"], ["(DATA)_LOGIC","NOT_DATA"], ["NOT_(DATA)_LOGIC","VALUE"], ["(DATA)_LOGIC","VALUE"], [" NOT_DATA_LOGIC","NOT_DATA"], ["DATA_LOGIC","NOT_DATA"], ["NOT_DATA_LOGIC","VALUE"], ["DATA_LOGIC","VALUE"], ["var"]],
    "NOT_(DATA)_LOGIC" : [["NOT_(DATA)","LOGIC"]],
    "NOT_DATA_LOGIC" : [["NOT_DATA","LOGIC"]],
    "(DATA)_LOGIC" : [["(DATA)","LOGIC"]],
    "DATA_LOGIC" : [["VALUE","LOGIC"]],
    "NOT_(DATA)" : [["NOTT","(DATA)"]],
    "NOT_DATA" : [["NOTT","VALUE"]],
    "(DATA)" : [["(DATA","CLOSE"]],
    "(DATA" : [["OPEN","VALUE"]],
    "BOOLEAN" : [["NOTT","(BOOLEAN)"], ["NOTT","BOOLEAN"], ["NOTT","(BOOLEANBASE)"], ["NOTT","BOOLEANBASE"], ["(BOOLEAN","CLOSE"], ["(BOOLEANBASE","CLOSE"], ["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["True"], ["False"], ["NOT_(DATA)_LOGIC","NOT_(DATA)"], ["(DATA)_LOGIC","NOT_(DATA)"], ["NOT_(DATA)_LOGIC","(DATA)"], [" (DATA)_LOGIC","(DATA)"], ["NOT_DATA_LOGIC","NOT_(DATA)"], ["NOT_DATA_LOGIC","(DATA)"], ["DATA_LOGIC","NOT_(DATA)"], ["DATA_LOGIC","(DATA)"], ["NOT_(DATA)_LOGIC","NOT_DATA"], ["(DATA)_LOGIC","NOT_DATA"], ["NOT_(DATA)_LOGIC","VALUE"], ["(DATA)_LOGIC","VALUE"], [" NOT_DATA_LOGIC","NOT_DATA"], ["DATA_LOGIC","NOT_DATA"], ["NOT_DATA_LOGIC","VALUE"], ["DATA_LOGIC","VALUE"], ["var"]],
    "(BOOLEANBASE)" : [["(BOOLEANBASE","CLOSE"]],
    "(BOOLEANBASE" : [["OPEN","BOOLEANBASE"]],
    "NOTT" : [["not"]],
    "IS" : [["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"]],
    "(NOT_VARIABLE)" : [["(NOT_VARIABLE","CLOSE"]],
    "(NOT_VARIABLE" : [["OPEN","NOT_VARIABLE"]],
    "NOT_VARIABLE" : [["NOTT","VARIABLE"]], 
    "VARIABLE_IS" : [["var","IST"]],
    "(VARIABLE)" : [["(VARIABLE","CLOSE"]],
    "(VARIABLE" : [["OPEN","VARIABLE"]],
    "IST" : [["is"]],
    "ORAND" : [["BOOLEAN_ORAND","BOOLEAN"]],
    "BOOLEAN_ORAND" : [["BOOLEAN","ORANDT"]],
    "ORANDT" : [["or"], ["and"]],
    "NONE" : [["None"]],
    "OPEN" : [["("]],
    "CLOSE" :[[")"]],
    "COLON" : [[":"]],
    "COMMA" :[[","]],
    "()" : [["OPEN","CLOSE"]],
    "CLASS" : [["CLASS_VARIABLE_PARAM","SECCLASS"]],
    "SECCLASS" : [["DEF","SECCLASS"], ["STATEMENT","SECCLASS"], ["DEF_VARIABLE_PARAM","STATEMENT_RETURN"], ["DEF_VARIABLE_PARAM","STATEMENT"], ["PASS","STATEMENT"], ["FUNCTIONCALL","STATEMENT"], ["ASSIGNMENT","STATEMENT"], ["IF","STATEMENT"], ["WHILE","STATEMENT"], ["FOR","STATEMENT"], ["VARIABLE_ASSIGN","VALUE"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE"," ()"],["VARIABLE_DOT_VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE_DOT_VARIABLE","()"], ["IFF","IFTAIL"], ["IFF","STATEMENT"], ["WHILEF","CONTENTLOOP"], ["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"], ["pass"]],
    "CLASS_VARIABLE_PARAM" : [["CLASS_VARIABLE","COLON"]],
    "CLASS_VARIABLE" : [["CLASST","VARIABLE"]],
    "PARAM" : [["(ARGUMENTSOFFUNC)","COLON"], ["()","COLON"]],
    "(ARGUMENTSOFFUNC)" : [["(ARGUMENTSOFFUNC","CLOSE"]],
    "(ARGUMENTSOFFUNC" : [["OPEN","ARGUMENTSOFFUNC"]],
    "CLASST" : [["class"]],
    "WITH" : [["WITH_FUNCTION_AS_VARIABLE:","STATEMENT"]],
    "WITH_FUNCTION_AS_VARIABLE:" : [["WITH_FUNCTION","AS_VARIABLE:"]],
    "WITH_FUNCTION" : [["WITHT","FUNCTIONCALL"]],
    "AS_VARIABLE:" : [["AS_VARIABLE","COLON"]],
    "AS_VARIABLE" : [["AST","VARIABLE"]],
    "WITHT" : [["with"]],
    "DEF" : [["DEF_VARIABLE_PARAM","STATEMENT_RETURN"], ["DEF_VARIABLE_PARAM","STATEMENT"]],
    "STATEMENT_RETURN" : [["STATEMENT","RETURN"]],
    "DEF_VARIABLE_PARAM" : [["DEF_VARIABLE","PARAM"]],
    "DEF_VARIABLE" : [["DEFT","VARIABLE"]],
    "DEFT" : [["def"]],
    "FOR" : [["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"]],
    "FOR_VARIABLE" : [["FORT","VARIABLE"]],
    "IN_SEQUENCE" : [["IN","SEQUENCE"]],
    "FOR_VARIABLE_IN_SEQUENCE" : [["FOR_VARIABLE","IN_SEQUENCE"]],
    ":CONTENTLOOP" : [["COLON","CONTENTLOOP"]],
    "SEQUENCE" : [["var"], ["word"], ["RANGE","R_PARAM"]],
    "R_PARAM" : [["(INT","CLOSE"], ["(INT,","INT)"], ["(INT,INT,","INT)"],["(VAR","CLOSE"],["var"]],
    "(INT,INT" : [["(INT,","INT"]],
    "(INT," : [["(INT","COMMA"]],
    "(INT" : [["OPEN","INT"]],
    "INT)"  : [["INT","CLOSE"]],
    "(VAR" : [["(","VARIABLE"]],
    "FORT" : [["for"]],
    "IN" : [["in"]],
    "RANGE" : [["range"]],
    "WHILE" : [["WHILEF","CONTENTLOOP"]],
    "WHILEF" : [["WHILET","CONDITION"]],
    "CONDITION" : [["(BOOLEAN)","COLON"], ["BOOLEAN","COLON"]],
    "(BOOLEAN)" : [["(BOOLEAN","CLOSE"]],
    "(BOOLEAN" : [["OPEN","BOOLEAN"]],
    "WHILET" : [["while"]],
    "IF" : [["IFF","IFTAIL"], ["IFF","STATEMENT"]],
    "BRANCH" : [["ELIFF","IFTAIL"], ["ELIFF","STATEMENT"], ["ELSEF","STATEMENT"]],
    "IFTAIL" : [["STATEMENT","BRANCH"]],
    "IFF" : [["IFT","CONDITION"]],
    "ELIFF" : [["ELIFT","CONDITION"]],
    "ELSEF" : [["ELSET","COLON"]],
    "IFT" : [["if"]],
    "ELIFT" : [["elif"]],
    "ELSET" : [["else"]],
    "IMPORT" : [["FROM_IMPORT_VARIABLE","AS"], ["FROM","IMPORT_VARIABLE"], ["IMPORT_VARIABLE","AS"], ["IMPORTT","VARIABLE"]],
    "FROM_IMPORT_VARIABLE" : [["FROM","IMPORT_VARIABLE"]], 
    "IMPORT_VARIABLE" : [["IMPORTT","VARIABLE"]], 
    "AS" : [["AST","VARIABLE"]], 
    "FROM" : [["FROMT","VARIABLE"]],
    "AST" : [["as"]],
    "FROMT" : [["from"]],
    "IMPORTT" : [["import"]],
    "BREAK" :  [["break"]],
    "CONTINUE" :  [["continue"]],
    "PASS" :  [["pass"]],
    "VARIABLE" : [["var"]],
    "STRING" : [["word"]],
    "INT" : [["INT", "DOT_INT"],["num"]],
    "DOT_INT" : [["DOT","NUM"]],
    "NUM" : [["num"]],
}
  

def cykParser(array):
    n = len(array)

    if n != 0:
      T = [[set([]) for j in range(n)] for i in range(n)]
      for j in range(n):
        #isi tabel [j][j]
          for lhs, rule in R.items():
              for rhs in rule:
                  if len(rhs) == 1 and rhs[0] == array[j]:
                      T[j][j].add(lhs)
        #isi sisa tabel
          for i in range(j, -1, -1):
              for k in range(i, j):
                if k+1 < n:
                  for lhs, rule in R.items():
                      for rhs in rule:
                        if (len(rhs) == 2) and (rhs[0] in T[i][k]) and (rhs[1] in T[k+1][j]):
                            T[i][j].add(lhs)

      if "SEC" in T[0][n-1]:
          print("Accepted")
      else:
          print("Syntax Error")
    else:
      print("File kosong!")
