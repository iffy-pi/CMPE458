# Liam Testing Documentation

All code used for testing can be found in /ptsrc/test/phase-3/liam/

## `if elsif else` testing

In Quby, the `elsif` clause was added to if statements. By testing that the Quby and PT-pascal output the same tokens when compiling code with similar functionality allows us to ensure proper Quby functionality moving forward. The `if_test1.pt` is used with the Quby compiler and `if_test2.pt` runs with the PT-pascal compiler. 

The Quby compiler had the following output:

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
.tLiteralInteger
oEmitValue
% value emitted 1
.tAssignInteger
.tIfBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tLiteralInteger
oEmitValue
% value emitted 1
.tEQ
.tIfThen
oEmitNullAddress
% value emitted -32767
.tWriteBegin
.tTrapBegin
.tLiteralAddress
oEmitValue
% value emitted 0
.tVarParm
.tParmEnd
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tParmEnd
.tLiteralInteger
oEmitValue
% value emitted 10
.tParmEnd
.tTrap
oEmitTrapKind(trWriteInteger)
% value emitted 8
.tWriteEnd
.tTrapBegin
.tLiteralAddress
oEmitValue
% value emitted 0
.tVarParm
.tParmEnd
.tTrap
oEmitTrapKind(trWriteln)
% value emitted 6
.tIfMerge
oEmitNullAddress
% value emitted -32767
.tIfBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tLiteralInteger
oEmitValue
% value emitted 2
.tEQ
.tIfThen
oEmitNullAddress
% value emitted -32767
.tWriteBegin
.tTrapBegin
.tLiteralAddress
oEmitValue
% value emitted 0
.tVarParm
.tParmEnd
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tParmEnd
.tLiteralInteger
oEmitValue
% value emitted 10
.tParmEnd
.tTrap
oEmitTrapKind(trWriteInteger)
% value emitted 8
.tWriteEnd
.tTrapBegin
.tLiteralAddress
oEmitValue
% value emitted 0
.tVarParm
.tParmEnd
.tTrap
oEmitTrapKind(trWriteln)
% value emitted 6
.tIfEnd
.tIfEnd
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```
And the PT-pascal compiler outpetted the following:
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
.tLiteralInteger
oEmitValue
% value emitted 1
.tAssignInteger
.tIfBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tLiteralInteger
oEmitValue
% value emitted 1
.tEQ
.tIfThen
oEmitNullAddress
% value emitted -32767
.tWriteBegin
.tTrapBegin
.tLiteralAddress
oEmitValue
% value emitted 0
.tVarParm
.tParmEnd
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tParmEnd
.tLiteralInteger
oEmitValue
% value emitted 10
.tParmEnd
.tTrap
oEmitTrapKind(trWriteInteger)
% value emitted 8
.tWriteEnd
.tIfEnd
.tTrapBegin
.tLiteralAddress
oEmitValue
% value emitted 0
.tVarParm
.tParmEnd
.tTrap
oEmitTrapKind(trWriteln)
% value emitted 6
.tIfBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tLiteralInteger
oEmitValue
% value emitted 2
.tEQ
.tIfThen
oEmitNullAddress
% value emitted -32767
.tWriteBegin
.tTrapBegin
.tLiteralAddress
oEmitValue
% value emitted 0
.tVarParm
.tParmEnd
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tParmEnd
.tLiteralInteger
oEmitValue
% value emitted 10
.tParmEnd
.tTrap
oEmitTrapKind(trWriteInteger)
% value emitted 8
.tWriteEnd
.tIfEnd
.tTrapBegin
.tLiteralAddress
oEmitValue
% value emitted 0
.tVarParm
.tParmEnd
.tTrap
oEmitTrapKind(trWriteln)
% value emitted 6
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

As seen by the two outputs above, both returned similar T-tokens


## `Module` Testing

The code for testing the module can be found in the file `module_test.pt` The file tests to see if the module declarations emit the correct values and store the module identifier on the stack so it can't be used once again. 

Running the code outputted the following without errors:
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
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```


## `Public` Procedure Testing

Public procedures were a new form of procedure added to the new Quby language. Similarly to regular procedures, they emit the same T-tokens, however when placed on the symbol stack, the new `syPublicProcedure` symbol is used instead of the normally used `syProcedure` symbol. By delcaring it as a `syPublicProcedure` we can make it accessable outside of the scope of a module. 

Running the `public_procedure_test.pt` file has a module with a public function declared within it. Running semtrace on it returned the following:

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
.tSkipProc
oEmitNullAddress
% value emitted -32767
.tLiteralAddress
oEmitValue
% value emitted 4
.tStoreAddress
.tParmEnd
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchAddress
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchAddress
.tFetchInteger
#eUndefinedIdentifier
#eExpnOperandReqd
.tAdd
.tAssignInteger
.tProcedureEnd
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

Doing further inspection into each operation taking place and using the -a flag in with the semtrace script showed that the `syPublicProcedure` symbol is placed on the stack as opposed to the `syProcedure` symbol. This will allow the procedure to be used outside of the module. 



## `Multi-Variable` Declaration Testing

Multi-Variable Decleration testing used the `multi_var_declaration_test1.pt` and `multi_var_decleration_test2.pt` files and was compiled using the ptsrc-ref compiler and the quby compiler being tested. The file `multi_var_declaration_test1.pt` was ran using the quby compiler and is expected to output the same T-tokens as the `multi_var_decleration_test2.pt` file should, when compiled using PT-pascal. 

Output of test 1 file
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
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

Running the same functionality code `multi_var_decleration_test2.pt` returned the same output, showing that the multivariable declaration functionality works.

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
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```