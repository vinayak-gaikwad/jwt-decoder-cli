from setuptools import setup, find_packages

setup(
    name="jwt-decoder-cli",
    version="0.1.0",
    author="vinayakg",
    description="A simple JWT decoder CLI tool",
    url="https://github.com/vinayak-gaikwad/jwt-decoder-cli",
    install_requires=[
        "PyJWT",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "jwt-decoder=jwt_decoder.cli:main",
        ],
    },
    python_requires=">=3.6",
)
