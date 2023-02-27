# Testing documentation for sections done by Liam

All code used for testing can be found in /ptsrc/test/phase-2/liam/

# 'module' testing
## Valid test case:

The code module.pt in the /ptsrc/test/phase-2/liam/ directory outputted the correct code shown below. This test case was used to see a correct implementation of the 'module' declaration

```
 .sProgram
 .sIdentifier
 .sParmEnd
  .sBegin
  % .sNewLine
  % .sNewLine
   .sModule
   % .sNewLine
   .sIdentifier
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          % .sNewLine
          .sInteger
     .sExpnEnd
     .sAssignmentStmt
     .sIdentifier
          % .sNewLine
          .sInteger
     .sExpnEnd
    .sEnd
  .sEnd
```

## Erroneus test case:
In the module error pt file, module_error.pt, the modules identifier is removed. An error is thrown at the subsequent line were x = 1 is. Below is the following output:
```
@Program
 ?pUsing (pUsing)
 .sProgram
 ?pIdentifier (pIdentifier)
 .sIdentifier
 [ (pSemicolon)
 | *:
 ] or >
 .sParmEnd
 @Block
  .sBegin
  [ (pSemicolon)
  | pSemicolon:
  % .sNewLine
  % .sNewLine
  ] or >
  }
  [ (pModule)
  | pModule:
  % .sNewLine
  @Module
   .sModule
   ?pIdentifier (pIdentifier)
   .sIdentifier
   @Block
    .sBegin
    [ (pAssignEquals)
    | *:
    ] or >
    .sEnd
    >>
   ;Block
   >>
  ;Module
  ] or >
  }
  [ (pAssignEquals)
  | *:
  ] or >
  .sEnd
  >>
 ;Block
 >>
;Program
scan/parse error, line 4: syntax error at: =
```

# 'while' testing
## Valid test case:
The code from while.pt outputted the following. This code correctly outputted the sBegin and sEnd to encompase the statments encapsulated by the loop.

```
 .sProgram
 .sIdentifier
 .sParmEnd
  .sBegin
  % .sNewLine
  % .sNewLine
   .sWhileStmt
        .sIdentifier
        .sInteger
    .sEq
   .sExpnEnd
   % .sNewLine
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          .sIdentifier
          % .sNewLine
          .sInteger
       .sAdd
     .sExpnEnd
    .sEnd
  .sEnd
```
## Erroneus test case:
In this test case the while loop is missing the subsequent do after the expression. The file while_error.pt had the following output:
```
@Program
 ?pUsing (pUsing)
 .sProgram
 ?pIdentifier (pIdentifier)
 .sIdentifier
 [ (pSemicolon)
 | *:
 ] or >
 .sParmEnd
 @Block
  .sBegin
  [ (pSemicolon)
  | pSemicolon:
  % .sNewLine
  % .sNewLine
  ] or >
  }
  [ (pWhile)
  | pWhile:
  @WhileStmt
   .sWhileStmt
   @Expression
    @SimpleExpression
     [ (pIdentifier)
     | *:
     @Term
      @Subterm
       [ (pIdentifier)
       | *:
       @Factor
        [ (pIdentifier)
        | pIdentifier:
        .sIdentifier
        @IdentifierExtension
         [ (pEquals)
         | *:
         >>
        ;IdentifierExtension
        ] or >
        >>
       ;Factor
       >>
      ;Subterm
      [ (pEquals)
      | *:
      ] or >
      >>
     ;Term
     [ (pEquals)
     | *:
     ] or >
     >>
    ;SimpleExpression
    [ (pEquals)
    | pEquals:
    @SimpleExpression
     [ (pInteger)
     | *:
     @Term
      @Subterm
       [ (pInteger)
       | *:
       @Factor
        [ (pInteger)
        | pInteger:
        % .sNewLine
        .sInteger
        ] or >
        >>
       ;Factor
       >>
      ;Subterm
      [ (pIdentifier)
      | *:
      ] or >
      >>
     ;Term
     [ (pIdentifier)
     | *:
     ] or >
     >>
    ;SimpleExpression
    .sEq
    ] or >
    >>
   ;Expression
   .sExpnEnd
   ?pDo (pIdentifier)
   scan/parse error, line 4: syntax error at: x
   @Block
    .sBegin
    [ (pIdentifier)
    | *:
    ] or >
    .sEnd
    >>
   ;Block
   >>
  ;WhileStmt
  ] or >
  }
  [ (pIdentifier)
  | *:
  ] or >
  .sEnd
  >>
 ;Block
 >>
;Program
```

# 'if' testing
## Valid test case:
The pt code used to test the if statements can be found in '/ptsrc/test/phase-2/liam/if.pt'. This code was used to test the correct use case of if statments

