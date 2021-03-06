import os
from zipfile import ZipFile

def create_assets_archive(directory):
    assets_name=directory.replace("assets-", "").split(".")[-1]
    print(f"Creating Assets.{assets_name}.zip for folder {directory}")
    with ZipFile(f'Assets.{assets_name}.zip', 'w') as myzip:
        dir_leaf = ""
        for root, _, files in os.walk(directory, topdown=False):
            for fi in files:
                print(f"Adding bin {fi} to Assets.{assets_name}.zip")
                myzip.write(os.path.join(root, fi), arcname=f"assets/{fi}")
                dir_leaf = os.path.join(root, fi)
        asset_path = directory.replace("assets-", "").replace(".", "/")
        for root, _, files in os.walk(os.path.join("Assets", asset_path, "fonts"), topdown=False):
            for fi in files:
                print(f"Adding mks_font/{fi} to Assets.{assets_name}.zip")
                myzip.write(os.path.join(root, fi), arcname=f"assets/{fi}")

def create_firmware_archive(directory):
    firmware_name = directory.replace("firmware-", "")
    print(f"Creating {firmware_name}.zip for folder {directory}")
    with ZipFile(f'{firmware_name}.zip', 'w') as myzip:
        myzip.write(f"{directory}/Robin_nano35.bin", arcname="Robin_nano35.bin")

for directory in os.listdir("."):
    if directory.startswith("assets-"):
        create_assets_archive(directory)
    elif directory.startswith("firmware-"):
        create_firmware_archive(directory)
