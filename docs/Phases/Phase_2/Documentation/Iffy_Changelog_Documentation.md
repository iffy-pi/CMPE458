## Cliff Notes
Link:
```
https://github.com/iffy-pi/CMPE458/compare/aab721523cf8c40155f0580c7140c702c4ba7eea..<latest commit here>
```

## Declarations
### Constants
Removed the semicolon ending token in the `ConstantDefinitions` rule as the semicolon ending token is not required in Quby.

Also removed the input choice loop to parse sequential constant declarations. Since Quby does not distinguish between declarations and statements, we can just have multiple constants handle by the main Block rule.

```
PICTURE OF CONSTANT DEFINITIONS HERE
```

### Types
Removed ending semicolon requirement from `TypeDefinitions` rule and also removed the parsing of multiple type declarations (for the same reason as removing the one in `ConstantDefinitions`).

```
PICTURE OF TYPE DEFINITIONS HERE
```

### Variables
Similar to the last two, in `VariableDeclarations`:
- Removed the ending semicolon requirement
- Removed the parsing of multiple variable declarations since that is handled by the Block rule

```
PICTURE OF VARIABLE DECLARATIONS HERE, showing deleted stuff
```

Also added an input choice loop to parse one-line variable declarations done with the comma.

```
Showing added choice loop
```

## Strings
### Index Operation
The string index operation `?` takes expressions as both its arguments according to the language specifications, and is at the same precedence as `div` and `mod`.

To make `?` the same precedence, it was added as a choice alternative to the Term rule, which contains the `div` and `mod` operations.

```
PICTURE OF RULE ADDED
```

As its choice actions, it calls the Subterm rule to maintain precedence. If the Expression rule is used instead, lower binding operators can be binded before the index operator.

We emit the `sIndex` semantic token after consuming the expression to make sure parser output is in postfix notation.

### Length Operation
The string length operation `#` is also similar to `?` and takes an expression as its operand. It is at the same precedence as not, and was therefore added as a choice alternative to the Factor rule.

```
PICTURE OF THE FACTOR RULE
```

A call to the Factor rule is done for parsing expressions again to maintain precedence. If lower binding operators are required, the contents can be surrounded by brackets which will lead to an Expression rule call in Factor.

### Substring Operation
The substring operation is at a new precedence level: Higher than `div` and `mod` but lower than `not`. To implement this new precedence level, the Subterm rule was defined:

```
PICTURE OF SUBTERM RULE
```

The Subterm rule is now in-between the Term and Factor rule as the new precedence level. Therefore, every call to Factor in Term was replaced with the Subterm rule.

```
picture of term rule
```

In the Subterm rule, we first make a call to Factor to process the preceding string literal that is the first operand of the substring operation. Then we have an input choice loop similar to that in Term.

If the read token is the `$`, then we call Factor to parse the range operands and then emit the `sSubstring` token to follow post fix notation. If it is anything else, we break.

## Other Syntactic Details
No functional changes to the parser were required for these changes as the only thing changed were the string of characters associated with the given operation. Therefore a simple find and replace in parser.ssl was done:
- Every occurrence `<>` was replaced with the new operation `!=`
- Every occurrence of the `not` keyword was replaced with the `pNot` token
- Every occurrence of `pColonEquals` or `:=` was replaced with the `pAssignEquals` token
- Every occurrence of `=` was replaced with `==` for the comparison equals operation.