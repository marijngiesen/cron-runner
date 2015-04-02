import glob
from setuptools import setup

setup(
    name='cron-runner',
    version='0.0.2',
    packages=['cronrunner'],
    url='https://github.com/marijngiesen/cron-runner',
    license='Apache 2.0',
    author='Marijn Giesen',
    author_email='marijn@studio-donder.nl',
    description='Runner of cron jobs with logging and duration timing',
    entry_points={
        'console_scripts': [
            'cron-runner = cronrunner.main:main',
        ]
    },
    install_requires=['requests', 'peewee', 'pyyaml', 'commandr', 'MySQL-python'],
    data_files=[
        ('/etc', glob.glob('config/*')),
    ]
)
