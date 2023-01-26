#!/usr/bin/env bash
# just runs the scan tracer
# directory of current script to make the command relative to script directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

PTSRC_DIR=$SCRIPT_DIR/../ptsrc
LIB_PT_DIR=$PTSRC_DIR/lib/pt

ssltrace "ptc -o1 -t1 -L $LIB_PT_DIR $PTSRC_DIR/test/test.pt" $LIB_PT_DIR/scan.def -i