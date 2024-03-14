import os
import shutil
import time

# Configuration
backup_directory = "/app/backups"
data_directory = "/var/lib/mysql"
code_directory = "/app"

def backup_data():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"data_backup_{timestamp}.tar.gz"
    backup_path = os.path.join(backup_directory, backup_name)
    shutil.make_archive(backup_path, 'gztar', root_dir=data_directory)

def backup_code():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"code_backup_{timestamp}.tar.gz"
    backup_path = os.path.join(backup_directory, backup_name)
    shutil.make_archive(backup_path, 'gztar', root_dir=code_directory)

if __name__ == "__main__":
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    backup_data()
    backup_code()