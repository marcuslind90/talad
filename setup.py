from setuptools import find_packages, setup
import talad

def read(filename):
    with open(filename) as f:
        return f.read()

setup(
    name="talad",
    version=talad.__version__, 
    packages=find_packages(),
    author="Marcus Lind",
    author_email="marcuslind90@gmail.com",
    license="MIT",
    description="Ecommerce module for Django.", 
    long_description=read('README.rst'), 
    url="http://github.com/marcuslind90/{{ app_name }}/",
    test_suite="tests",
    install_requires=[
        "Django>=1.11"
    ],
    tests_require=[],
    extras_require={},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
