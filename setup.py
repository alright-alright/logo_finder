from setuptools import setup, find_packages

setup(
    name='logo_toolkit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'Pillow',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'logo-toolkit=logo_toolkit.cli:main'
        ]
    }
)

