# Testing documentation for sections done by Liam

All testing documentation used can be found in /ptsrc/test/phase-2/liam/

# 'module' changes

Added functionality to parser to handle modules in Quby in the Block rule. First, whithin the Block rule the string 'module' is 
consumed then the Module rule is called. A .sModule is emited to signify that the following sIdentifier should be correlated to a module and then the Block rule is called for all subsequent declarations and statmenets to be encapsulated. The module is ended
when a end is placed at the end of the declarations. 

The code module.pt in the /ptsrc/test/phase-2/liam/ directory outputted:

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
# 'while' changes

While loops were changed to fit the new changes made to ptPascal. Instead of using the Statment rule for encapsulation, the Block rule
is now used. while loops still emit the same tokens as before. Handling while loops with Quby specifications will need to be done in the semantic phase. 

The code from while.pt outputted the following. 

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


# 'if' changes
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

# 'else' changes
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
# 'elsif' changes

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
# if elsif else Case

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
