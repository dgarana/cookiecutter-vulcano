# -*- coding: utf-8 -*-
import setuptools


setuptools.setup(
    name='{{cookiecutter.project_name}}',
    description='{{cookiecutter.project_description}}',
    version=':versiontools:{{cookiecutter.project_slug}}:',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['vulcano'],
    setup_requires=('versiontools'),
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_mail}}',
    entry_points = {
        'console_scripts': ['{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.app:main'],
    },
    url='{{cookiecutter.project_url}}',
)
