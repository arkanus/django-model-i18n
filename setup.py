#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
import os

setup(
    name = "django-pluggable-model-i18n",
    version = "0.1",
    url = 'http://code.google.com/p/django-pluggable-model-i18n/',
    download_url = 'http://code.google.com/p/django-pluggable-model-i18n/source/checkout',
    description = """a django application which enables you to store and work with content 
    translations for developing multilingual sites.""",
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
    ]
)
