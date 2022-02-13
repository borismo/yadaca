from setuptools import setup, find_packages
from pathlib import Path

GITHUB_REPO = 'https://github.com/borismo/yadaca/'

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='yadaca',
    author='Boris Morel',
    description='A package that generates a data catalog as a static website',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=GITHUB_REPO,
    project_urls={
        'Source': GITHUB_REPO,
        'Bug Tracker': GITHUB_REPO + 'issues',
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3',
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
    ),
    install_requires=[
        'click>=8',
        'SQLAlchemy>=1.4',
    ],
    entry_points={
        'console_scripts': [
            'yadaca = yadaca.main:cli',
        ],
    },
)