The testing code outputted:
```
 .sProgram
 .sIdentifier
 .sParmEnd
  .sBegin
  % .sNewLine
  % .sNewLine
   .sIfStmt
        .sIdentifier
        .sInteger
    .sEq
   .sExpnEnd
   % .sNewLine
   .sThen
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          .sInteger
     .sExpnEnd
    % .sNewLine
    .sEnd
  .sEnd
```
## Erroneus test case:
In the file if_error.pt, there is a missing then after an expression. The code had the following output:
```
@Program
 ?pUsing (pUsing)
 .sProgram
 ?pIdentifier (pIdentifier)
 .sIdentifier
 [ (pSemicolon)
 | *:
 ] or >
 .sParmEnd
 @Block
  .sBegin
  [ (pSemicolon)
  | pSemicolon:
  % .sNewLine
  % .sNewLine
  ] or >
  }
  [ (pIf)
  | pIf:
  @IfStmt
   .sIfStmt
   @Expression
    @SimpleExpression
     [ (pIdentifier)
     | *:
     @Term
      @Subterm
       [ (pIdentifier)
       | *:
       @Factor
        [ (pIdentifier)
        | pIdentifier:
        .sIdentifier
        @IdentifierExtension
         [ (pEquals)
         | *:
         >>
        ;IdentifierExtension
        ] or >
        >>
       ;Factor
       >>
      ;Subterm
      [ (pEquals)
      | *:
      ] or >
      >>
     ;Term
     [ (pEquals)
     | *:
     ] or >
     >>
    ;SimpleExpression
    [ (pEquals)
    | pEquals:
    @SimpleExpression
     [ (pInteger)
     | *:
     @Term
      @Subterm
       [ (pInteger)
       | *:
       @Factor
        [ (pInteger)
        | pInteger:
        % .sNewLine
        .sInteger
        ] or >
        >>
       ;Factor
       >>
      ;Subterm
      [ (pIdentifier)
      | *:
      ] or >
      >>
     ;Term
     [ (pIdentifier)
     | *:
     ] or >
     >>
    ;SimpleExpression
    .sEq
    ] or >
    >>
   ;Expression
   .sExpnEnd
   ?pThen (pIdentifier)
   scan/parse error, line 4: syntax error at: x
   .sThen
   @Block
    .sBegin
    [ (pIdentifier)
    | *:
    ] or >
    .sEnd
    >>
   ;Block
   [ (pIdentifier)
   | *:
   >>
  ;IfStmt
  ] or >
  }
  [ (pIdentifier)
  | *:
  ] or >
  .sEnd
  >>
 ;Block
 >>
;Program
```

