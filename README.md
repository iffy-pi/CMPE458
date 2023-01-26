# CMPE458
Repository for CMPE 458

# Repo Organization
ptsrc/ contains the contents of the tarball (`tar xvf /cas/course/cisc458/pt23/pt23-student.tar.gz`)

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

# Scripts ( /scripts )
## scantrace
Implements the scanner trace command:

```bash
ssltrace "ptc -o1 -t1 -L lib/pt $1" lib/pt/scan.def $2
```

Where:
- `$1` is the test file to pass in (was `test.pt` in the tutorial docs).
- `$2` is the tracing flag ( `-i` for input tokens, `-e` for output tokens)