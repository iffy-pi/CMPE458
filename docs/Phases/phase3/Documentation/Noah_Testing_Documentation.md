
## Procedure

All of the files being tested in this document are located under 'test/phase-3/noah'.

## `case` statement

The changes made to the case statement in this semantic phase only concern the generation of the else clause after the case. Otherwise, the same behaviour as PT Pascal is mimicked with the new syntax in the previous phase of the compiler.

Following is the output from the file 'case_1.pt' that shows a valid example of a case statement and its output using the Quby compiler.
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
.tCaseBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tCaseSelect
oEmitNullAddress
% value emitted -32767
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 8
.tLiteralInteger
oEmitValue
% value emitted 7
.tAssignInteger
.tCaseMerge
oEmitNullAddress
% value emitted -32767
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 8
.tLiteralInteger
oEmitValue
% value emitted 8
.tAssignInteger
.tCaseMerge
oEmitNullAddress
% value emitted -32767
.tCaseEnd
.tCaseElse
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 8
.tLiteralInteger
oEmitValue
% value emitted 9
.tAssignInteger
.tCaseMerge
oEmitNullAddress
% value emitted -32767
oEmitCaseBranchTable
% value emitted 6
% value emitted 7
% value emitted 19
% value emitted 31
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

This as we can see, is very similar to the output of the similar PTPascal test file, 'pt_case_1.pt', with the notable exception of the `.tCaseElse` and all corresponding functionality after the `.tCaseEnd` token.
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
.tCaseBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tCaseSelect
oEmitNullAddress
% value emitted -32767
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 8
.tLiteralInteger
oEmitValue
% value emitted 8
.tAssignInteger
.tCaseMerge
oEmitNullAddress
% value emitted -32767
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 8
.tLiteralInteger
oEmitValue
% value emitted 9
.tAssignInteger
.tCaseMerge
oEmitNullAddress
% value emitted -32767
.tCaseEnd
oEmitCaseBranchTable
% value emitted 6
% value emitted 7
% value emitted 17
% value emitted 27
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

## `do` statement

Unlike a lot of the other statements, the new `do` statement in Quby doesn't have a direct correlary in PTPascal. The most similar thing that we can compare it to is a `while` loop.

The below output token stream is from the test file 'do_1.pt'.
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
.tDoBegin
.tDoBreakIf
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tLiteralInteger
oEmitValue
% value emitted 42
.tLT
.tDoTest
oEmitNullAddress
% value emitted -32767
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tLiteralInteger
oEmitValue
% value emitted 1
.tAdd
.tAssignInteger
.tDoEnd
% value emitted 22
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

This output is exactly as expected. The do statement starts with the emission of a `.tDoBegin` and the `break if` statements are bounded by `.tDoBreakIf` and `.tDoTest`. To finish it off, the loop is ended with a `.tDoEnd`. A similar PTPascal example with a while loop is present in 'pt_do_1.pt'. The output when compiled with the PTPascal compiler is shown below.


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
.tWhileBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tLiteralInteger
oEmitValue
% value emitted 42
.tLT
.tWhileTest
oEmitNullAddress
% value emitted -32767
.tAssignBegin
.tLiteralAddress
oEmitValue
% value emitted 4
.tLiteralAddress
oEmitValue
% value emitted 4
.tFetchInteger
.tLiteralInteger
oEmitValue
% value emitted 1
.tAdd
.tAssignInteger
.tWhileEnd
% value emitted 20
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

This is very similar to the `do` example with some exceptions. In this example, a `.tWhileBegin` and `.tWhileEnd` bound the loop. As well the condition is only followed by a T-Code token `.tWhileTest` instead of being bounded on either side since its position is predictable in regular PTPascal while loops. This correlary shows that the do loop is indeed outputting the correct tokens for the semantic phase.

## Multiple constant declarations

In Quby, defining multiple constants using a single constant keyword (now `val` instead of `const`) is disallowed. The modification to this rule was successful as we can see that the regular single constant per definition works as shown in 'constants_1.pt'. The following is the output:

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


Meanwhile, as expected, declaring multiple constants in one line does not work as can be shown in 'bad_constants_1.pt'. Running this file with the Quby compiler fails with `#eUndefinedIdentifier` since the subsequent identifier in the same line is no longer valid.

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
#eUndefinedIdentifier
.tLiteralInteger
oEmitValue
% value emitted 10
.tAssignInteger
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

## Ternary operator

The ternary operator is an entirely new addition to Quby. This operator deals with subscripting a string.