import os
from setuptools import setup,find_packages



from setuptools import Extension
from setuptools.command.build_ext import build_ext
class DummyExtension(Extension):
    def __init__(self):
        super().__init__("dummy.extension", sources=[])
class DummyExtensionBuild(build_ext):
    def run(self) -> None:
        return
cmdclass = {
    "build_ext": DummyExtensionBuild,
}
# 定义扩展模块
ext_modules = [DummyExtension()]



classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3 :: Only
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: Microsoft :: Windows
Operating System :: Unix
Operating System :: MacOS :: MacOS X
"""

curr_path = os.path.abspath(os.path.dirname(__file__))
setup(
    name='miniolite',
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    version='0.0.0.3',
    # packages=['miniolite'],
    packages=find_packages(),
    package_data={'miniolite': ['py.typed']},
    python_requires='>=3.8',
    install_requires=['sqlalchemy >= 2.0.30'],
    classifiers=filter(None, classifiers.split('\n')),
    zip_safe=True,
    author='Yaqiang Sun',
    # long_description=open(os.path.join(curr_path, 'README.rst'), 'r').read(),
    long_description_content_type='text/x-rst',
    description='Object Storage based on db',
    license='GPL v3',
    keywords='lite file system database',
    url='https://github.com/yaqiangsun/miniolite',
    include_package_data=True,
)