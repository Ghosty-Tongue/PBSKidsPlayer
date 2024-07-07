from setuptools import setup, find_packages

setup(
    name='pbskidsplayer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'pbskidsplayer = pbskidsplayer.main:main',
        ],
    },
    author='Ghosty-Tongue',
    author_email='your.email@example.com',
    description='Python Package to fetch PBS Kids Content.',
    url='https://github.com/Ghosty-Tongue/pbskidsplayer',
)
