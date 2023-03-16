#Ethan Tasks

Semantic.ssl: 10 12 18 19

10. Merge the alternatives of the Statement rule into the Block rule and modify the Statement rule to push a new scope, call the Block rule, then pop the scope.
11. Modify the handling of type definitions to allow only one per definition
12. Add handling of the string index operator (?) to the BinaryOperator rule. Be careful to get type checking right.
13. Add handling of string concatenation to the sAdd part of the BinaryOperator rule. Remember strings are first class values in Quby, so string concatenation is just like integer addition in terms of what to do, but different t-codes.

DONE: 10, 12, 18, 19

Semantic.pt: 4

4. Add cases for the new semantic operations oSymbolTblStripScope and oSymbolTblMergeScope to the SslWalker.

The implementation of oSymbolTblStripScope is like oSymbolTblPopScope except that it should not decrement the lexical level. That is, it just changes all the identSymbolTblRefs for the symbols in the top scope to their symbolTblLink values, and that's all. (This has the effect of removing them from visibility even though they are technically still in the table. A bit of a hack, but easy and correct.) Unlike oSymbolTblPopScope, be careful not to change symbolTableTop, typeTableTop and lexicLevelStackTop in oSymbolTblStripScope since we’re don’t want to remove anything from the tables in this case. The implementation of oSymbolTblMergeScope is easy - it just has to decrement the lexical level without changing any ident links.

DONE: 4
