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
SUBFOLDER="$GROUPMACHINE:/cas/student/cisc458a1/cisc458"
echo "Transferring $PKGDIR to $SUBFOLDER..."
scp -r "$PKGDIR" "$SUBFOLDER/$pkgdir_leaf"
echo "Done!"
echo ""
echo ""
# ssh into the system to perform the submit command
echo "Submitting on group machine with SSH..."
ssh $GROUPMACHINE "turnin-cisc458 -v $SUBFOLDER/$pkgdir_leaf"
echo "Done!"
