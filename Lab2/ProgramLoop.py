from DirectoryMonitor import DirectoryMonitor


class ProgramLoop:
    def __init__(self):
        self.directory = 'D:\#Year2\OOP\OOP_Labs\Lab2\Lab2_test_folder'
        self.monitor = DirectoryMonitor(self.directory)


    def run(self):
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