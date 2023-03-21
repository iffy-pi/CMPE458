## Overview

- Removed support for `repeat` statement
- Added support for `do` loop
- Added support for `else` statement in `case`
- Removed support for multiple constant definitions in one line

### `repeat` statement

This change does not have much involved with it. All that was required here was deleting artifacts of the RepeatStmt rule and its detection in 'semantic.ssl'.

### `do` loop
 
This change primarily required adding in a new rule, `DoStmt`. First, in the `Block` rule, the `DoStmt` rule is called upon detection of an `sDo` token. Upon this the rule continually allows for either regular statements with the `Statement` rule and interspersed `break if` statements that will be bounded by the T-codes `tDoBreakIf` and `tDoTest`. Finally, the loop is terminated with a `tDoEnd` token.


### `case` statement

The majority of the `case` statement handling from PTPascal is used again in this phase. This is because in the previous phase of the compiler the body of the statement (with exception of the `else`) is emitted in a way to mimick the output of that of PTPascal. To handle the new `else` statement, a loop is added to the rule to check for regular case alternative and `else` statements, as well as an `sCaseEnd` token to terminate the statement. Upon detection of the `sElse` token, the `.tCaseEnd` token is emitted so the body of the case statement can be emitted exactly as before. After this, the else statement is emitted and a branch added in the case statement, ending in the consumption of the `sCaseEnd` token from the previous step. Thus, effectively making the `else` statement seem separate from the `case` statement making its handling more similar to that previously done in PTPascal.

### Multiple constant definitions

This change was a relatively simplistic one as there exists a rule already called `ConstantDefinitions` which was promptly renamed to `ConstantDefinition` now. in the rule before, a loop was used to gather all the declared constants. To support only a single definition, this loop was removed and replaced with its body, so now only a single identifier and subsequent assignment is accepted.
