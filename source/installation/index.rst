:orphan:

Installation
============

Here you can find instructions on how to install Mantid on various platforms.
We currently offer:

- :ref:`full installers <installation_full>` bundling
  all components (64-bit, Intel)
- :ref:`Conda packages <installation_conda>` for use with the
  `conda package manager <https://docs.conda.io/en/latest/>`__ (64-bit, Intel)

Please see the relevant sections for installation instructions.

.. _installation_full:

Full Installers
---------------

Latest Release
##############

.. raw:: html
   :file: latest.html

Instructions:

- :doc:`Windows <windows>`
- :doc:`macOS <macos>`
- :doc:`Linux <linux>`: Starting with version ``6.4`` the above `.xz` file for Linux can
  simply be extracted and run on any modern Linux (>2010) system.
  Prior and up to versions ``6.4``, ``rpm`` and ``deb`` versions are available for
  Red Hat/CentOS 7 and various versions of Ubuntu: 18.04, 16.04, 14.04.

Nightly Build
#############

.. include:: ./nightly_build_warning.txt


.. _installation_conda:

Conda
-----

Our packages are available through our `mantid <https://anaconda.org/mantid>`__
channel on Anaconda.org. The available packages are:

- ``mantid``: Python library accessing algorithms and workspaces.

- ``mantidqt`` Python library providing custom Qt widgets such as
  instrument viewer, slice viewer for use in other applications.

- ``mantidworkbench``: General-purpose graphical-user-interface for plotting,
  writing scripts etc.

Latest Release
##############

To install any of the packages simply use the `-c` option in Conda to add the
mantid channel and then the package name:

.. code-block:: sh

   conda install -c mantid mantid

Nightly Build
#############

.. include:: ./nightly_build_warning.txt

If you wish to use a nightly build then add the ``nightly`` label
to the channel:

.. code-block:: sh

   conda install -c mantid/label/nightly mantid
