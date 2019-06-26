#!/usr/bin/env sh

set -e

npm run .vuepress:build

# navigate to docs

cd .vuepress/dist

git init
git add -A 
git commit -m "deploy"

# deploying based on repo name

git push -f git@github.com:sodrooome/diy.git master:gh-pages

cd -