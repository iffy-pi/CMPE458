
All test files mentioned in this file are located in the folder 'ptsrc/test/phase-2/noah'.

## Unless Statement

### Valid Example

A valid example of the use of the Quby unless statement can be found in the file 'unless.pt'. The output is transformed as expected into an if statement with its expression notted. As well, the body of the statement is bounded by an `.sBegin` and an `.sEnd` token.
```
.sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
   .sIfStmt
        .sIdentifier
        .sInteger
    .sEq
   .sNot
   .sExpnEnd
   % .sNewLine
   .sThen
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          % .sNewLine
          .sIdentifier
     .sExpnEnd
    .sEnd
  .sEnd
```
### Invalid Example
The unless statement in Quby is required to have the `then` keyword token after its condition, the omission of the `then`, as seen in 'bad_unless.pt' makes the compiler fail as shown below in the following output.
```
...
    >>
   ;Expression
   .sNot
   .sExpnEnd
   ?pThen (pIdentifier)
   scan/parse error, line 4: syntax error at: y
   .sThen
   @Block
    .sBegin
    [ (pIdentifier)
    | *:
    ] or >
    .sEnd
...
```

## Case statement
### Valid Examples
The case statement can appear in two general forms in Quby: with a default clause or without one. The first valid testing file, 'case_1.pt' shows the proper output from a case statement with a default `else` clause:
```
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
   .sCaseStmt
        % .sNewLine
        .sIdentifier
   .sExpnEnd
      .sInteger
    .sLabelEnd
    % .sNewLine
     .sBegin
      .sAssignmentStmt
      .sIdentifier
           % .sNewLine
           .sInteger
      .sExpnEnd
     .sEnd
      .sInteger
    .sLabelEnd
    % .sNewLine
     .sBegin
      .sAssignmentStmt
      .sIdentifier
           % .sNewLine
           .sInteger
      .sExpnEnd
     .sEnd
   % .sNewLine
   .sElse
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          % .sNewLine
          .sInteger
     .sExpnEnd
    .sEnd
   .sCaseEnd
  .sEnd

```
The second testing file, 'case_2.pt', is the same as the first, except it removes the optional else clause from the case statement. Its output can be seen below:
```
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
   .sCaseStmt
        % .sNewLine
        .sIdentifier
   .sExpnEnd
      .sInteger
    .sLabelEnd
    % .sNewLine
     .sBegin
      .sAssignmentStmt
      .sIdentifier
           % .sNewLine
           .sInteger
      .sExpnEnd
     .sEnd
      .sInteger
    .sLabelEnd
    % .sNewLine
     .sBegin
      .sAssignmentStmt
      .sIdentifier
           % .sNewLine
           .sInteger
      .sExpnEnd
     .sEnd
   .sCaseEnd
  .sEnd
```

### Invalid Examples

There are three test files for invalid case statements. The first, 'bad_case_1.pt' tests the previous PT Pascal case statement syntax and as expected, it errors when encountering the previous `of` keyword:
```
...
    ;SimpleExpression
    [ (pOf)
    | *:
    >>
   ;Expression
   .sExpnEnd
   ?pWhen (pOf)
   scan/parse error, line 3: syntax error at: of
   @CaseAlternative
...
```
The second test file, 'bad_case_2.pt' tests a case statement that has a `when` clause without a matching `then`.
```
...
    ;OptionallySignedIntegerConstant
    [ (pIdentifier)
    | *:
    ] or >
    .sLabelEnd
    ?pThen (pIdentifier)
    scan/parse error, line 5: syntax error at: y
    @Block
     .sBegin
     [ (pIdentifier)
     | *:
     ] or >
     .sEnd
     >>
    ;Block
...
```
And thirdly, the last test file, 'bad_case_3.pt' tests a case statement that does not have any `when` clauses with a sole `else` statement, which also fails since it is looking for a `.sWhen` token when one is not to be found.
```
...
    ;SimpleExpression
    [ (pElse)
    | *:
    >>
   ;Expression
   .sExpnEnd
   ?pWhen (pElse)
   scan/parse error, line 4: syntax error at: else
   @CaseAlternative
    @OptionallySignedIntegerConstant
     [ (pElse)
     | *:
     @UnsignedIntegerConstant
...
```

## Do Statement
### Valid Examples
The do statement in Quby must start with the keyword `do` and end with the keyword `end` and in its body must contain exactly one `break if` statement. The testing file 'do.pt' adheres to the proper syntax and as expected produces the following valid token output stream:
```
 .sProgram
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  % .sNewLine
   .sDo
   .sBegin
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          % .sNewLine
          .sInteger
     .sExpnEnd
    .sEnd
   .sBreakIf
        .sIdentifier
        % .sNewLine
        .sInteger
    .sEq
   .sExpnEnd
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          % .sNewLine
          .sInteger
     .sExpnEnd
    .sEnd
   .sEnd
  .sEnd
  ```

### Invalid Example

The do loop is coming into the Quby language as a form of replacing the repeat loop and thus the repeat loop syntax has been deprecated. In the file 'bad_repeat.pt', the old syntax is utilized and as expected the program fails.
```
...
   | *:
   @CallStmt
    .sCallStmt
    .sIdentifier
    [ (pEquals)
    | *:
    .sParmEnd
    >>
   ;CallStmt
   >>
  ;AssignmentOrCallStmt
  ] or >
  }
  [ (pEquals)
  | *:
  ] or >
  .sEnd
  >>
 ;Block
 >>
;Program
scan/parse error, line 5: syntax error at: =
```

To test the new do syntax more rigorously, two more test files are provided. The first, 'do_1.pt' tests a do statement without the required `break if`, and as expected, it fails.
```
...
  [ (pEnd)
    | *:
    ] or >
    .sEnd
    >>
   ;Block
   ?pBreak (pEnd)
   scan/parse error, line 6: syntax error at: end
   ?pIf (pEnd)
   .sBreakIf
   @Expression
    @SimpleExpression
     [ (pEnd)
     | *:
     @Term
...
```
In the second file, a second break if statement is used in the loop which is not allowed. Following this rule, the program fails as shown.
```
...
   ] or >
    }
    [ (pBreak)
    | *:
    ] or >
    .sEnd
    >>
   ;Block
   ?pEnd (pBreak)
   scan/parse error, line 7: syntax error at: break
   .sEnd
   >>
  ;DoStmt
  ] or >
  }
  [ (pBreak)
  | *:
  ] or >
  .sEnd
...
```
