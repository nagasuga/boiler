from distutils.core import setup

setup(
    name='boiler',
    version='0.1.0',
    #packages=['boiler'],
    install_requires=[],
    dependency_links=[],
    description='CLI for creating boilerplate files, directories, and structures',
    author='Jeff Nagasuga',
    author_email='jeffrey.nagasuga@disney.com',
    url='http://github.com/nagasuga/boiler',
    keywords=[],
    classifiers=[],
    scripts=['bin/boiler', 'bin/boiler-config'],
)
