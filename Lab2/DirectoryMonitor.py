import os
import time
from datetime import datetime
from BaseFile import BaseFile
from TextFile import TextFile
from ImageFile import ImageFile
from ProgramFile import ProgramFile


class DirectoryMonitor:
    def __init__(self, directory):
        self.directory = directory
        self.snapshot_time = time.time()
        self.files_stats = self.get_files_stats()


    def get_files_stats(self):
        files_stats = {}
        for filename in os.listdir(self.directory):
            path = os.path.join(self.directory, filename)
            if os.path.isfile(path):
                stat_info = os.stat(path)
                files_stats[filename] = {
                    'mtime': stat_info.st_mtime, 
                    'ctime': stat_info.st_ctime,
                    'path': path
                }
        return files_stats


    def commit(self):
        current_files_stats = self.get_files_stats()
        
        file_changes = {}

        # Check for new files or file modifications
        for filename, data in current_files_stats.items():
            if filename not in self.files_stats:
                file_changes[filename] = 'Created'
            elif data['mtime'] != self.files_stats[filename]['mtime']:
                file_changes[filename] = 'Changed'
            else:
                file_changes[filename] = 'No Change'

        # Check for file deletions
        for filename in self.files_stats.keys():
            if filename not in current_files_stats:
                file_changes[filename] = 'Deleted'

        changes_detected = any(value != 'No Change' for value in file_changes.values())
        
        if changes_detected:
            self.snapshot_time = time.time()
            self.files_stats = current_files_stats
            print(f'\nNew snapshot created at: {datetime.fromtimestamp(self.snapshot_time).strftime("%Y-%m-%d %H:%M:%S")}')
            for filename, change in file_changes.items():
                print(f'{filename} - {change}')
            print()
        else:
            print('\nNo changes detected!\n')


    def get_file_instance(self, filename):
        ext = filename.split('.')[-1].lower()
        if ext == 'txt':
            return TextFile(os.path.join(self.directory, filename))
        elif ext in ['png', 'jpg']:
            return ImageFile(os.path.join(self.directory, filename))
        elif ext in ['py', 'java']:
            return ProgramFile(os.path.join(self.directory, filename))
        else:
            return BaseFile(os.path.join(self.directory, filename))


    def get_file_info(self, filename):
        file_instance = self.get_file_instance(filename)
        info = file_instance.info()
        print()
        for key, value in info.items():
            print(f'{key}: {value}')
        print()
