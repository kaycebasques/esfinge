source venv/bin/activate
python3 -m pip install -r requirements.txt --upgrade
python3 -m build
python3 -m twine upload dist/*
deactivate
