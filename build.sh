python setup.py sdist bdist_wheel
python -m twine upload dist/*

rm -rf tracardi_lang_detection.egg-info
