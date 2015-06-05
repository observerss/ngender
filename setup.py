try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ngender',
    version='0.1.1',
    description='Guess gender for Chinese names',
    url='https://github.com/observerss/ngender',
    author='Jingchao Hu(observerss)',
    author_email='jingchaohu@gmail.com',
    packages=['ngender'],
    package_data={'': ['LICENSE'],
                  'ngender': ['charfreq.csv']},
    license=open('LICENSE').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'ng = ngender.cli:main',
        ],
    }
)
