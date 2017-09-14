#!/bin/bash

set -o errexit -o nounset

rev=$(git rev-parse --short HEAD)

cd _site

git init
git config user.name "ashley williams"
git config user.email "ashley666ashley@gmail.com"

git remote add upstream "https://$GH_TOKEN@github.com/rust-community/rustbridge-www.git"
git fetch upstream
git reset upstream/master

touch .

git add -A .
git commit -m "rebuild pages at ${rev}"
git push -fq upstream HEAD:master
