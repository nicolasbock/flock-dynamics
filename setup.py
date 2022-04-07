from setuptools import setup

setup(
    name='flock_dyanmics',
    version='0.0.1',
    packages=['flock_dynamics'],
    install_requires=[
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'flock-dynamics=main:main',
        ],
    },
)
