## Person Breakdown
- Iffy
	- coder.ssl: 1,2,3,4,6 - Done
	- coder.pt: 1,2,4,5,6 - Done
	- tLiteralString - Iffy - Done
	- tFetchString - Iffy - Done
	- tAssignString - Iffy - Done
		- OperandAssignStringPopPop - Done
		- Also do coder.ssl #8 - Done
	- tStoreString - Iffy - Done
- Ethan
	- coder.ssl #5: Block rule updates - Ethan
	- tConcatenate - Ethan
		- OperandConcatenatePop
	- tIndex - Ethan
		- OperandIndexPop
	- tChr - Ethan
		- OperandChr
		- coder.ssl #10 : Removed optimzied case for tChr (I think it is referring to optimizing rule OperandChrAssignPopPop)
- Noah
	- tSubstring - Noah
		- OperandSubstringPopPop
	- tStringEqual - Noah
		- OperandStringEqualPop
	- coder.ssl #13 : Do statements modification - Noah
	- coder.ssl #14: Case statement else modification - Noah
- Liam
	- tSubscriptString - Liam
		- Also do coder.ssl #9
		- Also do coder.pt #3
	- tLength - Liam
		- OperandLength
	- tOrd - Liam
		- OperandOrd
		- coder.ssl #10: Removed Optimized case for Tord

## TODOs Full List
- coder.ssl #5: Block rule updates - Ethan
- coder.ssl #7, #8, #9
	- tLiteralString - Iffy
	- tFetchString - Iffy
	- tAssignString - Iffy
		- OperandAssignStringPopPop
		- Also do coder.ssl #8
	- tStoreString - Iffy
	- tSubscriptString - Liam
		- Also do coder.ssl #9
		- Also do coder.pt #3
	- tConcatenate - Ethan
		- OperandConcatenatePop
	- tSubstring - Noah
		- OperandSubstringPopPop
	- tIndex - Ethan
		- OperandIndexPop
	- tLength - Liam
		- OperandLength
	- tChr - Ethan
		- OperandChr
		- coder.ssl #10 : Removed optimzied case for tChr (I think it is referring to optimizing rule OperandChrAssignPopPop)
	- tOrd - Liam
		- OperandOrd
		- coder.ssl #10: Removed Optimzized case for Tord
	- tStringEqual - Noah
		- OperandStringEqualPop
	- tTrap trReadString
		- N/A if we did things right
	- tTrap trWriteString
		- N/A if we did things right
- coder.ssl #11 is just general for handling traps
- coder.ssl #13 : Do statements modification - Noah
- coder.ssl #14: Case statement else modification - Noah