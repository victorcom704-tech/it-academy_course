import os
import shutil

# 1
# current_dir = os.path.dirname(os.path.abspath(__file__))


# src = os.path.join(current_dir, "settings.ini")
# dst = os.path.join(current_dir, "settings_backup.ini")

# shutil.copy(src, dst)
# print("Файл скопирован")

# 2
# current_dir = os.path.dirname(os.path.abspath(__file__))
# src_log = os.path.join(current_dir, "app.log")
# target_dir = os.path.join(current_dir, "logs_backup")
# if not os.path.exists(target_dir):
#     os.makedirs(target_dir)

# shutil.copy(src_log, target_dir)
# print("файл скопирован в папку")

# 3
# current_dir = os.path.dirname(os.path.abspath(__file__))
# current_project = os.path.join(current_dir, "project")
# backup_project = os.path.join(current_dir, "project_backup")
# if os.path.exists(backup_project):
#     shutil.rmtree(backup_project)
#     print("Старый бэкап удален")

# shutil.copytree(current_project, backup_project)
# print("Папка скопирована")

# 4
# current_dir = os.path.dirname(os.path.abspath(__file__))
# report_file = os.path.join(current_dir, "report.txt")
# report_old_file = os.path.join(current_dir, "report_old.txt")
# try:
#     shutil.move(report_file, report_old_file)
#     print("Файл переименован")
# except FileNotFoundError:
#     print("Файл report.txt не найден")

# 5
# current_dir = os.path.dirname(os.path.abspath(__file__))
# logs_dir = os.path.join(current_dir, "logs")
# archive_dir = os.path.join(logs_dir, "archive")
# if not os.path.exists(archive_dir):
#     os.makedirs(archive_dir)
#     print("Папка archive создана")

# for item in os.listdir(logs_dir):
#     item_path = os.path.join(logs_dir, item)

#     if os.path.isfile(item_path):
#         shutil.move(item_path, archive_dir)
#         print("Файл перемещен в архив")


# 6
# def clean_build():
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     build_dir = os.path.join(current_dir, "build")

#     if os.path.exists(build_dir):
#         shutil.rmtree(build_dir)
#         print("Папка удалена")
#     else:
#         print("Папки не существует")


# clean_build()

# 7
# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_dir = os.path.join(current_dir, "project")
# project_zip = os.path.join(current_dir, "project_backup")
# shutil.make_archive(project_zip, "zip", project_dir)
# print("Архив создан")

# 8
# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_zip = os.path.join(current_dir, "project_backup.zip")
# restrored_project_dir = os.path.join(current_dir, "restored_project")
# if os.path.exists(restrored_project_dir):
#     shutil.rmtree(restrored_project_dir)
#     print("Папка удалена")

# shutil.unpack_archive(project_zip, restrored_project_dir)
# print("Архив распакован")


# 9
# def disk_usage():
#     total, used, free = shutil.disk_usage(".")

#     total_mb = total / (1024 * 1024)
#     used_mb = used / (1024 * 1024)
#     free_mb = free / (1024 * 1024)

#     print(f"Общий объём: {total_mb:.2f} МБ")
#     print(f"Занято: {used_mb:.2f} МБ")
#     print(f"Свободно: {free_mb:.2f} МБ")


# disk_usage()

# 10
# python_found = shutil.which("python")
# if python_found:
#     print(f"Путь к python :{python_found}")
# else:
#     print("Не найдено")
