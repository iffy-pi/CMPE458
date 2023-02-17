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

As its choice actions, it calls the Expression rule rather than the Subterm rule since it is designed to take an expression as its right operand as well.

We emit the `sIndex` semantic token after consuming the expression to make sure parser output is in postfix notation.

### Length Operation
The string length operation `#` is also similar to `?` and takes an expression as its operand. It is at the same precedence as not, and was therefore added as a choice alternative to the Factor rule.

```
PICTURE OF THE FACTOR RULE
```

Again similar to the index operator, it takes an expression. Therefore the Expression rule is called. We emit the `sLength` semantic token after to follow the postfix notation required in the parser output token stream.

### Substring Operation
The substring operation is at a new precedence level: Higher than `div` and `mod` but lower than `not`. To implement this new precedence level, the Subterm rule was defined:

```
PICTURE OF SUBTERM RULE
```

The Subterm rule is now in-between the Term and Factor rule as the new precedence level. Therefore, every call to Factor in Term was replaced with the Subterm rule.

```
picture of term rule
```

In the Subterm rule, we have a simple input choice to check if a `$` token is the next input token. If it is not, it matches the default alternative which just calls the Factor rule. This implements the previous functionality before the addition of the new precedence.

If the `$` token was read, then we call the Expression rule to parse both operands of the `pDotDot` token and then emit the `sSubstring` token to do the operation. 

## Other Syntactic Details
No functional changes to the parser were required for these changes as the only thing changed were the string of characters associated with the given operation. Therefore a simple find and replace in parser.ssl was done:
- Every occurrence `<>` was replaced with the new operation `!=`
- Every occurrence of the `not` keyword was replaced with the `pNot` token
- Every occurrence of `pColonEquals` or `:=` was replaced with the `pAssignEquals` token
- Every occurrence of `=` was replaced with `==` for the comparison equals operation.