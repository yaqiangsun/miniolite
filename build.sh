python setup.py bdist_wheel
# python setup.py bdist_wheel --plat-name=manylinux1_x86_64 --python-tag=cp310
# python setup.py bdist_wheel --plat-name=win_amd64 --python-tag=cp310

# upload to pypi
# twine upload dist/*