# DVC_DL_tensorflow

# commands -

## create a new env
py -m venv env
env\Scripts\activate.bat

## init DVC
git init
dvc init

## create empty files -
mkdir -p src/utils config
touch src/__init__.py src/utils/__init__.py param.yaml dvc.yaml config/config.yaml src/stage_01_load_save.py src/utils/all_utils.py setup.py .gitignore

## install src
pip install -e .