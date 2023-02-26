# Change Log Documentation (Noah)
## Overview

- Removed `repeat` statement
- Added support for `do` statement
- Modified `case` statement syntax
- Added support for `unless` statement

# `repeat` Statement

This keyword was removed from the parser. To do this, the checks for the `repeat` keyword were removed from the `Block` rule along with the corresponding rule, `RepeatStmt`.

# `do` Statement

The `do` statement is a purely additive addition to the parser that has the following syntax. 
```
do
    % ... body of do loop
    
    % strictly one or more `break if` statements
    % within the body of the `do` loop are required
    break if <condition>

    % ... body of do loop
end
```
To implement this, a keyword check is performed within the `Block` rule. After which, the corresponding `DoStmt` rule is called. At the start of the rule, a `.sDo` is emitted. All statements around `break if` statements are handled by the `Block` rule. While the `break if` statement emits a `.sBreakIf` token, followed by a condition. The `do` statement is finally terminated with a `.sEnd` token.

Since this is an additive change to the language, further changes will need to be made in the semantic phase of the compiler to support this feature.

# `unless` Statement

The `unless` statement is a new addition to the Quby language that has the following syntax. 
```
unless <condition> then
    % body of unless statement
end
```
This behaves semantically the same as an `if not <condition>`. Since this statement is purely syntactic sugar, it can be fully implemented into Quby by only applying change to this stage of the compiler, the parser. To do this, first a check for the keyword `unless` is added for the `Block` rule along with a call to the corresponding `UnlessStmt` rule if found. This rule then emits the same contents as an `if` statements, except with the addition of the emission of an `.sNot` token at before terminating the expression.

# `case` Statement

The `case` statement was a modifying change to the language which changes the syntax for the statements in Quby and adding a default branch to exit the statement with an `else`. These statement will have the following syntax.
```
case <expression>
    when <condition> then
        % `when` body
    when <condition> then
        % `when` body
    else
        % `else` body
end
```

For this statement to be syntactically valid, there must be at least 1 `when` condition in a case statement always, and that `when` statement may be accompanied 1 or more additional `when` statements and at most 1 `else` statement that acts as a default branch to exit the case statement. 

This statement behaves similar to the `case` statement before but has some major changes. Firstly, the requirement for an `of` keyword after the initial expression is removed. Meanwhile, the `when` statements are purely syntactic sugar for the previous case checking syntax in PT Pascal. These statements emit the same thing as previously to the semantic phase of the compiler while consuming the token `when` before the condition and the token `then` after the condition from the scanner. The `else` branch of the new `case` statement by contract will require additional support in the semantic phase of the compiler as this feature is not currently supported. When the `else` keyword is encountered, a corresponding `.sElse` token is emitted to the next phase of the compiler, followed by the contents of the following `Block` rule called as the body of the `else` statement.

