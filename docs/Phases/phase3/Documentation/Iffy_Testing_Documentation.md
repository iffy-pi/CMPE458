# Iffy Testing Documentation
## What am I testing
Changes to semantic.ssl:
Iffy: 21 22

DONE: 2 3 4 5 7 8 20 21 

Changes to semantic.pt:
Iffy:

DONE: 2 3 5 

- Verifying the old functionality
    - Assignment of variables
    - Binary operation
    - Ternary operation
    - Unary operation
    - If statement
    - Else statement
- String handling
    - String operations
        -  DONE: String equality and inequality
        - DONE: String length operation
    - DONE: Handling string literals
    - Handling string constants
    - New string traps

- Describe semtrace and ptsemtrace



## Handling String Literals
The following section consists of tests performed to verify that Quby treats Strings as first class data types and does not differentiate Strings and chars like Pascal. This will be done using the basic string equality, which is also tested.

To verify the proper handling of string literals for Quby, programs were defined in Pascal and Quby that handled a simple equality using string literals. It will be tested against the various types of literals.

### Empty String
The file `stringops/string_lit_0_qb.pt` performs a string comparison using an empty string in Quby. `stringops/string_lit_0_pt.pt` does the same operation but in Pascal.

Performing ptsemtrace on the Pascal file, an error occurs as null/empty strings are not allowed in Pascal:

```
....
       oSymbolStkPush(syExpression)
       @StringLiteral
        oValuePushStringLength
        [ oValueChoose (zero)
        | zero:
        #eNullString
        semantic error, line 4: null literal string not allowed
        oTypeStkPush(tpChar)
        oTypeStkLinkToStandardType(stdChar)
...
```

Performing semtrace on the Quby file, a valid output token stream is gotten since null strings are allowed:

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
.tLiteralString
oEmitString
.tStringEqual
.tAssignBoolean
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

In the above output, string literals are handled with `.tLiteralString` and then the `oEmitString` semantic operation to emit the string value. This matches the handling of first-class data types in Quby, as seen by the output of `stringops/string_lit_int.pt` which performs a comparison with integer literals:

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
.tLiteralInteger % literal code
oEmitValue % emits the value
% value emitted 0
.tLiteralInteger
oEmitValue
% value emitted 1
.tEQ
.tAssignBoolean
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

### 1-Char String
The file `stringops/string_lit_1_qb.pt` performs a string comparison using a one-char string in Quby. `stringops/string_lit_1_pt.pt` does the same operation but in Pascal.

The output of ptsemtrace and semtrace on the Pascal file (left) and Quby file (right) respectively, are shown below:

![[Pasted image 20230319205514.png]]

In Pascal, one-char string literals are automatically converted to the Pascal char type. For Quby, they are seen as valid string and hence it continues to use the `tLiteralString` instead of the `tLiteralChar` used in Pascal. Furthermore, it uses `tStringEqual` instead of `tEQ` as `semantic.ssl` uses that specific T-code for string equalities.

Also note that the 97, the ASCII code for `'a'` is emitted, which is the character in the source code.

## Multi-char String
The file `stringops/string_lit_m_qb.pt` performs a string comparison using a multi-char string in Quby.

The semtrace output of this file is shown below:

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
% value emitted 97
% value emitted 98
% value emitted 99
.tLiteralString
oEmitString
% value emitted 97
% value emitted 98
% value emitted 99
.tStringEqual
.tAssignBoolean
.tTrapBegin
.tTrap
oEmitTrapKind(trH
```

Each of the string literals begin with the `tLiteralString` token followed by `oEmitString` which emits the ASCII codes for the characters in the String (97 for `a`, 98 for `b` and 99 for `c`).

## String Equality
String equality uses the special T-code `tStringEqual` instead of the standard `tEQ`, which is a change made from the Pascal semantic phase. To test this, the following files were written:

- `stringops/string_eq.pt` assigns a boolean variable the result of a simple string literal comparison (`"a" == "b"`)
- `stringops/string_eq_2.pt` assigns a boolean variable the result of a simple integer literal comparison

The output of semtrace for both files is shown below (`string_eq_2` on the left, and `string_eq` on the right):

![[Pasted image 20230319191822.png]]

As you can see in the above image, one of the differences in the output is the use of `tLiteralString` and `oEmitString` rather than the `tLiteralInteger` and `oEmitValue`. This makes sense since `string_eq` uses string literals rather than integer literals.

Furthermore, the `tStringEquals` token is used rather than the `tEQ`, showing that for String literals, the appropriate string token is used. 

The differentiation is still made when using variables instead of literals, as indicated by the semtrace shown below (Left is `stringops/string_eq_vars_2.pt` which uses integer variables, right is `stringops/string_eq_vars.pt` which uses String variables):

![[Pasted image 20230319192545.png]]

## String Inequality
String inequality is implemented by inverting the output of the `tStringEquals` operation using the `tNot` T-code. This replaces the `tNEQ` for String comparisons.

This is indicated by the semtrace shown below:
- Left: `stringops/string_neq_2.pt`, performs integer literal inequality and assigns to variable
- Right: `stringops/string_neq.pt`, performs string literal inequality and assigns to variable

![[Pasted image 20230319203414.png]]

As seen above, the string inequality emits `tNot` after the `tStringEquals` to achieve the inequality operation on strings, rather than the `tNE` operation.

## String Length
To test the semantic output of the String length operation, the file `stringops/string_len.pt` assigns the length of the string "abc" to an integer variable.

The semtrace output is shown below:

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
% value emitted 97
% value emitted 98
% value emitted 99
.tLength
.tAssignInteger
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

As seen above, the string literal is emitted first and is then followed by the `tLength` operation. Since the result type is an integer, the code `tAssignInteger` is used to assign it to an integer variable.

If the variable that is assigned to is not an integer type (as is the case in `stringops/string_len_invalid.pt`), a type clash will occur (as indicated with the `eTypeMismatch` error token):

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
% value emitted 97
% value emitted 98
% value emitted 99
.tLength
#eTypeMismatch
.tAssignBoolean
.tTrapBegin
.tTrap
oEmitTrapKind(trHalt)
% value emitted 0
```

## String Constants
In Quby, string constants are handled in the same way as string variables.

The files `stringops/string_const.pt` and `stringops/string_var.pt` declare a string constant and string variable respectively. By comparing the `semtrace` output, the specified handling of string constants can be verified.

As seen by the text comparison below, the two output streams are identical:

![[Pasted image 20230320002944.png]]


