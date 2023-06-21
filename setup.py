#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-bqcost"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "1.3.0"
description = """The dbt_bqcost adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="qrtt1",
    author_email="qrtt1@infuseai.io",
    url="https://github.com/qrtt1/dbt-bqcost-adapter",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core~=1.3.0.",
    ],
)
