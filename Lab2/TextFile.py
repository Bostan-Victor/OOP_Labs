from BaseFile import BaseFile


class TextFile(BaseFile):
    def info(self):
        base_info = super().info()
        with open(self.path, 'r') as f:
            content = f.read()
            lines = content.split('\n')
            words = content.split()
            base_info.update({
                'line_count': len(lines),
                'word_count': len(words),
                'character_count': len(content)
            })
        return base_info