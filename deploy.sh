#!/usr/bin/env sh

set -e

npm run .vuepress:build

# npm run docs:build

# navigate to docs

cd .vuepress/dist

# cd docs/.vuepress/dist

git init
git add -A 
git commit -m "deploy"

# deploying based on repo name

git push -f git@github.com:sodrooome/diy.git master:gh-pages

# deploying based on github account

# git push -f git@github.com:sodrooome/sodrooome.github.io.git master

cd -