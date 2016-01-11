from __future__ import absolute_import
from setuptools import setup, find_packages

install_requires = [
    'lemur',
]

setup(
    name='lemur_digicert',
    version='0.1',
    author='keval',
    author_email='emailid',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'lemur.plugins': [
            'digicert_issuer = lemur_digicert.plugin:DigicertIssuerPlugin'
        ]
    }
)
