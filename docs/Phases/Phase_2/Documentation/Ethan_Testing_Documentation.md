# Ethan Testing

Testing is split into three sections, the testing for procedures, that for modules, and the final section which deals with program parsing more broadly.

All test files can be found in ptsrc/test/phase-2/ethan.

## Procedures

While the general logic for the procedures in Quby is similar to PT Pascal, changes were made to syntax and functionality, so testing is necessary.

### Public

The Phase 2 specifications state that the sPublic token must be emitted after the procedure sIdentifier. Tests for public procedures with and without parameters are shown below.

#### Without Parameters

The test file used to generate the following output is *public_def.pt*.
```
 .sProgram
 % .sNewLine
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sProcedure
  .sIdentifier
  .sPublic
   .sIdentifier
   .sIdentifier
   .sParmEnd
   .sBegin
   .sEnd
  .sEnd
```
As shown above, the sPublic token is emitted successfully and in the right place.

#### With Parameters

The test file used to generate the following output is *public_def_with_params.pt*.
```
 .sProgram
 % .sNewLine
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sProcedure
  .sIdentifier
  .sPublic
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sVar
   .sIdentifier
   % .sNewLine
   .sParmEnd
   .sBegin
   .sVar
    .sIdentifier
      % .sNewLine
      .sIdentifier
    .sAssignmentStmt
    .sIdentifier
         % .sNewLine
         .sIdentifier
    .sExpnEnd
   % .sNewLine
   .sEnd
  .sEnd
```
As shown above, the sPublic token is emitted successfully and in the right place. In addition, all parameters are identified successfully and in the right order. The begin and end tokens appear in their appropriate locations, and statements within procedures are recognized.

### Private

The private procedures are identical to public procedures less the sPublic token, and are processed identically as is shown below.

#### Without Parameters

The test file used to generate the following output is *private_def.pt*.
```
 .sProgram
 % .sNewLine
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sProcedure
  .sIdentifier
   .sIdentifier
   .sIdentifier
   .sParmEnd
   .sBegin
   .sEnd
  .sEnd
```

#### With Parameters

The test file used to generate the following output is *private_def_with_params.pt*.
```
 .sProgram
 % .sNewLine
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
  .sProcedure
  .sIdentifier
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sVar
   .sIdentifier
   % .sNewLine
   .sParmEnd
   .sBegin
   .sVar
    .sIdentifier
      % .sNewLine
      .sIdentifier
    .sAssignmentStmt
    .sIdentifier
         % .sNewLine
         .sIdentifier
    .sExpnEnd
   % .sNewLine
   .sEnd
  .sEnd
```

## Modules

Primary testing and design of the module was carried out by Liam, so the testing in this segment is limited to the functionality of the sPublic token, which will be shown below.

### Public

Modules can only be accessed when declared public in Quby, so ensuring sPublic tokens are emitted is essential.

The test file used to generate the following output is *public_module.pt*.
```
 .sProgram
 % .sNewLine
 % .sNewLine
 .sIdentifier
 .sParmEnd
  .sBegin
   .sModule
   % .sNewLine
   .sIdentifier
   .sPublic
    .sBegin
    .sVar
     .sIdentifier
       % .sNewLine
       .sIdentifier
    % .sNewLine
    .sEnd
  .sEnd
```
As shown above, both the sPublic and sModule tokens are emitted correctly and in proper order.

### Private

Testing of private modules can be seen in Liam's test doc, which will presumably be merged with this one so I guess plug his stuff into this segment

## Routine Recognition

This section pertains to the correct parsing of a complete and correct Quby program containing multiple procedures and/or modules with variables and parameters. The specified procedures/modules have varied visibility to make the test more realistic, though the primary aim is to ensure procedures and modules are recognized more broadly, which is shown below.

The test file used to generate the following output is *full_routine.pt*.

```
 .sProgram
 % .sNewLine
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
    % .sNewLine
    % .sNewLine
    .sInteger
  .sProcedure
  .sIdentifier
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sIdentifier
   .sVar
   .sIdentifier
   % .sNewLine
   .sParmEnd
   .sBegin
   .sVar
    .sIdentifier
      % .sNewLine
      .sIdentifier
    .sAssignmentStmt
    .sIdentifier
         % .sNewLine
         .sIdentifier
    .sExpnEnd
   % .sNewLine
   % .sNewLine
   .sProcedure
   % .sNewLine
   .sIdentifier
   .sPublic
    .sParmEnd
    .sBegin
    .sVar
     .sIdentifier
       % .sNewLine
       .sIdentifier
    % .sNewLine
    % .sNewLine
     .sModule
     % .sNewLine
     .sIdentifier
     .sPublic
      .sBegin
      .sVar
       .sIdentifier
         % .sNewLine
         .sIdentifier
      % .sNewLine
      .sEnd
    .sEnd
   .sEnd
  .sEnd
```
