from distutils.core import setup
setup(
  name = 'PYLog',
  packages = ['PYLog'],
  version = '2.0',
  license='MIT',
  description = 'Simple yet effective logging solution V2',
  author = 'Nox Protogen',
  author_email = 'cfym.gamer@gmail.com',
  url = 'https://github.com/9u3/pylog',
  download_url = 'https://github.com/9u3/pylog/tree/master/pylog/PYLog2',
  keywords = ['wrapper', 'api', 'logging'],
  install_requires=['aiohttp', 'colorama'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
