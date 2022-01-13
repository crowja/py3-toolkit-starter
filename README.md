# py3-toolkit-starter 0.0.1-dev0.

A simple template for creating a toolkit in Python, a program with subcommands,
for example `mytoolkit XXX --in=infile.txt`.

## Getting started

Grab the repo:

```sh
$ wget https://github.com/crowja/py3-toolkit-starter/archive/refs/heads/main.zip

# ... which creates py3-toolkit-starter-main.zip

$ unzip py3-toolkit-starter-main.zip $ mv py3-toolkit-starter-main
my-new-toolkit-name
```

The toolkit's primary command is `src/mytoolkit` and the associated subcommands
are handled by modules, e.g., `mytoolkit/XXX.py`, which perform the bulk of the
command line handling.

A few things:

*   `./bin/mytoolkit` is the main program that calls the tools. The tools
    themselves are Python modules in the folder `./mytoolkit`. See
    `./mytoolkit/XXX.pm` for an example. You'll want to modify these names and
    the references inside.
*   The variable `VERSION` is set to `0.0.1-dev0` in `./bin/mytoolkit`.
