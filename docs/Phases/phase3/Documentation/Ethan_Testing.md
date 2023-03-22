# Ethan Testing Documentation

## Procedure Scope Changes
As shown below, the changes made to the symbol table operations and block rule were effective. Scopes are pushed and pulled properly.
The source file for testing the block rule for procedures is `block_statement.pt`, located in `ptsrc/test/phase-3/ethan`.
```
 oSymbolStkPush(syProcedure)
 oSymbolTblPushScope
 oCountPush(three)
  oSymbolStkPushLocalIdentifier
  oSymbolStkSetKind(syVariable)
  oTypeStkPush(tpFile)
  oTypeStkLinkToStandardType(stdText)
  oSymbolStkEnterTypeReference
  oValuePush(two)
   .tFileDescriptor
   oAllocateAlignOnWord
   oSymbolStkEnterDataAddress
   .tLiteralInteger
   oEmitValue
   % value emitted 2
   .tFileBind
   .tLiteralAddress
   oEmitDataAddress
   % value emitted 0
   .tStoreInteger
   oAllocateDescriptor
  oSymbolTblEnter
  oSymbolStkPop
  oTypeStkPop
  oValuePop
 oCountPop
   oSymbolStkPushLocalIdentifier
   oSymbolStkSetKind(syConstant)
    oTypeStkPush(tpInteger)
    oTypeStkLinkToStandardType(stdInteger)
    oValuePushInteger
   oSymbolStkEnterTypeReference
   oTypeStkPop
   oSymbolStkEnterValue
   oValuePop
   oSymbolTblEnter
   oSymbolStkPop
   oSymbolStkPushLocalIdentifier
   oSymbolStkSetKind(syConstant)
    oTypeStkPush(tpInteger)
    oTypeStkLinkToStandardType(stdInteger)
    oValuePushInteger
   oSymbolStkEnterTypeReference
   oTypeStkPop
   oSymbolStkEnterValue
   oValuePop
   oSymbolTblEnter
   oSymbolStkPop
   oSymbolStkPushLocalIdentifier
   oSymbolStkSetKind(syProcedure)
   .tSkipProc
   oFixPushForwardBranch
   oEmitNullAddress
   % value emitted -32767
   oValuePushCodeAddress
   oSymbolStkEnterValue
   oValuePop
   oTypeStkPush(tpNull)
   oTypeStkSetRecursionFlag(yes)
   oTypeTblEnter
   oSymbolStkEnterTypeReference
   oSymbolTblEnter
   oSymbolTblPushScope
    oCountPush(zero)
    oCountIncrement
    oSymbolStkPushLocalIdentifier
    oSymbolStkSetKind(syVariable)
     oSymbolStkPushIdentifier
     oTypeStkPushSymbol
     oSymbolStkPop
     oSymbolStkEnterTypeReference
      oAllocateAlignOnWord
      oSymbolStkEnterDataAddress
      oAllocateVariable
     oSymbolTblEnter
    oCountIncrement
    oSymbolStkPushLocalIdentifier
    oSymbolStkSetKind(syVariable)
     oSymbolStkPushIdentifier
     oTypeStkPushSymbol
     oSymbolStkPop
     oSymbolStkEnterTypeReference
      oAllocateAlignOnWord
      oSymbolStkEnterDataAddress
      oAllocateVariable
     oSymbolTblEnter
    oCountIncrement
    oSymbolStkPushLocalIdentifier
    oSymbolStkSetKind(syVarParameter)
     oSymbolStkPushIdentifier
     oTypeStkPushSymbol
     oSymbolStkPop
     oSymbolStkEnterTypeReference
      oAllocateAlignOnWord
      oSymbolStkEnterDataAddress
      oAllocateVarParameter
     oSymbolTblEnter
      oValuePushCount
      oCountPushValue
      oValuePop
     .tLiteralAddress
     oValuePushSymbol
     oEmitValue
     % value emitted 12
     oValuePop
     .tStoreAddress
     oSymbolStkPop
     oTypeStkPop
     oCountDecrement
     .tLiteralAddress
     oValuePushSymbol
     oEmitValue
     % value emitted 8
     oValuePop
      .tStoreInteger
     oSymbolStkPop
     oTypeStkPop
     oCountDecrement
     .tLiteralAddress
     oValuePushSymbol
     oEmitValue
     % value emitted 4
     oValuePop
      .tStoreInteger
     oSymbolStkPop
     oTypeStkPop
     oCountDecrement
     oCountPop
     .tParmEnd
     oTypeStkEnterParameterCount
     oCountPop
     oCountPush(one)
     oSymbolStkPushLocalIdentifier
       oSymbolStkPushIdentifier
       oTypeStkPushSymbol
       oSymbolStkPop
     oValuePushCount
     oCountPushValue
      oCountDecrement
      oSymbolStkSetKind(syVariable)
       oAllocateAlignOnWord
       oSymbolStkEnterDataAddress
       oAllocateVariable
      oSymbolStkEnterTypeReference
      oSymbolTblEnter
     oCountPop
     oValuePop
     oTypeStkPop
     oCountDecrement
     oSymbolStkPop
     oCountPop
     oSymbolStkPushIdentifier
     .tAssignBegin
      .tLiteralAddress
      oValuePushSymbol
      oEmitValue
      % value emitted 16
      oValuePop
      oTypeStkPushSymbol
       oSymbolStkPushIdentifier
        .tLiteralAddress
        oValuePushSymbol
        oEmitValue
        % value emitted 4
        oValuePop
        oTypeStkPushSymbol
        .tFetchInteger
      oTypeStkSwap
      .tAssignInteger
     oTypeStkPop
     oSymbolStkPop
     oTypeStkPop
     oSymbolStkPop
   oTypeStkSetRecursionFlag(no)
   oTypeTblUpdate
   oTypeStkPop
   oSymbolTblUpdate
   oSymbolStkPop
   oSymbolTblPopScope
   oSymbolTblPreserveParameters
   .tProcedureEnd
   oFixPopForwardBranch
   oSymbolStkPushLocalIdentifier
   oSymbolStkSetKind(syPublicProcedure)
   .tSkipProc
   oFixPushForwardBranch
   oEmitNullAddress
   % value emitted -32767
   oValuePushCodeAddress
   oSymbolStkEnterValue
   oValuePop
   oTypeStkPush(tpNull)
   oTypeStkSetRecursionFlag(yes)
   oTypeTblEnter
   oSymbolStkEnterTypeReference
   oSymbolTblEnter
   oSymbolTblPushScope
    oCountPush(zero)
      oValuePushCount
      oCountPushValue
      oValuePop
     oCountPop
     .tParmEnd
     oTypeStkEnterParameterCount
     oCountPop
     oCountPush(one)
     oSymbolStkPushLocalIdentifier
       oSymbolStkPushIdentifier
       oTypeStkPushSymbol
       oSymbolStkPop
     oValuePushCount
     oCountPushValue
      oCountDecrement
      oSymbolStkSetKind(syVariable)
       oAllocateAlignOnWord
       oSymbolStkEnterDataAddress
       oAllocateVariable
      oSymbolStkEnterTypeReference
      oSymbolTblEnter
     oCountPop
     oValuePop
     oTypeStkPop
     oCountDecrement
     oSymbolStkPop
     oCountPop
   oTypeStkSetRecursionFlag(no)
   oTypeTblUpdate
   oTypeStkPop
   oSymbolTblUpdate
   oSymbolStkPop
   oSymbolTblPopScope
   oSymbolTblPreserveParameters
   .tProcedureEnd
   oFixPopForwardBranch
 oSymbolTblPopScope
 oSymbolStkPop
 .tTrapBegin
 .tTrap
 oEmitTrapKind(trHalt)
 % value emitted 0
```

