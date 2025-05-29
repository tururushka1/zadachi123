from utils.path_utils import safe_join
import shutil

class DirectoryOperations:
    def __init__(self, root):
        self.root = root

    def make_dir(self, current, dirname):
        path = safe_join(self.root, current, dirname)
        path.mkdir(parents=True, exist_ok=True)
        print("Директория создана")

    def remove_dir(self, current, dirname):
        path = safe_join(self.root, current, dirname)
        if path.is_dir():
            shutil.rmtree(path)
            print("Директория удалена")
        else:
            print("Директория не найдена")