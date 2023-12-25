import yadisk
import os

client = yadisk.Client(
    token="y0_AgAAAAAO6Ho-AAsJeAAAAAD1uS2d9qJOrDMsQO-l8V5it22P-aSNJUY"
)

if __name__ == "__main__":
    with client:
        # Проверяет, валиден ли токен
        print(client.check_token())

        # print(client.mkdir("/db_backups"))
        # # Получает общую информацию о диске
        print(client.get_disk_info())
        #
        # # Выводит содержимое "/some/path"
        #
        # # Загружает "file_to_upload.txt" в "/destination.txt"

        print(list(client.listdir("/rgz_db_backup")))
        for file in os.listdir(
            "/home/a1nsworth/programming/Python/EducationalProjects/DataBase/AirTransportationDRF/backups"
        ):
            with open(file, "w+") as f:
                client.upload(f, f"/rgz_db_backup/{f.name}", overwrite=True)
        # #
        # # # То же самое
        # # with open("file_to_upload.txt", "rb") as f:
        # #     client.upload(f, "/destination.txt")
        # #
        # # # Скачивает "/some-file-to-download.txt" в "downloaded.txt"
        # # client.download("/some-file-to-download.txt", "downloaded.txt")
