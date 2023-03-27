# CMPE458
Repository for CMPE 458

# Repo Organization
ptsrc/ contains the contents of the tarball (`tar xvf /cas/course/cisc458/pt23/pt23-student.tar.gz`)

ptsrc-ref/ is the same extraction, is included to be just a reference of the original state of the files.

# Running Pascal
To run the local library ( created at ptsrc/lib/pt), you must specify it with the `ptc` command:

```
ptc -L ptsrc/lib/pt <source file>
```

You can also add it as an alias to your bash profile, and can then use the command `ptccl` instead of `ptc`.

```
alias ptccl='ptc -L ptsrc/lib/pt'
```

If adding as an alias, remember to use full location.

To load the alias, you must run:

```
source ~/.bash_profile
```

which can be run automatically by adding it to your ~/.bashrc file.

## Building Compiler
You can rebuild the compiler by running:

```
make clean
make scanner
```

Where `scanner` can be replaced with whatever make tag.

# Scripts ( /scripts )
## scantrace
Implements the scanner trace command:

```bash
ssltrace "ptc -o1 -t1 -L lib/pt $1" lib/pt/scan.def $2
```

Where:
- `$1` is the test file to pass in (was `test.pt` in the tutorial docs).
- `$2` (optional) is the tracing flag ( `-i` for input tokens, `-e` for output tokens)

# parser_def_paster
Handles the pasting of the scan.def and parser.def content into parser/parser.pt (Tutorial 2 Page 4)

Run it with:

```
python parser_def_paster.py
```

Note: You should first make the scanner (`make scanner`) and then run the paste script. You can verify everything is pasted correctly by making the scanner again (it should not give any errors this time).

## Using semtrace and ptsemtrace
These are the designed ssltrace script for semantic section. `ptsemtrace` is the ssltrace for the Pascal compiler (using build/ptsrc/lib/pt). `semtrace` is the ssltrace for the Quby compiler (using ptsrc/lib/pt).

You can use `ptsemtrace` to see the generated t-codes for the pascal compiler, and then use `semtrace` for the generated t-codes on Quby. You can then compare the two for validation.

Script usage information (applies to both scripts):
```
semtrace <file> [<flag>]
    <file> : required : file address : file to ssltrace on
    <flag> : optional : string       : Flag to use to change trace behaviour

Default behaviour prints out emitted tokens.
```

Supported flags:
- `-ge`: Check the ssltrace output for errors using grep
- `-o`: Print emitted tokens and semantic operations (like trace in Tutorial 6)
- `-a`: Print entire trace (including branching and stuff)
- `-u`: Token output for default is automaticaally stripped, use this flag to keep unstripped
- Can also specify any other flag, which will be passed through to ssltrace e.g. `-i` to print input tokens

# Using codetrace and ptcodetrace
Same as `semtrace` and `ptsemtrace` but just for the code generation phase instead, with some new flags:

```
codetrace <file> [<flag>]
    <file> : required : file address : file to ssltrace on
    <flag> : optional : string       : Flag to use to change trace behaviour

Default behaviour prints out emitted tokens, and deletes generated assembly file (if it did not exist before call to codetrace)
```

Supported flags:
- `-ge`: Check the ssltrace output for errors using grep
- `-o`: Print emitted tokens and semantic operations (like trace in Tutorial 6)
- `-a`: Print entire trace (including branching and stuff)
- `-as`: Print the generated assembly code
- `-asf`: Print the generated assembly code and also keep the generated assembly code file
- `-f`: Keep the generated assembly code file
- `-d` : Delete the generated assembly code file, even if it existed before
- `-u`: Token output for default is automaticaally stripped, use this flag to keep unstripped
- Can also specify any other flag, which will be passed through to ssltrace e.g. `-i` to print input tokens


# Using qbasm and ptasm
These are scripts that generate the assembly instructions for a given Quby and PT file respectively. `qbasm` uses the Quby compiler (in ptsrc/lib/pt) while `ptasm` uses the PT compiler (in build/ptsrc/lib/pt)

Script usage is shown below (applies to both scripts):

```
qbasm <file> [<flag>]
    <file> : required : file address : PT file to compile
    <flag> : optional : string       : Flag to use to change trace behaviour
```

Supported flags:
- `-o`: Instead of saving to `.s` file, outputs the assembly instructions in console