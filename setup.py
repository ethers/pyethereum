
from setuptools import setup, find_packages

console_scripts = [ 'pyeth=pyethereum.eth:main',
                    'pyethclient=pyethereum.ethclient:main']

setup(name="pyethereum",
      version='0.2.5',
      packages=find_packages("."),
      install_requires=[
          'six', 'leveldb', 'bitcoin', 'pysha3',
          'miniupnpc','ethereum-serpent', 'pytest',
          'bottle', 'waitress', 'docopt'],
      entry_points=dict(console_scripts=console_scripts))
