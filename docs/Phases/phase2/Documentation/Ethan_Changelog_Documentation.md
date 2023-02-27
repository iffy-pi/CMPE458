# All Changes made by Ethan and how they were implemented

- Updated the block rule with new rules and removed old rules
- Removed the begin rule while maintaining the emission of begin tokens
- Merged the statement rule into the block rule to make it more generally applicable
- Added indication of public function token emission (created sPublic token)
- Maintained PT-style emission of sBegin and sEnd tokens to minimise changes needed during semantic analysis


# Block Rule additions

All removed keywords were taken out of the block rule or replaced with their Quby counterparts if a direct counterpart existed (i.e. procedure -> def). For new Quby keywords with no direct counterparts, corresponding rules were added.

The statement rule was removed entirely, as Quby makes no distinction between declarations and statements. The statement rule was integrated into the block rule to simplify routine parsing as a whole, so that the block rule was the primary rule crawling for the parser.

Another change to the Block rule was making sure to consume pEnd tokens, or else only the first procedure/module would be recognized.

# Routine Handling changes

To simplify semantic analysis changes for Quby implementation, the parser still emits sBegin and sEnd tokens at the beginning of every block. This was implemented through modifications to the block and statement rules, so that any block of Quby will be interpreted similarly to PT Pascal in semantic analysis.

While sBegin tokens are still emitted, the BeginStmt rule for handling the actual begin keyword has been removed.

# Procedure/Module handling changes

While the general form of the module rule was handled by Liam, and the procedure rule remains mostly the same as in PT Pascal, there are a couple key changes that fall under routine handling. A major change was the inclusion of the sPublic token, and subsequent changes to accomodate. For the procedure rule, changes were made within the block rule to allow for public procedures, and smeicolons were removed in the ProcedureHeading rule. For modules, due to the construction of the rule, changes were made to the module rule directly, though the form of the change was similar to that of the procedure change in the block rule.
