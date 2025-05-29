from pathlib import Path
from commands.navigation import Navigation
from commands.file_ops import FileOperations
from commands.dir_ops import DirectoryOperations

ROOT_DIR = Path("./workspace").resolve()
ROOT_DIR.mkdir(parents=True, exist_ok=True)

current_path = ROOT_DIR

nav = Navigation(ROOT_DIR)
dir_ops = DirectoryOperations(ROOT_DIR)
file_ops = FileOperations(ROOT_DIR)

print("[Файловый менеджер] — Введите команду. (exit для выхода)")

while True:
    try:
        cmd = input(f"[{str(current_path.relative_to(ROOT_DIR))}] > ").strip().split()
        if not cmd:
            continue

        match cmd[0]:
            case 'exit':
                break
            case 'ls':
                nav.list_dir(current_path)
            case 'cd':
                if len(cmd) > 1:
                    current_path = nav.change_dir(current_path, cmd[1])
            case 'pwd':
                print(current_path)
            case 'mkdir':
                if len(cmd) > 1:
                    dir_ops.make_dir(current_path, cmd[1])
            case 'rmdir':
                if len(cmd) > 1:
                    dir_ops.remove_dir(current_path, cmd[1])
            case 'create':
                if len(cmd) > 1:
                    file_ops.create_file(current_path, cmd[1])
            case 'read':
                if len(cmd) > 1:
                    file_ops.read_file(current_path, cmd[1])
            case 'write':
                if len(cmd) > 1:
                    file_ops.write_file(current_path, cmd[1])
            case 'append':
                if len(cmd) > 1:
                    file_ops.write_file(current_path, cmd[1], append=True)
            case 'rm':
                if len(cmd) > 1:
                    file_ops.remove_file(current_path, cmd[1])
            case 'mv':
                if len(cmd) > 2:
                    file_ops.move_or_rename(current_path, cmd[1], cmd[2])
            case 'cp':
                if len(cmd) > 2:
                    file_ops.copy(current_path, cmd[1], cmd[2])
            case _:
                print("Неизвестная команда")
    except Exception as e:
        print(f"Ошибка: {e}")