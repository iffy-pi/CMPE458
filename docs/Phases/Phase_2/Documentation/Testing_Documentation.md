# Testing Documentation
All files referred to are in ptsrc/test/phase-2.

The testing document also uses the term parsetrace, this is a short form referring to using the SSL trace command on our built compiler up to th eparser phase.

For example, running parsetrace on test.pt is equivalent to:

```
ssltrace "ptc -o2 -t2 -L CMPE458/ptsrc/lib/pt test.pt" CMPE458/ptsrc/lib/pt/parser.def -e
```

This was implemented with a shell script.

# Iffy testing
- Test declarations
    - Constants
    - Types
    - Variables
- Syntax changes
    - Not operator
    - Not equals
    - Assignment operator
    - Comparison operator
- String operations
    - Substring ($)
    - Index (?)
    - Length (#)
    - Testing parsing of expressions
    - Verifying it obeys specified precedence