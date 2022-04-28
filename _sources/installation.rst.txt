Installation
============

Here you can find instructions on how to install Mantid on various platforms.
We currently offer ``x86_64``
:ref:`standalone installers <installation_standalone>` bundling all
components on:



We also offer ``x86_64`` :ref:`Conda packages <installation_conda>` that offer
more fine-grained control over installed components.

Please see the relevant sections below for installation prerequisites
and instructions.

.. _installation_standalone:

Standalone Workbench Installers
-------------------------------

- RedHat/CentOS 7
- Ubuntu 18.04
- Windows 10
- macOS (High Sierra+)

Latest Release
##############

Windows/macOS
~~~~~~~~~~~~~

.. raw:: html
   :file: installation_latest_win_mac.html

Linux
~~~~~

.. raw:: html
   :file: installation_latest_linux.html


Nightly Build
#############

.. include:: ./nightly_build_warning.rst

.. .. raw:: html
..    :file: download_latest.html

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

.. include:: ./nightly_build_warning.rst

If you wish to use a nightly build then add the ``nightly`` label
to the channel:

.. code-block:: sh

   conda install -c mantid/label/nightly mantid
