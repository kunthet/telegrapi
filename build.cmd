rmdir dist /s /q
python -m build
twine upload dist/*