import time

class DirectoryMonitor:
    def __init__(self, directory):
        self.directory = directory
        self.snapshot_time = time.time()
        # self.files_stats = self.get_files_stats()


    def commit(self):
        self.snapshot_time = time.time()
        print(f'New snapshot created at: {self.snapshot_time}')
