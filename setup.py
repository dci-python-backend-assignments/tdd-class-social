from setuptools import setup, find_packages

setup(
    version="0.1",
    name="class_social",
    author="DCI Python Backend 2022 Class",
    author_email="mathias.brito@digitalcareerinstitute.org",
    description="Class Social, a social network for students!",
    url="https://github.com/dci-python-backend-assignments/tdd-class-social",
    license="MIT",
    keywords=['social networks', 'education'],
    requires=[
        'fastapi',
        'requests',
        'uvicorn'
    ],
    test_suite='pytest',
    packages=find_packages(),
    entry_points={
        "console_scripts": ['blog=blog.main:main']
    }
)
