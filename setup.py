from setuptools import setup

setup(
    name="ChangeDetection",
    install_requires=[
        "click~=7.0",
        "colorama"
    ],
    extras_require={
        'test': "pytest~=6.2.3",
    },
)