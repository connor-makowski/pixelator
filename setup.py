from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'pixelator',
  packages = ['pixelator'],
  version = '1.0.0',
  license='MIT',
  description = 'Pixelate images to a specified size and color palette for AI/ML and various other purposes',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Connor Makowski',
  author_email = 'connor.m.makowski@gmail.com',
  url = 'https://github.com/connor-makowski/pixelator',
  download_url = 'https://github.com/connor-makowski/pixelator/dist/pixelator-1.0.0.tar.gz',
  keywords = ['pixelate', 'picture', 'pixel', 'pixels', 'ai', 'ml'],
  install_requires=[
          'opencv-python>=4.6.0.66',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
  ],
  python_requires=">=3.6, <4",
)
