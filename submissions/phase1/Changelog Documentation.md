## Keywords
### Adding New Keywords - Iffy
Quby adds the following keywords to the language:
- `using`
- `val`
- `def`
- `break`
- `when`
- `module`
- `unless`
- `elsif`

In order for these new keywords to be screened into their associated keyword tokens, the Scanner/Screener must know the string of characters that is associated to each keyword (for example, `break` is identified with the string "break").

These strings were added to parser/stdIdentifiers:

![[Pasted image 20230204162540.png]]

Then, an output token was created for each new keyword and was put in the output section of parser/scan.ssl:

![[Pasted image 20230204162753.png]]

The output tokens for the keywords were placed in the same order as their strings in stdIdentifiers in order for the tokens to be mapped to the appropriate strings.

### Removing Old Keywords - Iffy
Quby also removes the following keywords from the program:
- not
- until
- program
- const
- procedure
- begin
- repeat

To remove these keywords, the opposite set of steps were taken for adding keywords.

First, the string value assigned to each keyword was removed from parser/stdIdentifiers:

![[Pasted image 20230204163118.png]]

Then, their associated tokens were removed from parser/scan.ssl:

![[Pasted image 20230204163201.png]]

It is also important to note that since `pRepeat` was the last keyword token before the change, the new last keyword token is `pElsif` which was assigned to `lastKeywordToken`.

### Updating parser.pt
The final step required is to update parser/parser.pt with the modified set of tokens. This is required because parser.pt contains the integer codes assigned to the scan.ssl output tokens. As we have both added and removed tokens, the defined tokens in parser.pt are out of date.

We update parser.pt by first running `make scanner` to generate parser/scan.def which contains the token integer code assignments written in Pascal, for example:

```
        lBackslash = 13;
        lLeftAngle = 14;
        lRightAngle = 15;
        lLeftParen = 16;
        lRightParen = 17;
        lLeftBracket = 18;
        lRightBracket = 19;
        lLeftBrace = 20;
        lRightBrace = 21;
        lExclamation = 22;
        lHash = 23;
```

We then copy the contents of scan.def and paste it into the specified locations at parser.pt. This essentially updates parser.pt with the new tokens and their associated integer codes. An excerpt of some the changes in parser.pt is shown below:

![[Pasted image 20230204163816.png]]

## New String Literals - Iffy
In Quby, strings are defined with double quotes (`"`) rather than single quotes (`'`). To implement this specification, the defined quotation character would have to be changed.

The quotation character recognized by the compiler is defined in parser/parser.pt, assigned to the `quote` variable.

Therefore, the only change required is to update the value assigned to the quote variable from a single quote, to a double quote:

![[Pasted image 20230204164459.png]]

## New Operator Characters - (Iffy, Ethan, Liam and Noah)
Quby implements some new operators with the addition of the following characters: `%`, `#`, `?`, `$` and `!`.

These characters were not used in the Pascal program specification and are therefore not assigned any input tokens in scan.ssl. This was rectified by adding the input tokens along with the character mnemonic:

![[Pasted image 20230204165055.png]]

Since the contents of scan.ssl were changed, we recompiled scan.def and copied it into parser.pt to add the new input tokens.

However, parser.pt does not get the string mnemonics from scan.def, only the integers assigned to each token. The `charClassMap` is used instead and maps tokens to their associated character. This was also modified to add the new operator characters. For each one, the character was assigned to their associated input token:

![[Pasted image 20230204165326.png]]

## Scanning New Operators (`?`, `$` and `#`) - Liam & Ethan
The question mark, dollar and hash tag are new operators that have specific functionality in the Quby language. This means that they must have their own tokens like other operators and be emitted by the scanner when they are read.

Firstly, we implement their output tokens by adding them to the output section of scan.ssl:

![[Pasted image 20230204165947.png]]

As we have changed the set of defined tokens in scan.ssl, we updated parser.pt with the recompiled scan.def.

Next, we add new choices to the choice loop for the main Scan rule in scan.ssl. These choices match against our operator characters and emit their associated token:

![[Pasted image 20230204170126.png]]

![[Pasted image 20230204170219.png]]

As seen above, when `?` is matched, it is consumed and emits `pQuestion`, the assigned `pQuestion` token.

## Handling New Not (`!`) and Not Equals (`!=`) - Ethan & Iffy
Quby replaces Pascal's `not` and `<>` with `!` and `!=`. This was what led to the addition of the exclamation character in the program. 

Since `not` is no longer a keyword, the `!` operator must be assigned its own token so that in later stages the parser knows how to handle it. This is done by adding its token to the list of output tokens in scan.ssl:

![[Pasted image 20230204170609.png]]

As we have changed the set of defined tokens in scan.ssl, we updated parser.pt with the recompiled scan.def.

Next we add a new choice option in the main Scan rule for the exclamation character and then handle the two different cases, for the not operation and the not equals:

![[Pasted image 20230204170711.png]]

Finally, we need to remove the support for the old not equals operator (`<>`), this is done by removing the second choice  when the choice matches the `<` label:

![[Pasted image 20230204170856.png]]

## Handling New Assignment (`=`) and Comparison `(==)` Operators - Iffy
Quby replaces Pascal's `:=` and `=` with `=` and `==` respectively. These changes would have to be made in the scanner in order to emit the correct tokens for the new characters.

Firstly, the `pColonEquals` token in scan.ssl was replaced with a more descriptive token name for the operation: `pAssignEquals`:

![[Pasted image 20230204171101.png]]

As we have changed the set of defined tokens in scan.ssl, we updated parser.pt with the recompiled scan.def.

Then the actions run when the `=` character is matched in the choice of the main Scan rule was modified to emit the expected tokens:

![[Pasted image 20230204171242.png]]

Finally, support for the old `:=` token was removed by modifying the choice of `:`:

![[Pasted image 20230204171308.png]]

## New Comments with `%` - Noah
Quby replaces Pascal's old version of comments with the simple use of the `%` symbol. Any characters after the `%` symbol are discarded.

This was done by changing the input token for the choice label that called the Comment rule in the main Scan rule to a `%`:

![[Pasted image 20230204171530.png]]

The Comment Rule was modified to handle the new comment parsing, and the AlternateComment rule was removed to remove support for the other version of Pascal comments:

![[Pasted image 20230204171721.png]]

















