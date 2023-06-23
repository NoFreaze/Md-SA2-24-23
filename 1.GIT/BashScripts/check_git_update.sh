#!/usr/bin/bash
sha256sum log > last_hash
git log --pretty=format:"%h - %an, %ar : %s" --graph --since=100.hours --no-merges > log
sha256sum log > new_hash
if cmp -s last_hash new_hash; then
    echo "Изменений в репозитории не обнаружено"
else
    echo "Репозиторий был изменён"
    mail -s "Обновление в репозитории" terintsov95@mail.ru
fi
