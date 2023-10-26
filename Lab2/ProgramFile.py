from BaseFile import BaseFile


class ProgramFile(BaseFile):
    def info(self):
        base_info = super().info()
        with open(self.path, 'r') as f:
            content = f.read()
            lines = content.split('\n')

            if self.path.endswith('.py'):
                class_count = sum(1 for line in lines if 'class ' in line)
                method_count = sum(1 for line in lines if 'def ' in line)
            elif self.path.endswith('.java'):
                class_count = sum(1 for line in lines if 'class ' in line)
                method_count = sum(1 for line in lines if '(' in line and ')' in line and '{' in line)

            base_info.update({
                'line_count': len(lines),
                'class_count': class_count,
                'method_count': method_count
            })

        return base_info