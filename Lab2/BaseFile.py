import os
from datetime import datetime


class BaseFile:
    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(path)
        self.extension = os.path.splitext(self.filename)[1]
        stat_info = os.stat(path)
        self.created_time = stat_info.st_ctime
        self.updated_time = stat_info.st_mtime


    def info(self):
        return {
            'file_name': self.filename,
            'extension': self.extension,
            'created_time': datetime.fromtimestamp(self.created_time).strftime("%Y-%m-%d %H:%M:%S"),
            'updated_time': datetime.fromtimestamp(self.updated_time).strftime("%Y-%m-%d %H:%M:%S")
        }
