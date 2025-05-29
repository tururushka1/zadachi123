from utils.path_utils import safe_join
import shutil

class FileOperations:
    def __init__(self, root):
        self.root = root

    def create_file(self, current, filename):
        path = safe_join(self.root, current, filename)
        path.touch(exist_ok=True)
        print("Файл создан")

    def read_file(self, current, filename):
        path = safe_join(self.root, current, filename)
        if path.exists():
            print(path.read_text(encoding='utf-8'))
        else:
            print("Файл не найден")

    def write_file(self, current, filename, append=False):
        path = safe_join(self.root, current, filename)
        mode = 'a' if append else 'w'
        content = input("Введите содержимое: ")
        with path.open(mode, encoding='utf-8') as f:
            f.write(content + '\n')
        print("Файл записан")

    def remove_file(self, current, filename):
        path = safe_join(self.root, current, filename)
        if path.is_file():
            path.unlink()
            print("Файл удалён")
        else:
            print("Файл не найден")

    def move_or_rename(self, current, src, dst):
        src_path = safe_join(self.root, current, src)
        dst_path = safe_join(self.root, current, dst)
        shutil.move(src_path, dst_path)
        print("Готово")

    def copy(self, current, src, dst):
        src_path = safe_join(self.root, current, src)
        dst_path = safe_join(self.root, current, dst)
        if src_path.is_file():
            shutil.copy2(src_path, dst_path)
        elif src_path.is_dir():
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        print("Скопировано")