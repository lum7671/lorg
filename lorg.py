import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLI_PATH = ROOT / "src" / "lorg" / "cli.py"

spec = importlib.util.spec_from_file_location("lorg_cli", CLI_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot load CLI module from {CLI_PATH}")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


if __name__ == "__main__":
    module.main()
