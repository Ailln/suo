from setuptools import setup
from setuptools import find_packages

NAME = "suo"
AUTHOR = "Ailln"
EMAIL = "kinggreenhall@gmail.com"
URL = "https://github.com/Ailln/suo"
LICENSE = "MIT License"
DESCRIPTION = "中英文缩写转化"
VERSION = "0.0.5"

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=open("./requirements.txt", "r").read().splitlines(),
        long_description=open("./README.md", "r").read(),
        long_description_content_type="text/markdown",
        entry_points={
            "console_scripts": [
                "suo=suo.shell:run"
            ]
        },
        package_data={
            "suo": ["src/*.yaml"]
        },
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            f"License :: OSI Approved :: {LICENSE}",
            "Operating System :: OS Independent"
        ],
        python_requires=">=3.6"
    )
