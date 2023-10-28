from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.4',
    author='Artem l'
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greeting=hello_world_vvm.main:greeting']}
)