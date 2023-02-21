# Testing documentation for sections done by Liam

All testing documentation used can be found in /ptsrc/test/phase-2/liam/

# 'module' testing

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


# 'while' testing

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


# 'if' testing
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

# 'else' changes

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
# 'elsif' changes
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
