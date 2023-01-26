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