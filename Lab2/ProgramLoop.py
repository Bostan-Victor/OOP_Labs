from DirectoryMonitor import DirectoryMonitor
import threading
import time
from datetime import datetime


class ProgramLoop:
    def __init__(self):
        self.directory = 'D:\#Year2\OOP\OOP_Labs\Lab2\Lab2_test_folder'
        self.monitor = DirectoryMonitor(self.directory, self)
        self.stop_monitoring = False
        self.notified_files = set()


    def monitor_directory(self):
        while not self.stop_monitoring:
            file_changes, _ = self.monitor.detect_changes()
            
            for filename, change in file_changes.items():
                if change != 'No Change' and filename not in self.notified_files:
                    print(f'\nNew changes detected at: {datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")}')
                    print(f'{filename} - {change}')
                    self.notified_files.add(filename)
            
            time.sleep(5)  


    def run(self):
        monitor_thread = threading.Thread(target=self.monitor_directory)
        monitor_thread.start()
        inp = ''
        while inp != 'exit':
            inp = input('Choose an option(commit, info <filename>, status, exit): ').strip().lower()
            if inp == 'commit':
                self.monitor.commit()
            elif inp.startswith('info '):
                filename = inp.split(' ')[1]
                self.monitor.get_file_info(filename)
            elif inp == 'status':
                self.monitor.status()
        self.stop_monitoring = True  # Tell the monitoring thread to stop
        monitor_thread.join()
            