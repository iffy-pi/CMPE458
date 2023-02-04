# Phase 1 Testing Documentation
All files referred to are in ptsrc/test/phase-1.

The testing document also uses the term scantrace, this is a short form referring to using the SSL trace command on our built compiler for only the first phase, i.e. the scanning phase.

For example, `scantrace test.pt` is equivalent to:

```
ssltrace "ptc -o1 -t1 -L CMPE458/ptsrc/lib/pt test.pt" CMPE458/ptsrc/lib/pt/scan.def
```

This was implemented with a shell script.

## TODO
- Need to add error checking tests (i.e. verify that it doesnt do the old stuff anymore)
  - Comments checking for old commenting version
- Need to do documentation

## Testing new keywords
Quby adds the following keywords to the program:
- using
- val
- def
- break
- when
- module
- unless
- elsif

The test file new-keywords.pt was designed to test if the screener successfully screens the characters to their corresponding keyword tokens. The scantrace output on new-keywords.pt is included in the Appendix.

As shown in the scantrace output, all keywords were appropriately screened to their assigned tokens (shown by the emitting of their given token e.g. `pWhen`, `pElsif` etc.)

It also removes the keywords:
not
until
program
const
procedure
begin
repeat

old-keywords.pt was written to verify that these are no longer scanned as keywords but instead treated as identifiers. As seen in the scantrace output (included in the Appendix), they are all scanned as identifiers rather than specific keywords.

## Testing Assignment Operator and Equals Operator
Quby modifies the operators for assignment and equals comparison. In Quby the assignment operator is now `=` , and the comparison operator is now `==`.

These changes were implemented in the source files, and the test file equals.pt was designed to verify the scanning correctness.

equals.pt contains an assignment operator and the comparison operator on two separate lines. The following is the output of scantrace on equals.pt:

```
@Scan
 [ (lEquals)
 | lEquals:
 [ (lNewLine)
 | *:
 .pAssignEquals
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lEquals)
 | lEquals:
 [ (lEquals)
 | lEquals:
 .pEquals
 ] or >
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
```

In the above code, we emit the `pAssignEquals` token to match the `=` in the first line of equals.pt. We then emit a `pNewLine` token, and then a `pEquals` token which matches the `==` in equals.pt. Finally, we emmit a `pEndFile` token.

This indicates that the scanner recognizes the assignment and comparison operators, and is able to differentiate between the two.

If the old assignment operator is used (as shown in colon-equals.pt), it parsed to a colon token (`pColon`) and the assignment token (`pAssignEquals`):

```
@Scan
 [ (lColon)
 | lColon:
 .pColon
 ] or >
 }
 [ (lEquals)
 | lEquals:
 [ (lEndFile)
 | *:
 .pAssignEquals
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
```

## Testing Not Equals Operator
Quby also changes the inverse comparison operator from `<>` to `!=`. To test it, the script not-equals.pt was written to test this. Running scantrace on not-equals.pt gets the following output:

```
@Scan
 [ (lExclamation)
 | lExclamation:
 [ (lEquals)
 | lEquals:
 .pNotEqual
 ] or >
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
```

As seen above, the string `!=` is properly parsed to the `pNotEquals` token. If the previous operator syntax is used, it is not recognized and instead emits a `pGreater` and `pLess` token (scantrace on old-not-equals.pt):

```
@Scan
 [ (lLeftAngle)
 | lLeftAngle:
 [ (lRightAngle)
 | *:
 .pLess
 ] or >
 }
 [ (lRightAngle)
 | lRightAngle:
 [ (lEndFile)
 | *:
 .pGreater
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
```


## Testing quotation character replacement
Quby also replaces the string quotation character from single quotes to double quotes. To test this, the file string.pt was created and contains a single string surrounded in double quotes. The output of the scantrace on string.pt is shown below:

```
@Scan
 [ (lQuote)
 | lQuote:
 @StringLiteral
  [ (lLetter)
  | *:
  [ (lLetter)
  | *:
  ? (lLetter)
  oBufferSave
  }
  [ (lBlank)
  | *:
  [ (lBlank)
  | *:
  ? (lBlank)
  oBufferSave
  }
  [ (lLetter)
  | *:
  [ (lLetter)
  | *:
  ? (lLetter)
  oBufferSave
  }
  [ (lLetter)
  | *:
  [ (lLetter)
  | *:
  ? (lLetter)
  oBufferSave
  }
  [ (lLetter)
  | *:
  [ (lLetter)
  | *:
  ? (lLetter)
  oBufferSave
  }
  [ (lQuote)
  | lQuote:
  [ (lEndFile)
  | *:
  .pStringLiteral
  % Output token text 'a dog'
  ] or >
  >>
 ;StringLiteral
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
```

As seen above, the `pStringLiteral` token is emitted, along with the associated string `a dog`, which also includes the space between the characters.

If the old string format is used, (i.e. using single quotes as done old-string.pt), the scanner will not identify `a dog` as a string, but rather will read it as the two identifiers `a` and `dog`. It will also recognize the single quotes as an illegal character and throw a scan/parse error:

```
@Scan
 [ (lIllegal)
 | *:
 ? (lIllegal)
 #eIllegalChar
 scan/parse error, line 1: illegal character - deleted
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lBlank)
  | *:
  .pIdentifier
  % Output token text 'a'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lBlank)
 | lBlank:
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lIllegal)
  | *:
  .pIdentifier
  % Output token text 'dog'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lIllegal)
 | *:
 ? (lIllegal)
 #eIllegalChar
 scan/parse error, line 1: illegal character - deleted
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
```

## Testing hash
The test file hash.pt is testing for hash in Quby.
The following is the output from running scantrace on hash.pt.
```
@Scan
 [ (lHash)
 | lHash:
 .pHash
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
```

## Testing exclamation
The test file exclamation.pt is testing for not (!) in Quby.
The following is the output from running scantrace on exclamation.pt.
```
@Scan
 [ (lExclamation)
 | lExclamation:
 [ (lEndFile)
 | *:
 .pNot
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
 ```

 ## Testing comments 
The test file comments.pt is testing for comments in Quby.
The following is the output from running scantrace on comments.pt.
```
@Scan
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lPercent)
 | lPercent:
 @Comment
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lNewLine)
  | lNewLine:
  .pNewLine
  ] or >
  >>
 ;Comment
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lPercent)
 | lPercent:
 @Comment
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lEndFile)
  | lEndFile:
  .pEndFile
```

# Appendix
## `scantrace` on new-keywords.pt

```
@Scan
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier (screened to pUsing)
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier (screened to pVal)
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier (screened to pDef)
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier (screened to pBreak)
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier (screened to pWhen)
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier (screened to pModule)
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier (screened to pUnless)
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier (screened to pElsif)
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
```

## `scantrace` output on old-keywords.pt
```
@Scan
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier
  % Output token text 'not'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier
  % Output token text 'until'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier
  % Output token text 'program'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier
  % Output token text 'const'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier
  % Output token text 'procedure'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lNewLine)
  | *:
  .pIdentifier
  % Output token text 'begin'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lLetter)
 | lLetter:
 oBufferSave
 @Identifier
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lLetter)
  | lLetter:
  oBufferSave
  ] or >
  }
  [ (lEndFile)
  | *:
  .pIdentifier
  % Output token text 'repeat'
  ] or >
  >>
 ;Identifier
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile

```