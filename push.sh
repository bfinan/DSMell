# YOLOs a push to master

git pull
git add .
git status
# commit with today's date as the commit message, plus a semantic tidbit
git commit -m "$(date +%Y-%m-%d) $1"
git push


