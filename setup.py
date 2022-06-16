from setuptools import setup, find_packages

setup(
    name="testapp",
    version="0.0.1",
    url="https://github.com/kdowolski-reef/test_repo",
    packages=find_packages(),
    python_requires=">=3.6",
    package_data={"": ["somfile", "templates/*.html"]},
    include_package_data=True,
)
