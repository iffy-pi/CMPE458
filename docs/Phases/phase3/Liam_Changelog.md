# Liam Changelog

## ModuleDefinition rule

### New Symbol Table additions

syModule and syPublicProcedure were added to the Symbol table for identifying and treating Modules and PublicProcedures. This allows them to be added to the Symbol stack when identified.

### ModuleDefinition rule

The ModuleDefinition rule was added to the rule section of Semantic.ssl. The module rule is used to consume sModule and then add the subsequent symbol to the symbol stack as a Module. Modules don't take in parameters, so we don't call the `@ProgramParameter` rule. Instead, the `@Block` rule is called to handle all declarations within the module. The oSymbolTblStripScope and oSymbolTblMergeScope are then used to promote all public symbols to the enclosing scope.
        
## Public Procedure Handling

The Public procedure handling is done by picking up the `sPublic` output token from the semantic analizer when a procedure is being defined. Then, in the `@ProcedureDefinition` rule, we set the type of procedure it is on the symbol stack by using the case:
```
[
    | sPublic:
            oSymbolStkSetKind(syPublicProcedure)
    | *:
            oSymbolStkSetKind(syProcedure)
]
```