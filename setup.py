from setuptools import setup, find_packages

setup(
    name='PBSKidsPlayer',
    version='0.1.0',
    description='A package to fetch and play PBS Kids content',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)
