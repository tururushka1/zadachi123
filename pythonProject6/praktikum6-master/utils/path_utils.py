from pathlib import Path

def safe_join(root, current, *paths):
    result = (current / Path(*paths)).resolve()
    if not str(result).startswith(str(root)):
        raise ValueError("Попытка выхода за пределы рабочей директории")
    return result