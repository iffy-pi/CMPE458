# Iffy Tasks
## TODO
- Testing for declarations
	- Test constants
		- Valid constant declaration
		- Invalid constant declaration
			- Improper operator or keyword
			- Improper value
			- Comma separated constants
	- Test type declaration
		- Valid type declarations
		- Invalid type declarations
			- Using wrong operator or keyword
			- Comma separated types
	- Test variable declarations
		- Testing valid variable declarations
			- Comma separated declarations
		- Invalid variable declarations
			- Missing keyword operators
			- Invalid comma separation

- Testing other syntactic details
	- Testing new not equals
	- Testing new comparison equals

- Testing string precedence
	- Test the addition of the new operators individually
		- Testing $ (substring)
		- Testing # (length)
		- Testing ? (index)
	- Validating precedence tests
		- Making sure precedence rules are applied at each level of precedence
		- Constructing parse trees to match 


## DONE
- Update declarations ***Iffy***
	- Modify constant, type and variable to meet the language spec
	- To assist the semantic phase, if there is more tha
- Modify the string type - ***Iffy***
	- Add new operators in the required precedence rules
- Syntactic details ***Iffy***
	- Replace pColonEquals with pAssignEquals
	- Everything else **should** be fine.
