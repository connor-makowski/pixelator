from distutils.core import setup
setup(
  name = 'pixelator',
  packages = ['pixelator'],
  version = '0.1',
  license='MIT',
  description = 'Pixelate images to a specified size and color palette for AI/ML and various other purposes',
  author = 'Connor Makowski',
  author_email = 'connor.m.makowski@gmail.com',
  url = 'https://github.com/connor-makowski/pixelator',
  download_url = 'https://github.com/connor-makowski/pixelator/archive/v_01.tar.gz',
  keywords = ['pixelate', 'picture', 'pixel', 'pixels', 'ai', 'ml'],
  install_requires=[
          'Pillow',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
  ],
)