## String Index Operator
This section corresponds to the String Index operator (?). Testing is completed for string literals and variables, and for semantically correct and incorrect source code.

### Literals
#### Semantically Correct Test
Below is the output for a semantically correct String Index operation on two string literals, in source file `sti_lit_valid.pt`.
As can be seen in the tokens emitted, the assignment is properly recognized as semantically correct.
```
.tFileDescriptor
.tLiteralInteger
oEmitValue
% value emitted 2
.tFileBind
.tLiteralAddress
oEmitDataAddress
% value emitted 0
.tStoreInteger
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tLiteralString
oEmitString
% value emitted 72
% value emitted 101
% value emitted 108
% value emitted 108
% value emitted 111
% value emitted 32
% value emitted 116
% value emitted 104
% value emitted 101
% value emitted 114
% value emitted 101
.tLiteralString
oEmitString
% value emitted 116
% value emitted 104
% value emitted 101
.tIndex
.tAssignInteger
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```
#### Semantically Incorrect Test
Below is the error output for a semantically incorrect String Index operation on a string literal and an integer literal, in source file `sti_lit_invalid.pt`.
The compiler correctly identifies that the String Index operation cannot be performed between an integer and a string.
```
semantic error, line 5: operand and operator types clash
```

### Variables
#### Semantically Correct Test
Below is the output for a semantically correct String Index operation on two string variables assigned to an integer variable, in source file `sti_var_valid.pt`.
As can be seen in the tokens emitted, the assignment operation is properly recognized as semantically correct.
```
.tFileDescriptor
.tLiteralInteger
oEmitValue
% value emitted 2
.tFileBind
.tLiteralAddress
oEmitDataAddress
% value emitted 0
.tStoreInteger
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tLiteralString
oEmitString
% value emitted 72
% value emitted 101
% value emitted 108
% value emitted 108
% value emitted 111
% value emitted 32
% value emitted 116
% value emitted 104
% value emitted 101
% value emitted 114
% value emitted 101
.tAssignString
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 1028
.tLiteralString
oEmitString
% value emitted 116
% value emitted 104
% value emitted 101
.tAssignString
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 2052
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchString
.tLiteralAddress
oEmitValue
% value emitted 1028
.tFetchString
.tIndex
.tAssignInteger
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```
#### Semantically Incorrect Test
Below is the error output for a semantically incorrect String Index operation on a string variable and an integer constant to an integer variable, in source file `sti_var_invalid.pt`.
The compiler correctly identifies that the String Index operation cannot be performed between an integer and a string.
```
semantic error, line 10: operand and operator types clash
```

