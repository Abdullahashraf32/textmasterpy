from setuptools import setup, find_packages
import os
readme_path = "README.md"
if os.path.exists(readme_path):
    with open("README.md", "r", encoding="utf-8") as file:
        long_description = file.read()
else:
    long_description = "A Python library for text analysis and processing in English and Arabic."
setup(
    name="textmasterpy",
    version="1.0.1",
    description="A Python library for text analysis and processing in English and Arabic.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Abdullah Ashraf",
    author_email="abdullahashraf4846@gmail.com",
    url="https://github.com/Abdullahashraf32/textmasterpy.git",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.6",
    install_requires=[],
    license="MIT",
    zip_safe=False,
)
