#! /usr/bin/env python3
"""Installation script."""

from setuptools import setup

setup(
    name="b64lzma",
    use_scm_version={"local_scheme": "node-and-timestamp"},
    setup_requires=["setuptools_scm"],
    author="HOMEINFO - Digitale Informationssysteme GmbH",
    author_email="<info at homeinfo dot de>",
    maintainer="Richard Neumann",
    maintainer_email="<r dot neumann at homeinfo priod de>",
    py_modules=["b64lzma"],
    license="GPLv3",
    description="Represent bytes as LZMA-compressed, base64-encoded strings.",
)
