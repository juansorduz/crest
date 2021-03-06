# @file setup_homestead_prov.py
#
# Copyright (C) Metaswitch Networks 2016
# If license terms are provided to you in a COPYING file in the root directory
# of the source code repository by which you are accessing this code, then
# the license outlined in that COPYING file applies to your use.
# Otherwise no rights are granted except for those provided to you by
# Metaswitch Networks in a separate written agreement.

import logging
import sys
# Workaround bug in multiprocessing - http://bugs.python.org/issue15881
# Without this, running tests involving twisted throws an error on completion
try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages
from logging import StreamHandler

_log = logging.getLogger("homestead_prov")
_log.setLevel(logging.DEBUG)
_handler = StreamHandler(sys.stderr)
_handler.setLevel(logging.DEBUG)
_log.addHandler(_handler)

setup(
    name='homestead_prov',
    version='0.1',
    namespace_packages = ['metaswitch'],
    packages=find_packages('src', include=['metaswitch', 'metaswitch.homestead_prov', 'metaswitch.homestead_prov.*']),
    package_dir={'':'src'},
    package_data={'': ['*.xsd', '*.xml']},
    test_suite='metaswitch.homestead_prov.test',
    install_requires=["crest"],
    tests_require=[
        "funcsigs",
        "Mock",
        "pbr",
        "phonenumbers",
        "six"],
    options={"build": {"build_base": "build-homestead_prov"}},
    )
