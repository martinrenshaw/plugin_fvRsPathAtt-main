import codecs
import os.path

from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='netbox-plugin-fvRsPathAtt',
    version=get_version('plugin_fvRsPathAtt/version.py'),
    description='Bind static paths to EPGs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/martinrenshaw/plugin_fvRsPathAtt',
    author='M.Renshaw',
    author_email='martin@martinrenshaw.com',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ]
)
