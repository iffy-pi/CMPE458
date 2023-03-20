## Cliff Notes
Pictures were obtained using GitHub Commit Comparison:

```
https://github.com/iffy-pi/CMPE458/compare/bc66a8bd7d0c80dd3202324ee4d0e48713c91c60..<latest commit here>

https://github.com/iffy-pi/CMPE458/compare/bc66a8bd7d0c80dd3202324ee4d0e48713c91c60..8b26a97
```

- Token Updates
	- Updating input token list to match output tokens
- String updates
	- Updating char output t-codes to string
	- Adding string size definition
	- Updated char type to string type
	- Added string traps
- Handling Length Operation
- Handling Substring Operation
- Handling String Literals
- Change Handling of string constants to string literals
- Added symbol table requirements

- Updated tokens from semantic.def
- Updated pidChar to pidString and then made ref to be string
- Allocate variable string 

## Overview
- Updated Input Tokens
- Updated Output Tokens
- Added new Symbol Table semantic operations
- Added support for Quby Strings
	- Replaced old char-based output tokens with String
	- Added new String operation T-codes
	- Replaced char types with String
- Updated code to handle string literals as first class data types
- Updated code to handle string constants, as string variables'
- Updated code to handle string equality and inequality with specific `tStringEquals` T-code
- Updated semantic.pt with String pre-declared type and string variable allocation.

## Input Token Updates
Following the previous phases, the input tokens of `semantic.ssl` where updated to match the output tokens of `parser.ssl`. They are the same order to preserve the constants assigned to the tokens by the SSL walker.

![[Pasted image 20230315232740.png]]

## Output Token Updates
The old T-codes that supported the semantic behaviour for while and repeat are removed from the output tokens of `semantic.ssl` as they are not used by Quby.

![[Pasted image 20230315231414.png]]

![[Pasted image 20230315231421.png]]
Instead, they are replaced with new T-codes for the general `do` in

![[Pasted image 20230315231431.png]]

A new t-code `tCaseElse` is also added to support the `else` featured added to cases in Quby.

There are other changes to the T-codes, which will be discussed in later sections.

## New Symbol Table Semantic Operations
The new semantic operations `oSymbolTblStripScope` and `oSymbolTblMergeScope` were added to the `SymbolTable` semantic mechanism:

PICTURE: HERE (NOT ADDED BECAUSE NO COMMENTS ON WHAT IT DOES)

## Structure Updates to support Quby Strings
### Changing Output Tokens
`tFetchChar`, `tAssignChar`, `tStoreChar` and `tSubscriptChar` were all replaced in the output tokens (and in their code usage) with their string counter parts in `semantic.ssl`:

![[Pasted image 20230315230118.png]]

Since Quby strings encompass both Chars and Strings, `tLiteralChar` is replaced by `tLiteralString`.  Quby strings are also first-class values, and are not arrays like they were in Pascal.

New T-codes were added to support the String length, substring, index and equality operations:

![[Pasted image 20230315231359.png]]

### Changing Semantic Mechanisms and Types
Several changes were also made to replace the semantic operations and types in `semantic.ssl` for the Pascal Char type to the Quby String.

`tpChar` was removed from the `TypeKind` type as Quby strings cover both Pascal chars and strings.

![[Pasted image 20230315232133.png]]

Quby Strings are also standard primitive types, and hence replace `stdChar` in the `StdType` type:

![[Pasted image 20230315232216.png]]

Both `tpString` and `stdString` replace the usage of their Char countertypes in the rules.

The `stringSize` token was added to the `Integer` type and initialized to 1024 for the size of string variables.

![[Pasted image 20230315232445.png]]

`pidString` replaces `pidChar` in the `PredeclaredId` type, since Quby strings again replace the Pascal char primitive type. The usage of `pidChar` in rules was also replaced with `pidString`

![[Pasted image 20230315232547.png]]

The Char trap kinds in the `TrapKind` type are also replaced with their String counterparts, initialized to the relevant codes used in the Quby runtime library.

![[Pasted image 20230315233423.png]]

They also replace any usage of the old Char trap codes in the rules.

## Handling String Literals
Quby makes String first class values, unlike Pascal were Strings are treated as packed char array. This leads to changes in how a String literal is handled semantically, in the `StringLiteral` rule in `semantic.ssl`.

Now all strings are handled the same way, unlike the previous checking in Pascal:

![[Pasted image 20230315232949.png]]

In simple terms:
- It pushes the type `tpString` onto the Type Stack and link that Type Stack entry to the standard type for Quby strings with `oTypeStkLinkToStandardType(stdString)`
- Next it uses emit the `tLiteralString` T-code to indicate the next token should be treated as a string
- It then uses `oEmitString` to emit the string value.

This replaces the previous method of handling strings like character arrays, removing the need for the `tSkipString` and `tStringData` T-codes, and hence why they are removed from the output T-codes:

![[Pasted image 20230315231235.png]]

## Handling String Constants
According to the implementation requirements, String constants should be handled as String variables.

