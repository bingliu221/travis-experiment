from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/bingliu221/travis-experiment',
      author='Bing Liu',
      author_email='bingliu221@gmail.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)
