# coding: utf-8

from setuptools import setup, find_packages

setup(
    name="pymake",
    packages=find_packages(),
    python_requires=">=3.7",
    extras_require={"test": ["pytest >= 3.10.1", "pytest-xdist"]},
    include_package_data=False,
    zip_safe=False,
    py_modules=["make", "mkformat", "mkparse"],
    entry_points={
        "console_scripts": [
            "pymake=make:main",
            "mkformat=mkformat:main",
            "mkparse=mkparse:main",
        ]
    },
)
