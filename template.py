import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    file=Path(filepath)
    file_dir,filename=os.path.split(file)

    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating directory {file_dir} for file {filename}")
    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,'w') as f:
            pass
            logging.info(f"creating empty file {filename}")
    else:
        logging.info(f"{filename} is already exists")