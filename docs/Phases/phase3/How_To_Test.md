- The first step is to check if the SSL trace generates any output errors (so you can use the grep for errors or check the tutorial 6 for it)
- If there are no errors in the SSL trace, you can verify program correctness by looking at the T-codes outputted for the Pascal program
	- That is, write the equivalent code in Pascal and run SSL trace on it (you can  use build or ptsrc-ref for this) and then compare the generated T-codes, if they are the same then we know the program is correct
	- This is applicable from language modifications that come from Quby, new features (such as Strings, and modules and such) might not be tested that way
- For new changes, you would have to look at the output and verify that it works semantically, or is at least close to the expectation for semantic output

- For testing we would be doing
	- Verifying the old functionality
		- Assignment of variables
		- Binary operation
		- Ternary operation
		- Unary operation
		- If statement
		  Else statement
	- Testing the new functionality
		- iF-ELSE behaviour
		- do statement
		- module functionality
		- public procedures
		- case else statement modification
	- String handling
		- String operations
		- Handling string literals
		- Handling string constants
		- String equality and inequality
		- New string traps