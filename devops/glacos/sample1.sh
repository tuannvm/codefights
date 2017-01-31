#!/bin/bash

rm -rf root/devops
mkdir -p root/devops
mkdir -p root/devops/cloud


touch mkdir -p root/devops/cloud/start.hint
echo  "Hint\ndown" >> root/devops/cloud/start.hint


mkdir -p root/devops/cloud/dir1

touch mkdir -p root/devops/cloud/dir1/hintFile.txt
echo  "Hint! Well no, not really." >> root/devops/cloud/dir1/hintFile.txt


mkdir -p root/devops/cloud/dir2

touch mkdir -p root/devops/cloud/dir2/notahint.cpp
echo  "Hint\nup down down" >> root/devops/cloud/dir2/notahint.cpp

touch mkdir -p root/devops/cloud/dir2/totallyahint.java
echo  "hint\nup up up" >> root/devops/cloud/dir2/totallyahint.java


mkdir -p root/devops/cloud/dir3

touch mkdir -p root/devops/cloud/dir3/q.hello
echo  "Hint\ndown" >> root/devops/cloud/dir3/q.hello

touch mkdir -p root/devops/cloud/dir3/meh.md
echo  "Hint\nup" >> root/devops/cloud/dir3/meh.md

touch mkdir -p root/devops/cloud/dir3/peh.txt
echo  "A cake is a lie" >> root/devops/cloud/dir3/peh.txt


mkdir -p root/devops/cloud/dir3/secret

touch mkdir -p root/devops/cloud/dir3/secret/congrats
echo  "Hint\n" >> root/devops/cloud/dir3/secret/congrats

