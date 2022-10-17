# Mantid Project Landing Page

This repository holds the source for the www subdomain for the mantidproject.
For other sites see the corresponding GitHub repository - each is named after
the subdomain.

Contents:

- [Build Instructions](#build-instructions)
- [Updating the latest release links](#updating-the-latest-release-links)
- [Adding a news item](#adding-a-news-item)

## Build Instructions

### Set up Python

It is recommended that the site be built inside either a virtual environment or
a conda environment.

#### Virtualenv

If you already have Python installed create and activate a new virtual environment:

```sh
python -m venv ./virtualenv
. ./virtualenv/bin/activate.sh
```

#### Conda/Mamba

If you have Conda or Mamba installed but you do not have Python installed
create and activate a new environment:

```sh
mamba create -p ./condaenv
mamba activate $PWD/condaenv
```

### Build

In the root directory of the project install the dependencies:

```sh
pip install -r requirements.txt
```

Build the site with `make`:

```sh
make html
```

The site will be built in a `_build` directory.

### View

To view the site it is recommended to run a webserver rather than accessing
the files directly in the browser as some restrictions can apply when
accessing various assets directly via the file system.
Python has a `http.server` that is useful for this:

```sh
python -m http.server --directory=_build/html
```

Vist the url given by the server when it starts.

## Updating the latest release links

The links on the installation page must be updated whenever a new
release of mantid is published. The update is best done using the
`generate_release_html.py` script that will fetch the latest
verion number from the [mantid releases list]() automatically.
The update can be done by hand if necessary by editing the
`source/_templates/installation-latest.html` template.

To use the script, follow the instructions above to create an environment
that is able to build the pages. Once the site is built run

```sh
python generate_release_html.py
```

then build the pages and view the updates.
Commit the result and push the updated versions to republish the updated
pages.


## Adding a news item

The new sidebar is defined in `source/_templates/sidebar-news.html`.
While the path says template it is just plain html.
To add a new item copy one of the `<div class="index-news-item">` blocks
and add it at the top.
Once copied update the item title, href and descriptive text.
