from setuptools import setup, find_packages

setup(name="mess_server_proj",
      version="0.0.1",
      description="mess_server_proj",
      author="StanleyIG",
      author_email="oootehts@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
