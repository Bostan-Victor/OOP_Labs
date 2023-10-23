from DirectoryMonitor import DirectoryMonitor

class Main:
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
                pass
            elif inp == 'status':
                pass


if __name__ == '__main__':
    main = Main()
    main.run()
