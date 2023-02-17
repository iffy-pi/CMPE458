## Cliff Notes
- Test declarations --> Done
    - Constants
    - Types
    - Variables
- Syntax changes
    - Not operator
    - Not equals
    - Assignment operator
    - Comparison operator
- String operations
    - Substring ($)
    - Index (?)
    - Length (#)
    - Testing parsing of expressions
    - Verifying it obeys specified precedence

## Declarations
### General Invalid Assignments
#### Missing Identifier
If the declaration is missing an identifier (for constant, type and variable declarations), the parser will throw an error as all rules are expecting the `pIdentifier` token after the keyword. Instead of that they receive the token for the declaration assignment operator (either colon or `=`)

This is verified by the parser trace output on the file `general_invalid_1.pt`, which omits the identifier for a variable declaration.

```
...
.sVar
  @VariableDeclarations
   ?pIdentifier (pColon)
   scan/parse error, line 3: syntax error at: :
   .sIdentifier
   [ (pColon)
   | *:
...
```

The same error will occur for other declaration types as based on `general_invalid_2.pt` and `general_invalid_3.pt`

`general_invalid_2.pt` output:

```
...
  @ConstantDefinitions
   ?pIdentifier (pAssignEquals)
   scan/parse error, line 3: syntax error at: =
   .sIdentifier
   ?pAssignEquals (pAssignEquals)
   @ConstantValue
...
```

`general_invalid_3.pt` output:

```
...
  @TypeDefinitions
   ?pIdentifier (pColon)
   scan/parse error, line 3: syntax error at: :
   .sIdentifier
   ?pColon (pColon)
   @TypeBody
    [ (pColon)
    | *:
    @SimpleType
...
```

#### Keyword as Identifier Name
If a keyword is used as the identifier name for any declaration, the parser will thrown an error. This is because keywords have their own tokens and are not recognized as `pIdentifier` tokens, which are what the declaration rules are expecting.

This is verified by the parser trace output on the file `general_invalid_4.pt`, which uses the unless keyword for a variable declaration.

```
...
  @VariableDeclarations
   ?pIdentifier (pUnless)
   scan/parse error, line 3: syntax error at: unless
   .sIdentifier
   [ (pUnless)
   | *:
   ] or >
...
```

he same error will occur for other declaration types as based on `general_invalid_5.pt` and `general_invalid_6.pt`

`general_invalid_5.pt` output:

```
...
  @ConstantDefinitions
   ?pIdentifier (pUnless)
   scan/parse error, line 3: syntax error at: unless
   .sIdentifier
   ?pAssignEquals (pUnless)
   @ConstantValue
    [ (pUnless)
...
```

`general_invalid_6.pt` output:

```
...
 @TypeDefinitions
   ?pIdentifier (pUnless)
   scan/parse error, line 3: syntax error at: unless
   .sIdentifier
   ?pColon (pUnless)
   @TypeBody
...
```


### Constants
#### Valid Declaration
First we used `constants_valid.pt` to test if the parser outputted the correct semantic tokens for declaring constants in Quby. The file contains two constant declarations and a `using` statement to complete the program.

The expected output of the program is (Note the double slash `//` refers to our own added comments to the system output):

```
.sProgram        // For the pUsing token
.sIdentifier     // Identifier of the using statement
.sParmEnd        // Part of the program definition
.sBegin          // Block begin statement
.sConst          // the constant semantic token, triggered by pVal token
.sIdentifier     // identifer for "a"
.sInteger        // the constant assigned to "a"
.sConst          // the constant semantic token, triggered by pVal token
.sIdentifier     // identifier for "b"
.sStringLiteral  // The string constant assigned to "b"
.sEnd            // Block end statement
```

By running `parsetrace` on the file, we get the following output:

```
 % .sNewLine
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sConst
   .sIdentifier
    % .sNewLine
    .sInteger
  .sConst
   .sIdentifier
    .sStringLiteral
  .sEnd
```

This matches our expected output, with the only change being the addition of the `% .sNewLine`, which are automatically emitted by the parser. This shows that the parser can correctly parse constant assignment statements in Quby.

#### Invalid Declaration
We also test invalid constant declarations to ensure the parser throws an error when they are seen. Consider `constants_invalid_1.pt` where the constant assignment is done with a colon rather than an `=`. While the emitted tokens look the same:

```
% .sNewLine
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sConst
   .sIdentifier
    .sInteger
  .sEnd
```

Looking at the entire parsertrace output, we see that an error is raised when we encounter the token. This will be caught by the full compiler:

```
...
  @ConstantDefinitions
   ?pIdentifier (pIdentifier)
   .sIdentifier
   ?pAssignEquals (pColon)
   scan/parse error, line 3: syntax error at: :
   @ConstantValue
    [ (pColon)
    | *:
    ?pInteger (pColon)
    }
...
```

We also try declaring multiple constants at once using the comma separated notation only reserved for variable declaration. This is done in `constants_invalid_2.pt` whose output is:

```
 % .sNewLine
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sConst
   .sIdentifier
    .sInteger
  .sEnd
```

The outputted semantic tokens only recognize one constant declaration instead of the others. Furthermore, a parser error is thrown due to the occurrence of the comma:

```
...
   .sIdentifier
   ?pAssignEquals (pComma)
   scan/parse error, line 3: syntax error at: ,
   @ConstantValue
    [ (pComma)
    | *:
    ?pInteger (pComma)
    }
    .sInteger
...
```

#### Identifier Constant Assignment
The file `constant_idens.pt` tests constant assignment with a variable that was not previously defined. The parser trace output for this file is:

```
 % .sNewLine
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sConst
   .sIdentifier
    .sIdentifier
  .sEnd
```

The parser does not throw any errors as an identifier is considered a legal constant value. The parser is not able to recognize the identifier as undeclared because it performs context free syntax checking and therefore cannot see the scope of the identifier.

### Type Declarations
#### Valid Assignments
The file `type_valid.pt` contains two valid type declarations and is the test file to show that the parser correctly parses type declarations. The expected output of the parser trace on this file is:

```
.sProgram        // For the pUsing token
.sIdentifier     // Identifier of the using statement
.sParmEnd        // Part of the program definition
.sBegin          // Block begin statement

.sType       // type semantic token
.sIdentifier // type identifier for "t"
.sIdentifier // type assigned for t
.sType       // type semantic token
.sIdentifier // type identifier for "p"
.sIdentifier // type assigned for p 

.sEnd            // Block end statement
```

This is validated by the actual parsertrace output:

```
 % .sNewLine
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sType
   .sIdentifier
     % .sNewLine
     .sIdentifier
  .sType
   .sIdentifier
     .sIdentifier
  .sEnd
```

Since a `pIdentifier` is considered a valid type (as shown in SimpleType), undeclared user types will not cause parser errors as that requires context aware checking (the parser is nt aware of the scope of the identifiers).

### Invalid Assignments
The file `type_invalid_1.pt` attempts to create a type with the `=` operator rather than the `:` operator. While the parser trace output indicates no issues:

```
 % .sNewLine
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sType
   .sIdentifier
       .sIdentifier
     .sRange
       .sIdentifier
  .sEnd
```

Investigating the full parser trace shows that a parsing error was thrown when the parser expected a `:` in TypeBody but instead got the `=`:

```
...
  @TypeDefinitions
   ?pIdentifier (pIdentifier)
   .sIdentifier
   ?pColon (pAssignEquals)
   scan/parse error, line 3: syntax error at: =
   @TypeBody
    [ (pAssignEquals)
    | *:
    @SimpleType
     [ (pAssignEquals)
...
```

### Variables
#### Valid Assignments
The file `variables_valid.pt` is designed to test if the parser correctly parses a variable declarations. It contains two one-variable declarations on separate lines. The expected output is:

```
.sProgram        // For the pUsing token
.sIdentifier     // Identifier of the using statement
.sParmEnd        // Part of the program definition
.sBegin          // Block begin statement

.sVar         // variable declaration token
.sIdentifier  // identifier for variable to be declared: "a"
.sIdentifier  // identifier for variable type of a
.sVar         // variable declaration token
.sIdentifier  // identifier for variable to be declared: "b"
.sIdentifier  // identifier for variable type of b

.sEnd            // Block end statement
```

This is verified by the actual parser trace output shown below:

```
 % .sNewLine
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sVar
   .sIdentifier
     % .sNewLine
     .sIdentifier
  .sVar
   .sIdentifier
     .sIdentifier
  .sEnd
```

We also have the test file `variables_commas_valid.pt` to test the parsing of multi-variable declarations using the comma separation that is introduced in Quby. This file is a modifications of `variables_valid.pt`, where instead we have one two-variable declaration.

The expected output for this case would be the variables token and the identifier token, ending with the type to be assigned to the variables:

```
.sProgram        // For the pUsing token
.sIdentifier     // Identifier of the using statement
.sParmEnd        // Part of the program definition
.sBegin          // Block begin statement

.sVar         // variable declaration token
.sIdentifier  // identifier for variable to be declared: "a"
.sVar         // variable declaration token
.sIdentifier  // identifier for variable to be declared: "b"
.sIdentifier  // identifier for variable type of b and a

.sEnd            // Block end statement
```

This is verified by the actual parser trace output shown below:

```
 % .sNewLine
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sVar
   .sIdentifier
   .sVar
   .sIdentifier
     .sIdentifier
  .sEnd
```

#### Invalid Assignments
The file `variables_invalid_1.pt` tries to declare variables with the `=` operator rather than the expected `colon` operator. As the case with types, the parser throws an error as it was expecting the colon:

```
...
   ?pColon (pAssignEquals)
   scan/parse error, line 3: syntax error at: =
   @TypeBody
    [ (pAssignEquals)
    | *:
    @SimpleType
     [ (pAssignEquals)
...
```

We also have `variables_invalid_2.pt` which misuses the comma notation for multi-variables. It uses the comma but does not specify a variable name.

The parser throws an error for this, because (as defined the VariableDeclarations rule) the parser is expecting a `pIdentifier` if a `,` is specified after the first variable identifier:

```
...
   [ (pComma)
   | pComma:
   .sVar
   ?pIdentifier (pColon)
   scan/parse error, line 3: syntax error at: :
   .sIdentifier
   ] or >
   }
...
```