#!/bin/bash
echo core >/proc/sys/kernel/core_pattern
sed -i "s/gcc/afl-gcc/g" $1
sed -i "s/g++/afl-g++/g" $1
sed -i "s/clang/afl-clang/g" $1
sed -i "s/clang++/afl-calng++/g" $1
afl-fuzz -i /in -o /out path/to/program
