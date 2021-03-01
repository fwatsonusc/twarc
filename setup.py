import sys
import twarc
import setuptools

version = twarc.__version__

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    dependencies = f.read().split()

if __name__ == "__main__":
    setuptools.setup(
        name='twarc',
        version=version,
        url='https://github.com/docnow/twarc',
        author='Ed Summers',
        author_email='ehs@pobox.com',
        packages=['twarc', ],
        description='Archive tweets from the command line',
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires='>=3.3',
        install_requires=dependencies,
        setup_requires=['pytest-runner'],
        tests_require=['pytest', 'python-dotenv'],
        entry_points={'console_scripts': ['twarc = twarc.command:cli']}
    )
