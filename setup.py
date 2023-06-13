from setuptools import setup

requires = [
    'requests'
]


def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='centapp',
    version='1.0.0',
    author='hteppl',
    author_email='hteppl.dev@gmail.com',
    description='Python client library for interacting with CentApp API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/hteppl/centapp-sdk-python',
    packages=['centapp'],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords=['python', 'api', 'sdk', 'payments', 'centapp'],
    python_requires='>=3.7'
)
