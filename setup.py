from setuptools import setup, find_packages

__author__ = "Luis Santos"
__copyright__ = "Copyright 2020, Architecture and Building Systems - ETH Zurich"
__credits__ = ["Luis Santos, Jimeno Fonseca"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Luis Santos"
__email__ = "cea@arch.ethz.ch"
__status__ = "Production"

setup(name='scenario_generator',
      version=__version__,
      description="A plugin for the City Energy Analyst, used to automates a number of parallelized simulations based on variable distributions",
      license='MIT',
      author='Architecture and Building Systems',
      author_email='cea@arch.ethz.ch',
      url='https://github.com/architecture-building-systems/cea-plugin-template',
      long_description="This City Energy Analyst plugin is used to automate a number of parallelized simulations of the same scenario *for a single building*, based on variable input stochastic distributions. An output file is produced, which saves main inputs and outputs from each iteration.",
      py_modules=[''],
      packages=find_packages(),
      package_data={},
      install_requires=[],
      include_package_data=True)
