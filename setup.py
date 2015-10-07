from setuptools import setup

setup_kwargs = dict(
    name='tombstones',
    version='0.1',
    description='Python package to mark dead code.',
    license='BSD',
    author='Per Classon',
    author_email='perwclasson@gmail.com',
    url='https://github.com/perclasson/python-tombstones',
    download_url='https://github.com/perclasson/python-tombstones/tarball/0.1',
    packages=['tombstones'],
    package_dir={'tombstones': 'tombstones'},
    entry_points={
        'console_scripts': ['tombstones=tombstones.__main__:main'],
    },
    install_requires=['wrapt>=1.10.5'],
    include_package_data=True,
    keywords=['dead code', 'unreachable code'],
    classifiers=[],
)

setup(**setup_kwargs)
