#!/bin/sh

cd ..

PATH_SAVE_TAR_GZ=backups_archive/backups_archive.gz
PATH_BACKUPS=backups

tar -czf "$PATH_SAVE_TAR_GZ" "$PATH_BACKUPS"

FILEPATH=$PATH_SAVE_TAR_GZ

FILENAME="${FILEPATH##*/}"

TOKEN='y0_AgAAAAAO6Ho-AAsJeAAAAAD1uS2d9qJOrDMsQO-l8V5it22P-aSNJUY'

# Простая функция для парсинга свойств из JSON
function parseJson
{
    local output
    regex="(\"$1\":[\"]?)([^\",\}]+)([\"]?)"
    [[ $2 =~ $regex ]] && output=${BASH_REMATCH[2]}
    echo $output
}

# Функция для отправки файла
function sendFile
{
    echo "Start sending a file: $1"

    # Получаем URL для загрузки файла
    sendUrlResponse=`curl -s -H "Authorization: OAuth $TOKEN" https://cloud-api.yandex.net:443/v1/disk/resources/upload/?path=app:/$FILENAME&overwrite=true`
    sendUrl=$(parseJson 'href' $sendUrlResponse)

    # Отправляем файл
    sendFileResponse=`curl -s -T $FILEPATH -H "Authorization: OAuth $TOKEN" $sendUrl`

    echo "Completing a file upload: $1"
}

sendFile $FILEPATH