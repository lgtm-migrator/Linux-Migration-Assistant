from setuptools import setup, find_packages
setup(
    name="Linux Migration Assistant",
    version="0.0.1",
    license="GPL-3.0",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=['*contrib*', '*docs*', '*tests*']),
    python_requires='>=3',
)
