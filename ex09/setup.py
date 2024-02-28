from setuptools import setup, find_packages
setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    url='https://github.com/Lucstone/piscine-python-42/tree/main/ex09/ft_package',
    author='lnaidu',
    author_email='lnaidu@student.42nice.com',
    license='MIT',
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    packages=find_packages(),
)