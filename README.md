# py3-toolkit-starter 0.0.1-dev0.

A simple template for creating a toolkit in Python, a program with subcommands,
for example `mytoolkit XXX --in=infile.txt`.

## Getting started

Grab the repo:

```sh
$ wget https://github.com/crowja/py3-toolkit-starter/archive/refs/heads/main.zip
```

which creates py3-toolkit-starter-main.zip

```
$ unzip py3-toolkit-starter-main.zip
$ mv py3-toolkit-starter-main my-new-toolkit-name
```

A few things:

*   `./bin/mytoolkit` is the main program that calls the tools. The tools
    themselves are Python modules in the folder `./mytoolkit`. See
    `./mytoolkit/XXX.pm` for an example. You'll want to modify these names and
    the references inside.
*   If you're going to do versioning with `bump2version`, move
    `dot-bumpversion.cfg` to `.bumpversion.cfg` and edit it. `VERSION` appears
    in `README.md`, `setup.py`, and `bin/mytoolkit`.
*   Replace this `README.md` file with something appropriate.
