
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()