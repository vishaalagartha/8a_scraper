import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="8a_scraper",
    version="0.0.3",
    author="Vishaal Agartha",
    author_email="vishaalagartha@gmail.com",
    license="MIT",
    description="A Python client for scraping data from 8a.nu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishaalagartha/8a_scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'beautifulsoup4==4.9.1',
        'bs4==0.0.1',
        'certifi==2020.6.20',
        'chardet==3.0.4',
        'idna==2.10',
        'python-slugify==4.0.1'
        'requests==2.24.0',
        'selenium==3.141.0',
        'soupsieve==2.0.1',
        'urllib3==1.25.9',
        'webdriver-manager==3.2.2'
    ],
    extras_require={
        'test': ['unittest'],
    },
    keywords=[
        "climbing",
        "rockclimbing",
        "bouldering",
        "sportclimbing",
        "8a",
        "8a.nu",
        "data mining",
        ]
)
