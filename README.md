boiler
======

CLI for creating boilerplate files, directories, and structures


Install
=======

```
pip install -U git+https://github.com/nagasuga/boiler.git
```


Usage
=====

```
boiler [-h] [-v] {pull,ls,rm,create} ...

CLI for creating boilerplate files, directories, and structures

positional arguments:
    pull               Download boilerplate
    ls                 List all saved boilerplates
    rm                 Remove boilerplates
    create             Create boilerplate
```


TODO
====

* Use hard link instead of copying files if platform has it available
* take variables as option to replace templated files