# 'else' changes
## Valid test case:
The if_else.pt code is a correct use case of the 'else' statment and had the following output:
```
 .sProgram
 .sIdentifier
 .sParmEnd
  .sBegin
  % .sNewLine
  % .sNewLine
   .sIfStmt
        .sIdentifier
        .sInteger
    .sEq
   .sExpnEnd
   % .sNewLine
   .sThen
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
  .sEnd
```
## Erroneus test case:
The file else_error.pt tested having multiple subsequent else statements. The code had the following output error message:
```
@Program
 ?pUsing (pUsing)
 .sProgram
 ?pIdentifier (pIdentifier)
 .sIdentifier
 [ (pSemicolon)
 | *:
 ] or >
 .sParmEnd
 @Block
  .sBegin
  [ (pSemicolon)
  | pSemicolon:
  % .sNewLine
  % .sNewLine
  ] or >
  }
  [ (pElse)
  | *:
  ] or >
  .sEnd
  >>
 ;Block
 >>
;Program
scan/parse error, line 3: syntax error at: else
```
# 'elsif' changes
## Valid Test Case:
The code below was used to test proper use case of the elsif statment. 
The if_elsif.pt code outputted the following, placing the nested if rule within a .sElse .sBegin and a .sEnd: 
```
 .sProgram
 .sIdentifier
 .sParmEnd
  .sBegin
  % .sNewLine
  % .sNewLine
   .sIfStmt
        .sIdentifier
        .sInteger
    .sEq
   .sExpnEnd
   % .sNewLine
   .sThen
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          % .sNewLine
          .sInteger
     .sExpnEnd
    .sEnd
   .sElse
   .sBegin
    .sIfStmt
         .sIdentifier
         .sInteger
     .sEq
    .sExpnEnd
    % .sNewLine
    .sThen
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
## Erroneus Test Case:
The file elsif_error.pt tests to see if placing an elsif after an else could still function. The code had the following output:
```
@Program
 ?pUsing (pUsing)
 .sProgram
 ?pIdentifier (pIdentifier)
 .sIdentifier
 [ (pSemicolon)
 | *:
 ] or >
 .sParmEnd
 @Block
  .sBegin
  [ (pSemicolon)
  | pSemicolon:
  % .sNewLine
  % .sNewLine
  ] or >
  }
  [ (pIf)
  | pIf:
  @IfStmt
   .sIfStmt
   @Expression
    @SimpleExpression
     [ (pIdentifier)
     | *:
     @Term
      @Subterm
       [ (pIdentifier)
       | *:
       @Factor
        [ (pIdentifier)
        | pIdentifier:
        .sIdentifier
        @IdentifierExtension
         [ (pEquals)
         | *:
         >>
        ;IdentifierExtension
        ] or >
        >>
       ;Factor
       >>
      ;Subterm
      [ (pEquals)
      | *:
      ] or >
      >>
     ;Term
     [ (pEquals)
     | *:
     ] or >
     >>
    ;SimpleExpression
    [ (pEquals)
    | pEquals:
    @SimpleExpression
     [ (pInteger)
     | *:
     @Term
      @Subterm
       [ (pInteger)
       | *:
       @Factor
        [ (pInteger)
        | pInteger:
        .sInteger
        ] or >
        >>
       ;Factor
       >>
      ;Subterm
      [ (pThen)
      | *:
      ] or >
      >>
     ;Term
     [ (pThen)
     | *:
     ] or >
     >>
    ;SimpleExpression
    .sEq
    ] or >
    >>
   ;Expression
   .sExpnEnd
   ?pThen (pThen)
   % .sNewLine
   .sThen
   @Block
    .sBegin
    [ (pIdentifier)
    | pIdentifier:
    @AssignmentOrCallStmt
     [ (pAssignEquals)
     | pAssignEquals:
     .sAssignmentStmt
     .sIdentifier
     @Expression
      @SimpleExpression
       [ (pInteger)
       | *:
       @Term
        @Subterm
         [ (pInteger)
         | *:
         @Factor
          [ (pInteger)
          | pInteger:
          % .sNewLine
          .sInteger
          ] or >
          >>
         ;Factor
         >>
        ;Subterm
        [ (pElse)
        | *:
        ] or >
        >>
       ;Term
       [ (pElse)
       | *:
       ] or >
       >>
      ;SimpleExpression
      [ (pElse)
      | *:
      >>
     ;Expression
     .sExpnEnd
     ] or >
     >>
    ;AssignmentOrCallStmt
    ] or >
    }
    [ (pElse)
    | *:
    ] or >
    .sEnd
    >>
   ;Block
   [ (pElse)
   | pElse:
   % .sNewLine
   .sElse
   @Block
    .sBegin
    [ (pIdentifier)
    | pIdentifier:
    @AssignmentOrCallStmt
     [ (pAssignEquals)
     | pAssignEquals:
     .sAssignmentStmt
     .sIdentifier
     @Expression
      @SimpleExpression
       [ (pInteger)
       | *:
       @Term
        @Subterm
         [ (pInteger)
         | *:
         @Factor
          [ (pInteger)
          | pInteger:
          % .sNewLine
          .sInteger
          ] or >
          >>
         ;Factor
         >>
        ;Subterm
        [ (pElsif)
        | *:
        ] or >
        >>
       ;Term
       [ (pElsif)
       | *:
       ] or >
       >>
      ;SimpleExpression
      [ (pElsif)
      | *:
      >>
     ;Expression
     .sExpnEnd
     ] or >
     >>
    ;AssignmentOrCallStmt
    ] or >
    }
    [ (pElsif)
    | *:
    ] or >
    .sEnd
    >>
   ;Block
   ] or >
   >>
  ;IfStmt
  ] or >
  }
  [ (pElsif)
  | *:
  ] or >
  .sEnd
  >>
 ;Block
 >>
;Program
scan/parse error, line 7: syntax error at: elsif
```

# if elsif else Case
The following code was used to test correct cases where there are subsequent 'elsif's or 'else's after an elsif.
The if_elsif_else.pt code tests the new implementations for if, elsif and else all together and outputted: 

```
 .sProgram
 .sIdentifier
 .sParmEnd
  .sBegin
  % .sNewLine
  % .sNewLine
   .sIfStmt
        .sIdentifier
        .sInteger
    .sEq
   .sExpnEnd
   % .sNewLine
   .sThen
    .sBegin
     .sAssignmentStmt
     .sIdentifier
          % .sNewLine
          .sInteger
     .sExpnEnd
    .sEnd
   .sElse
   .sBegin
    .sIfStmt 
         .sIdentifier
         .sInteger
     .sEq
    .sExpnEnd
    % .sNewLine
    .sThen
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
   .sEnd
  .sEnd
```
