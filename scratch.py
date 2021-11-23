from cyk import terminals
'''
return
True
False
not
is
or
and
class
with
as
def
for
in 
range
while
if
elif
else
import
from
break
continue
pass
'''
R = {
    "SEC" : [["IF","SEC"], ["DEF","SEC"], ["IMPORT","SEC"], ["WITH","SEC"], ["CLASS","SEC"], ["WHILE","SEC"], ["FOR","SEC"], ["IFF","IFTAIL"], ["IFF","STATEMENT"], ["DEF_VARIABLE_PARAM","STATEMENT_RETURN"], ["DEF_VARIABLE_PARAM","STATEMENT"], ["FROM_IMPORT_VARIABLE","AS"], ["FROM","IMPORT_VARIABLE"], ["IMPORT_VARIABLE","AS"], ["IMPORTT","VARIABLE"], ["WITH_FUNCTION_AS_VARIABLE:","STATEMENT"], ["CLASS_VARIABLE_PARAM","SECCLASS"], ["WHILEF","CONTENTLOOP"], ["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"]],
    "STATEMENT" : [["PASS","STATEMENT"], ["FUNCTIONCALL","STATEMENT"], ["ASSIGNMENT","STATEMENT"], ["IF","STATEMENT"], ["WHILE","STATEMENT"], ["FOR","STATEMENT"], ["VARIABLE_ASSIGN","VALUE"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"], ["IFF","IFTAIL"], ["IFF","STATEMENT"], ["WHILEF","CONTENTLOOP"], ["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"], ["pass"]],
    "CONTENTLOOP" : [["PASS","CONTENTLOOP"], ["FUNCTIONCALL","CONTENTLOOP"], ["ASSIGNMENT","CONTENTLOOP"], ["IF","CONTENTLOOP"], ["WHILE","CONTENTLOOP"], ["FOR","CONTENTLOOP"], ["BREAK","CONTENTLOOP"], ["CONTINUE","CONTENTLOOP"], ["VARIABLE_ASSIGN"," VALUE"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE"," ()"], ["IFF","IFTAIL"], ["IFF","STATEMENT"], ["WHILEF","CONTENTLOOP"], ["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"], ["pass"], ["break"], ["continue"]],
    "FUNCTIONCALL" : [["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"]],
    "(ARGUMENTSOFFUNCCALL)" : [["OPENARGUMENTSOFFUNCCALL","CLOSE"]],
    "(ARGUMENTSOFFUNCCALL" : [["OPEN","ARGUMENTSOFFUNCCALL"]],
    "ARGUMENTSOFFUNCCALL" : [["DATA","LOOPFUNC"], ["None","LOOPFUNC"], ["word","LOOPFUNC"], ["num"], ["var"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["NOTT","(BOOLEAN)"], ["NOTT","BOOLEAN"], ["NOTT","(BOOLEANBASE)"], ["NOTT","BOOLEANBASE"], ["(BOOLEAN","CLOSE"], ["(BOOLEANBASE","CLOSE"], ["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["True"], ["False"]],
    "LOOPFUNC" : [["COMMA_DATA","LOOPFUNC"], ["COMMA","DATA"], ["COMMA","None"], ["COMMA","word"]],
    "COMMA_DATA" : [["COMMA","DATA"], ["COMMA","None"], ["COMMA","word"]],
    "ARGUMENTSOFFUNC" : [["VARIABLE","LOOPFUNCDEF"], ["var"]],
    "LOOPFUNCDEF" : [["COMMA_VARIABLE","LOOPFUNCDEF"]],
    "COMMA_VARIABLE"  : [["COMMA","VARIABLE"]],
    "DATA" : [["num"], ["var"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["NOTT","(BOOLEAN)"], ["NOTT","BOOLEAN"], ["NOTT","(BOOLEANBASE)"], ["NOTT","BOOLEANBASE"], ["(BOOLEAN","CLOSE"], ["(BOOLEANBASE","CLOSE"], ["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["True"], ["False"]],
    "ASSIGNMENT" : [["VARIABLE_ASSIGN","VALUE"]],
    "VARIABLE_ASSIGN" : [["VARIABLE","ASSIGN"]],
    "RETURN" : [["RET","R_LOOP"], ["RET","DATA"], ["RET","None"], ["RET","word"]],
    "R_LOOP" : [["DATA","LOOPRET"], ["None","LOOPRET"], ["word","LOOPRET"]],
    "LOOPRET" : [["COMMA","R_LOOP"], ["COMMA","DATA"], ["COMMA","None"], ["COMMA","word"]],
    "RET" : [["return"]],
    "OPERATOR" : [["=="], ["<="], [">="], ["!="], ["<"], [">"], ["<>"], ["+"], ["-"], ["*"], ["/"], ["**"], ["//"], ["%"], ["&"], ["|"], ["^"], ["~"], ["<<"], [">>"]],
    "LOGIC" : [["=="], ["<="], [">="], ["!="], ["<"], [">"], ["<>"]],
    "ASSIGN" : [["="], ["+="], ["-="], ["*="], ["/="], ["**="], ["//="], ["%="], ["&="], ["|="], ["^="], [">>="], ["<<="]],
    "VALUE" : [["DATA_OPERATOR","DATA"], ["DATA_OPERATOR","word"], ["num"], ["var"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["NOTT","(BOOLEAN)"], ["NOTT","BOOLEAN"], ["NOTT","(BOOLEANBASE)"], ["NOTT","BOOLEANBASE"], ["(BOOLEAN","CLOSE"], ["(BOOLEANBASE","CLOSE"], ["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["True"], ["False"]],
    "DATA_OPERATOR" : [["DATA","OPERATOR"]],
    "BOOLEANBASE" : [["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"], ["True"], ["False"], ["NOT_(DATA)_LOGIC","NOT_(DATA)"], ["(DATA)_LOGIC","NOT_(DATA)"], ["NOT_(DATA)_LOGIC","(DATA)"], [" (DATA)_LOGIC","(DATA)"], ["NOT_DATA_LOGIC","NOT_(DATA)"], ["NOT_DATA_LOGIC","(DATA)"], ["DATA_LOGIC","NOT_(DATA)"], ["DATA_LOGIC","(DATA)"], ["NOT_(DATA)_LOGIC","NOT_DATA"], ["(DATA)_LOGIC","NOT_DATA"], ["NOT_(DATA)_LOGIC","DATA"], ["NOT_(DATA)_LOGIC","None"], ["NOT_(DATA)_LOGIC","word"], ["(DATA)_LOGIC","DATA"], ["(DATA)_LOGIC","None"], ["(DATA)_LOGIC","word"], [" NOT_DATA_LOGIC","NOT_DATA"], ["DATA_LOGIC","NOT_DATA"], ["NOT_DATA_LOGIC","DATA"], ["NOT_DATA_LOGIC","None"], ["NOT_DATA_LOGIC","word"], ["DATA_LOGIC","DATA"], ["DATA_LOGIC","None"], ["DATA_LOGIC","word"], ["var"]],
    "NOT_(DATA)_LOGIC" : [["NOT_(DATA)","LOGIC"]],
    "NOT_DATA_LOGIC" : [["NOT_DATA","LOGIC"]],
    "(DATA)_LOGIC" : [["(DATA)","LOGIC"]],
    "DATA_LOGIC" : [["DATA","LOGIC"]],
    "NOT_(DATA)" : [["NOTT","(DATA)"]],
    "NOT_DATA" : [["NOTT","DATA"]],
    "(DATA)" : [["(DATA","CLOSE"]],
    "(DATA" : [["OPEN","DATA"], ["OPEN","None"], ["OPEN","word"]],
    "BOOLEAN" : [["NOTT","(BOOLEAN)"], ["NOTT","BOOLEAN"], ["NOTT","(BOOLEANBASE)"], ["NOTT","BOOLEANBASE"], ["(BOOLEAN","CLOSE"], ["(BOOLEANBASE","CLOSE"], ["VARIABLE_IS","NOT_VARIABLE"], ["VARIABLE_IS","(NOT VARIABLE)"], ["VARIABLE_IS","VARIABLE"], ["VARIABLE_IS","(VARIABLE)"], ["BOOLEAN_ORAND","BOOLEAN"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE","()"],["True"], ["False"], ["NOT_(DATA)_LOGIC","NOT_(DATA)"], ["(DATA)_LOGIC","NOT_(DATA)"], ["NOT_(DATA)_LOGIC","(DATA)"], [" (DATA)_LOGIC","(DATA)"], ["NOT_DATA_LOGIC","NOT_(DATA)"], ["NOT_DATA_LOGIC","(DATA)"], ["DATA_LOGIC","NOT_(DATA)"], ["DATA_LOGIC","(DATA)"], ["NOT_(DATA)_LOGIC","NOT_DATA"], ["(DATA)_LOGIC","NOT_DATA"], ["NOT_(DATA)_LOGIC","DATA"], ["NOT_(DATA)_LOGIC","None"], ["NOT_(DATA)_LOGIC","word"], ["(DATA)_LOGIC","DATA"], ["(DATA)_LOGIC","None"], ["(DATA)_LOGIC","word"], [" NOT_DATA_LOGIC","NOT_DATA"], ["DATA_LOGIC","NOT_DATA"], ["NOT_DATA_LOGIC","DATA"], ["NOT_DATA_LOGIC","None"], ["NOT_DATA_LOGIC","word"], ["DATA_LOGIC","DATA"], ["DATA_LOGIC","None"], ["DATA_LOGIC","word"], ["var"]],
    "(BOOLEANBASE)" : [["(BOOLEANBASE","CLOSE"]],
    "(BOOLEANBASE" : [["OPEN","BOOLEANBASE"]],
    "(BOOLEAN)" : [["(BOOLEAN","CLOSE"]],
    "(BOOLEAN" : [["OPEN","BOOLEAN"]],
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
    "CLOSE" :[[" )"]],
    "COLON" : [[":"]],
    "COMMA" :[[" ,"]],
    "()" : [["OPEN","CLOSE"]],
    "CLASS" : [["CLASS_VARIABLE_PARAM","SECCLASS"]],
    "SECCLASS" : [["DEF","SECCLASS"], ["STATEMENT","SECCLASS"], ["DEF_VARIABLE_PARAM","STATEMENT_RETURN"], ["DEF_VARIABLE_PARAM","STATEMENT"], ["PASS","STATEMENT"], ["FUNCTIONCALL","STATEMENT"], ["ASSIGNMENT","STATEMENT"], ["IF","STATEMENT"], ["WHILE","STATEMENT"], ["FOR","STATEMENT"], ["VARIABLE_ASSIGN","VALUE"], ["VARIABLE","(ARGUMENTSOFFUNCCALL)"], ["VARIABLE"," ()"], ["IFF","IFTAIL"], ["IFF","STATEMENT"], ["WHILEF","CONTENTLOOP"], ["FOR_VARIABLE_IN_SEQUENCE",":CONTENTLOOP"], ["pass"]],
    "CLASS_VARIABLE_PARAM" : [["CLASS_VARIABLE","PARAM"]],
    "CLASS_VARIABLE" : [["CLASST","var"]],
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
    "R_PARAM" : [["(INT","CLOSE"], ["(INT,","INT)"], ["(INT,INT,","INT)"]],
    "(INT,INT" : [["(INT,","INT"]],
    "(INT," : [["(INT","COMMA"]],
    "(INT" : [["OPEN","INT"]],
    "INT)"  : [["INT","CLOSE"]],
    "FORT" : [["for"]],
    "IN" : [["in"]],
    "RANGE" : [["range"]],
    "WHILE" : [["WHILEF","CONTENTLOOP"]],
    "WHILEF" : [["WHILET","CONDITION"]],
    "CONDITION" : [["(BOOLEAN)","COLON"], ["BOOLEAN COLON"]],
    "(BOOLEAN)" : [["(BOOLEAN","CLOSE"]],
    "(BOOLEAN" : [["OPEN","BOOLEAN"]],
    "WHILET" : [["while"]],
    "IF" : [["IFF","IFTAIL"], ["IFF","STATEMENT"]],
    "BRANCH" : [["ELIFF","IFTAIL"], ["ELSEF","STATEMENT"]],
    "IFTAIL" : [["STATEMENT","BRANCH"]],
    "IFF" : [["IFT","CONDITION"]],
    "ELIFF" : [["ELIFT","CONDITION"]],
    "ELSEF" : [["ELSET","CONDITION"]],
    "IFT" : [["if"]],
    "ELIFT" : [["elif"]],
    "ELSET" : [["elif","else"]],
    "IMPORT" : [["FROM_IMPORT_VARIABLE","AS"], ["FROM","IMPORT_VARIABLE"], ["IMPORT_VARIABLE","AS"], ["IMPORTT","VARIABLE"]],
    "FROM_IMPORT_VARIABLE" : [["FROM","IMPORT_VARIABLE"]], 
    "IMPORT_VARIABLE" : [["IMPORTT","VARIABLE"]], 
    "AS" : [["AST","VARIABLE"]], 
    "FROM" : [["FROMT", "VARIABLE"]],
    "AST" : [["as"]],
    "FROMT" : [["from"]],
    "IMPORTT" : [["import"]],
    "BREAK" :  [["break"]],
    "CONTINUE" :  [["continue"]],
    "PASS" :  [["pass"]],
    "VARIABLE" : [["var"]],
    "STRING" : [["word"]],
    "INT" : [["num"]]
}