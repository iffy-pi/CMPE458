# All Changes made by Liam and how they were implemented

- Added 'module' to parser
- 'while' loop updated to work with new changes to Block rule
- 'if' statement changes
- 'else' statement changes
- 'elsif' statement changes

# 'module' changes

Added functionality to parser to handle modules in Quby in the Block rule. First, whithin the Block rule the string 'module' is 
consumed then the Module rule is called. A .sModule is emited to signify that the following sIdentifier should be correlated to a module and then the Block rule is called for all subsequent declarations and statmenets to be encapsulated. The module is ended
when a end is placed at the end of the declarations. 

# 'while' loop changes

While loops were changed to fit the new changes made to ptPascal. Instead of using the Statment rule for encapsulation, the Block rule
is now used. while loops still emit the same tokens as before. Handling while loops with Quby specifications will need to be done in the semantic phase. 

# 'if' statment changes 

If statmentents were changed such that they call the block rule after the expression decleration. This encapsulates the following
code in sBegin and sEnd. 

# 'else' statement changes

The else was changed so that instead of calling the statement rule, it calls the Block rule after emiting sElse.
This way the following declerations are encapsulated by sBegin and sEnd. After the Block rule, the code then exits the 
If rule. 

# 'elsif' statement changes

elsif was added to the parser in a way such that it behaves as a nested if statement. Following an if statement, if an elsif
follows, the code will emit an sElse, and then within the else, the If rule is called again. In the case that the if statment and subsequent elsif statment, is ended with an else statement. The elsif is nested within the if statments else. And then the else statmenet is applied to the nested if statement created by the elsif. 
 ```
if x == 1 then
    x = 0
elsif x == 2 then
    x = 1
else 
    x = 2
end
 ```
 is the equivalent of 
  ```
if x == 1 then
    x = 0
else
    if x == 2 then
        x = 1
    else 
        x = 2
    end
end
 ```