import shutil

shutil.copy("source.txt", "backup.txt")
shutil.move("backup.txt", "archive/backup.txt")