This is done in Quby by modifying the `ConstantDefinitions` rule, after the identifier is consumed:

![[Pasted image 20230315234728.png]]

We perform a choice operation on the value token after the identifier. If it is not a string literal, it is handled as a normal constant (`*` alternative). If it is a string literal, then we use the `HandleStringConstant` rule to implement the alternative handling:

![[Pasted image 20230320003350.png]]

The rule performs the same set of operations as done by `VariableDeclarations` and `AssignmentStmt`:
- Push the type onto the type stack
- Enter the variable attributes with `EnterVariableAttributes` rule (this also enters it into the Symbol Table)
- Pop the type from the Type Stack and the local identifier from the Symbol Stack.
- Emits `tAssignBegin` to begin an assignment statement, and uses `Variable` to get type information  (makes sense since identifier is still on top of the symbol stack)
- Emits the relevant string literal
- Finishes with `tAssignString` and clearing out the Symbol stack and type stack

## Implementing String Length
Implementing the String length operation involved modifying the Unary operator to add a new alternative for the `sLength` token. The Unary operator is modified since the string length operation takes one operand:

![[Pasted image 20230315233642.png]]

The type checking for the String length operation is handled with the `HandleStringLengthOperation` rule:

![[Pasted image 20230315233723.png]]

The rule simply checks if the type on top of the type stack is a string, and then pops it from the stack, placing the result type: an Integer. This achieves the same functionality as the other unary operators but is specific to the string length operation.

The `CompareAndSwapTypes` rule cannot be used for type checking (unlike the other unary operators) because the String length operand takes a string type and gives an integer type as a result.

If `CompareAndSwapTypes` were to be used, we would have to make an addition to the inner choice table `tpInteger` alternative in the outer choice table, and add `tpString` as an accepted type:

![[Pasted image 20230315234003.png]]

But this cannot be done as it would allow the negation of a string, which is not allowed in Quby. As a result, we define a specific rule to handle the String operation.

## Handling String Equality
The String equality is handled by using the `tStringEqual` T-code rather than the `tEQ` T-code when the type on the Type Stack is a String:

![[Pasted image 20230316000517.png]]

The choice rule operates on the type on top of the type stack (which is returned by the choice operation `oTypeStkChooseKind`). If the type is a string, then  `StringEqual` is emitted, otherwise  `tEQ` is emitted.

String inequality is handled in a similar way, but with the emission of the `tNot` to invert the results of `tStringEqual`:

![[Pasted image 20230319213412.png]]


## Handling String Substring Operation
The string substring operation is the only three-operand operation in Quby. The `TernaryOperator` rule was written to handle the substring operation and any other tri-operand operations in future:

![[Pasted image 20230320144733.png]]

The `TernaryOperator` rule follows a similar format to the `BinaryOperator` rule:
- It begins with a choice to see if the current semantic token is a tri-op operation, if not the rule exists
- If it is, then the appropriate t-code is emitted for the operation, followed by its type checking and then its result type is pushed onto the stack
- At the end of the rule, we pop the symbol stack twice to remove the `syExpressions` of the last 2 operands, and then set the kind of the last one to an expression
	- This makes it so that the symbol stack contains the result of the operation on top of it

It is added to the Expression rule as the other operator rules are:

![[Pasted image 20230320144827.png]]

The substring operation is identified by the consumption of the `sSubstring` token. When this is matched, we emit the `tSubstring` T-code, handle the type checking with the `HandleStringOperandTypeChecking` rule, and then push the result type of the operation ( a string) to the type stack.

The rule `HandleStringOperandTypeChecking` is as follows:

![[Pasted image 20230320144130.png]]

This follows the format for the standard type checking. Since operands are consumed left to right, the type stack will be in the order of: string, int, int. This is followed in the type checking above: it checks for an integer type, pops the stack again and checks for an integer type and then pops the stack again to check for a string type. If the string type is matched, the type stack is popped and the rule returns.

If the types on the type stack do not match at any point, a type mismatch error is thrown and recovery is done by just popping the relevant number of types from the type stack.


## Changes to `semantic.pt`
### Updating token definitions
`semantic.pt` was updated with the new token constant definitions from `semantic.def` which was generated from the changes to `semantic.ssl`.

The `stdString` and `tpString` also replace the `stdChar` and `tpChar` usage in `semantic.pt`.

### Updating Predeclared Types
As `pidChar` was replaced by `pidString`, its Symbol Table pre-initialization is also updated to reflect this change. The `standardCharTypeRef` was also replaced with `standardStringTypeRef` in the code:

![[Pasted image 20230316001049.png]]

### Adding String Variable Allocation
The switch case in `oAllocateVariable` was modified to allocate space for Quby Strings as they are now first class variables:

![[Pasted image 20230316001558.png]]

`tpChar` is removed from the case statement and a new case for `tpString` is added. The case action allocates `stringSize` bytes for each string variable, just like the Integer and subrange types. 

`stringSize` is set in `semantic.ssl` (the `Integer` type) to 1024.