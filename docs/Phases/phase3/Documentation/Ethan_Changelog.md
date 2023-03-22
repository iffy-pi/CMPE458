# Ethan Changelog

## Block Rule Changes
Modified the statement and block rules so that the alternatives of the statement rule are performed by the block rule, while the statement rule simply pops and pushes the scope.

## Type Definition Modifications
Type definition handling has been updated to support only one per definition.

## Changes to Binary Opartor Handling
The string index operator was added to the BinaryOperator rule, as well as the string concatenation operator, which was added to the sAdd section.

## New Symbol Table Semantic Operations
The new semantic operations `oSymbolTblStripScope` and `oSymbolTblMergeScope` were added to the `SymbolTable` semantic mechanism. These replace the `oSymbolTblPopScope` operation from PT Pascal.