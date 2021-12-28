# py3-toolkit-starter.

A simple template for creating toolkits in Python, programs with
subcommands, for example `mytoolkit XXX --in=infile.txt`.

## Getting started

Grab the repo:

```sh
$ wget https://github.com/crowja/py3-toolkit-starter/archive/refs/heads/main.zip
# ... creates py3-toolkit-starter-main.zip 

$ unzip py3-toolkit-starter-main.zip
$ mv py3-toolkit-starter-main my-new-toolkit-name
```
The toolkit's primary command is `src/mytoolkit` and the associated subcommands
are handled by modules, e.g., `mytoolkit/XXX.py`, which perform the bulk of the
command line handling.
