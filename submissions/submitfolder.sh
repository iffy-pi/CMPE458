#!/usr/bin/env bash
# submits the specified directory to the group account correct folder
# will need to know the group account password
if (( $# < 1 )) ; then
    echo "Must specify the directory to submit"
    exit 0
fi

PKGDIR=$1

if [[ ! -d $PKGDIR ]]; then
    echo "$PKGDIR is not a directory!"
    exit 1
fi

GROUPMACHINE="cisc458a1@linux2.caslab.queensu.ca"

#then get the parent directory
pkgdir_parent=`echo $PKGDIR | sed -e 's#\(.*\)\(/.*\)#\1#'`
#youngest directory, last directory in the path name
pkgdir_leaf=`echo $PKGDIR | sed -e 's#\(.*/\)\(.*\)#\2#'`

# transfer the file to the group account with scp
LOCALSUBFOLDER="/cas/student/cisc458a1/cisc458"
REMOTESUBFOLDER="$GROUPMACHINE:/cas/student/cisc458a1/cisc458"

echo "Transferring $PKGDIR to $LOCALSUBFOLDER..."
ssh $GROUPMACHINE 'if [[ -d '$LOCALSUBFOLDER/$pkgdir_leaf' ]]; then rm -rf '$LOCALSUBFOLDER/$pkgdir_leaf' && echo Deleted previous version!; else echo no match!;  fi'
scp -r "$PKGDIR" "$REMOTESUBFOLDER/$pkgdir_leaf"
echo "Done!"
echo ""
echo ""

# ssh into the system to perform the submit command
echo "Submitting on group machine with turnin through SSH..."
ssh $GROUPMACHINE "cd $LOCALSUBFOLDER && turnin-cisc458 -v $pkgdir_leaf"
echo "Done!"
