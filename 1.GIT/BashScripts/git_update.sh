#!/bin/bash
git pull origin
echo 'Удаленный репозиторий загружен'
date=$(date '+%Y-%m-%d')
git branch $date
echo 'Ветка $date создана'
git checkout $date
git add .
git commit -m 'Обновление файлов с локального репозитория:$date'
git push -u origin $date
echo 'Скрипт завершил работу'
