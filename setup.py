from setuptools import setup

setup_kwargs = dict(
    name='tombstones',
    version='0.1',
    license='BSD',
    packages=['tombstones'],
    package_dir={'tombstones': 'tombstones'},
    entry_points={
        'console_scripts': ['tombstones=tombstones.__main__:main'],
    },
    install_requires=['wrapt>=1.10.5'],
    include_package_data=True,
)

setup(**setup_kwargs)
