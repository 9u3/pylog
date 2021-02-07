from distutils.core import setup
setup(
  name = 'PYLog',
  packages = ['PYLog'],
  version = '1.1',
  license='MIT',
  description = 'Simple yet effective logging solution',
  author = 'Nox Protogen',
  author_email = 'cfym.gamer@gmail.com',
  url = 'https://github.com/9u3/pylog',
  download_url = 'https://github.com/9u3/pylog/tree/master/pylog',
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
