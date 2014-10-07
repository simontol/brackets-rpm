#!/bin/sh

rm -rf brackets
rm -rf brackets-shell

git clone https://github.com/adobe/brackets.git
git clone https://github.com/adobe/brackets-shell.git

cd brackets && git checkout release-$1 && git submodule update --init && rm -rf .git && cd ..
cd brackets-shell && git checkout release-$2 && git submodule update --init && rm -rf .git && cd ..

tar -cvzf SOURCES/brackets-$1.tar.gz brackets
tar -cvzf SOURCES/brackets-shell-$2.tar.gz brackets-shell

rm -rf brackets
rm -rf brackets-shell
