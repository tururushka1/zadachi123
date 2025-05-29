from utils.path_utils import safe_join

class Navigation:
    def __init__(self, root):
        self.root = root

    def list_dir(self, current):
        for entry in sorted(current.iterdir()):
            print("[D]" if entry.is_dir() else "[F]", entry.name)

    def change_dir(self, current, target):
        new_path = safe_join(self.root, current, target)
        if new_path.is_dir():
            return new_path
        print("Не удалось перейти: не директория")
        return current