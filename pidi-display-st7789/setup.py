import setuptools

VERSION = '1.0.0'

setuptools.setup(
    name="OrangePi.Pidi.st7789",
    version=VERSION,
    author='Andriy Malyshenko',
    author_email='andriy@sonocotta.com',
    description="pidi plugin for display output using an ST7789 SPI LCD on the OrangePi.",
    long_description=open("README.md").read() + "\n" + open("CHANGELOG.txt").read(),
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/sonocotta/pidi-plugins-python",
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["pidi_display_st7789"],
    install_requires=[
        "pidi-display-pil>=0.1.0",
        "OrangePi.ST7789",
        "Pillow",
    ],
    entry_points={
        'pidi.plugin.display': [
            'DisplayST7789 = pidi_display_st7789:DisplayST7789'
        ]
    },
    python_requires=">=2.7",
    test_suite="tests",
    include_package_data=True
)