## String Concatenation
This section corresponds to String Concatenation. Testing is completed for string literals and variables, and for semantically correct and incorrect source code.

### Literals
#### Semantically Correct Test
Below is the output for a semantically correct string concatenation on two string literals, in source file `stcat_lit_valid.pt`.
As can be seen in the tokens emitted, the concatenation and assignment is properly recognized as semantically correct.
```
.tFileDescriptor
.tLiteralInteger
oEmitValue
% value emitted 2
.tFileBind
.tLiteralAddress
oEmitDataAddress
% value emitted 0
.tStoreInteger
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tLiteralString
oEmitString
% value emitted 72
% value emitted 101
% value emitted 108
% value emitted 108
% value emitted 111
% value emitted 32
.tLiteralString
oEmitString
% value emitted 87
% value emitted 111
% value emitted 114
% value emitted 108
% value emitted 100
.tConcatenate
.tAssignString
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```
#### Semantically Incorrect Test
Below is the error output for a semantically incorrect string concatenation on a string literal and an integer literal, in source file `stcat_lit_invalid.pt`.
The compiler correctly identifies that an integer and a string cannot be added.
```
semantic error, line 5: type clash
```

### Variables
#### Semantically Correct Test
Below is the output for a semantically correct string concatenation on two string variables assigned to an integer variable, in source file `stcat_var_valid.pt`.
As can be seen in the tokens emitted, the concatenation and assignment is properly recognized as semantically correct.
```
.tFileDescriptor
.tLiteralInteger
oEmitValue
% value emitted 2
.tFileBind
.tLiteralAddress
oEmitDataAddress
% value emitted 0
.tStoreInteger
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tLiteralString
oEmitString
% value emitted 72
% value emitted 101
% value emitted 108
% value emitted 108
% value emitted 111
% value emitted 32
.tAssignString
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 1028
.tLiteralString
oEmitString
% value emitted 87
% value emitted 111
% value emitted 114
% value emitted 108
% value emitted 100
.tAssignString
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 2052
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchString
.tLiteralAddress
oEmitValue
% value emitted 1028
.tFetchString
.tConcatenate
.tAssignString
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```
#### Semantically Incorrect Test
Below is the error output for a semantically incorrect string concatenation on a string variable and an integer constant to an integer variable, in source file `stcat_var_invalid.pt`.
The compiler correctly identifies that an integer and a string cannot be added.
```
semantic error, line 10: type clash
```

## Type Definitions
### Semantically Correct Test
Below is the output for a semantically correct type definition, in source file `type_valid.pt`.
The type is correctly identified and added to the symbol table.
```
 oSymbolStkPush(syProcedure)
 oSymbolTblPushScope
 oCountPush(three)
  oSymbolStkPushLocalIdentifier
  oSymbolStkSetKind(syVariable)
  oTypeStkPush(tpFile)
  oTypeStkLinkToStandardType(stdText)
  oSymbolStkEnterTypeReference
  oValuePush(two)
   .tFileDescriptor
   oAllocateAlignOnWord
   oSymbolStkEnterDataAddress
   .tLiteralInteger
   oEmitValue
   % value emitted 2
   .tFileBind
   .tLiteralAddress
   oEmitDataAddress
   % value emitted 0
   .tStoreInteger
   oAllocateDescriptor
  oSymbolTblEnter
  oSymbolStkPop
  oTypeStkPop
  oValuePop
 oCountPop
   oSymbolStkPushLocalIdentifier
   oSymbolStkSetKind(syType)
     oSymbolStkPushIdentifier
     oTypeStkPushSymbol
     oSymbolStkPop
   oSymbolStkEnterTypeReference
   oTypeStkPop
   oSymbolTblEnter
   oSymbolStkPop
 oSymbolTblPopScope
 oSymbolStkPop
 .tTrapBegin
 .tTrap
 oEmitTrapKind(trHalt)
 % value emitted 0
 ```
### Semantically Incorrect Test
Below is the error output for a semantically incorrect type definition, in source file `type_invalid.pt`.
The compiler recognizes that only one type can be declared per definition.
```
scan/parse error, line 3: syntax error at: ,
```
