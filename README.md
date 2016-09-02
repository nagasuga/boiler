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
boiler [-h] [-v] {list,add,rm,create} ...

CLI for creating boilerplate files, directories, and structures

positional arguments:
  {list,add,rm,create}  Sub-command help
    list                List all saved boilerplates
    add                 Add boilerplate
    get                 Downloads boilerplate from repository and set it up in given destination
    rm                  Remove boilerplates
    create              Create boilerplate

optional arguments:
  -h, --help            show this help message and exit
  -v                    Verbose mode to print more information
```


TODO
====

* Use hard link instead of copying files if platform has it available
* take variables as option to replace templated files
