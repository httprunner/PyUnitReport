import io
import os
import re

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'pyunitreport', '__init__.py')) as f:
    version = re.compile(r"__version__\s+=\s+'(.*)'", re.I).match(f.read()).group(1)

requirements = [
    # Package requirements here
    "jinja2"
]

test_requirements = [
    # Package test requirements here
]

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyUnitReport',
    version=version,
    description="A unit test runner for Python, and generate HTML reports.",
    long_description=long_description,
    author="Ordanis Sanchez Suero, Leo Lee",
    author_email='mail@debugtalk.com',
    url='https://github.com/debugtalk/PyUnitReport',
    packages=find_packages(exclude=['tests']),
    package_data={
        'pyunitreport': ['template/*'],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='HtmlTestRunner TestRunner Html Reports',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
