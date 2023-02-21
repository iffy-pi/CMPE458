# Testing documentation for sections done by Liam

All testing documentation used can be found in /ptsrc/test/phase-2/liam/

# if changes
The pt code used to test the if statements can be found in /ptsrc/test/phase-2/liam/if.pt

If statmentents were changed such that they call the block rule after the expression decleration. This encapsulates the following
code in sBegin and sEnd. 

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

# else changes
The else was changed so that instead of calling the statement rule, it calls the Block rule after emiting sElse.
This way the following declerations are encapsulated by sBegin and sEnd. After the Block rule, the code then exits the 
If rule. 

The if_else.pt code had the following output:
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
# elsif

elsif was added to the parser in a way such that it behaves as a nested if statement. Following an if statement, if an elsif
follows, the code will emit an sElse, and then within the else, the If rule is called again.

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
# if elsif else case

When having an if, followed by elsif, followed by a else statment, the elsif is encapsulated in the first if statments else. Then the 
subsequent else is incapsulated by the nested if statements sBegin and sEnd tokens. The below code shows how the else is nested along
with the elsif. 

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
