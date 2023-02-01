# Phase 1 Testing Documentation
All files referred to are in ptsrc/test.

## Testing hash
The test file hash.pt is testing for hash in Quby.
The following is the output from running scantrace on hash.pt.
```
@Scan
 [ (lHash)
 | lHash:
 .pHash
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
```

## Testing exclamation
The test file exclamation.pt is testing for not (!) in Quby.
The following is the output from running scantrace on exclamation.pt.
```
@Scan
 [ (lExclamation)
 | lExclamation:
 [ (lEndFile)
 | *:
 .pNot
 ] or >
 }
 [ (lEndFile)
 | lEndFile:
 .pEndFile
 ```

 ## Testing comments 
The test file comments.pt is testing for comments in Quby.
The following is the output from running scantrace on comments.pt.
```
@Scan
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lPercent)
 | lPercent:
 @Comment
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lNewLine)
  | lNewLine:
  .pNewLine
  ] or >
  >>
 ;Comment
 ] or >
 }
 [ (lNewLine)
 | lNewLine:
 .pNewLine
 ] or >
 }
 [ (lPercent)
 | lPercent:
 @Comment
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lBlank)
  | *:
  ? (lBlank)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lLetter)
  | *:
  ? (lLetter)
  }
  [ (lEndFile)
  | lEndFile:
  .pEndFile
```