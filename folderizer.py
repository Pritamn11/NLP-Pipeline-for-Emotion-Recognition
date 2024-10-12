import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

project_name = 'EmotionRecognition'

list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transforamation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]

for file_path_str in list_of_files:
    file_path = Path(file_path_str)

    # Creating the directory
    os.makedirs(file_path.parent, exist_ok=True)
    logging.info(f"{file_path.parent} directory created")

    # Creating an empty file if its not a directory
    if not file_path.is_dir():
        file_path.touch()
        logging.info(f"{file_path} file created")
    

# # Verifying the directory structure and files using os.walk
# for root, dirs, files in os.walk('.'):
#     logging.info(f"Current directory: {root}")
#     logging.info(f"Subdirectories: {dirs}")
#     logging.info(f"Files: {files}")
#     logging.info("")
