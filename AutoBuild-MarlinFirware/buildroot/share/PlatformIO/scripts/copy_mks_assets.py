Import("env")
import shutil
from pathlib import Path

source_assets_path = Path(env.Dictionary("PROJECT_DIR"), "..", "MKS_Assets")
assets_path = Path(env.Dictionary("PROJECT_BUILD_DIR"), env.Dictionary("PIOENV"), "out")

assets_path.mkdir(parents=True, exist_ok=True)
shutil.copytree(source_assets_path, assets_path, dirs_exist_ok=True)