#!/bin/bash
echo core >/proc/sys/kernel/core_pattern
./configure CC="afl-clang" CXX="afl-clang++"
make
afl-fuzz -i $1 -o $2 $3 $4 $5
