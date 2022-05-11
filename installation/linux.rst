:orphan:

Linux Packages
==============

Red Hat/CentOS 7
----------------

Setup
#####

Enable the `Extra Packages for Enterprise Linux (EPEL) <https://docs.fedoraproject.org/en-US/epel/#_el7>`_
repositories.

Activate the yum repository for the version of Mantid you require by
downloading the appropriate repository configuration file and saving it to ``/etc/yum.repos.d``:

- `stable release <_static/isis-rhel.repo>`__
- `nightly build <_static/isis-rhel-testing.repo>`__

Installation
############

Install the version of Mantid you require with:

- stable release: ``yum install mantid``. Installs to ``/opt/Mantid``
- nightly build: ``yum install mantidnightly``. Installs to ``/opt/mantidnightly``

Run
###

To run MantidWorkbench:

- stable release: ``/opt/Mantid/bin/mantidworkbench``
- nightly build: ``/opt/mantidnightly/bin/mantidworkbench``

Ubuntu
------

Setup
#####

Enable the ``mantid`` prerequisites PPA:

.. code-block:: sh

   sudo apt-add-repository ppa:mantid/mantid

Add the ``mantid`` signing key to your key chain:

.. code-block:: sh

   wget -O - http://apt.isis.rl.ac.uk/2E10C193726B7213.asc | sudo apt-key add -

Activate the apt repository for the version of Mantid you require by running:

- stable release: ``sudo apt-add-repository "deb [arch=amd64] http://apt.isis.rl.ac.uk $(lsb_release -c | cut -f 2) main"``
- nightly build: ``sudo apt-add-repository "deb [arch=amd64] http://apt.isis.rl.ac.uk $(lsb_release -c | cut -f 2)-testing main"``

and force an apt update:

.. code-block:: sh

   sudo apt-get update

Installation
############

Install the version of Mantid you require with:

- stable release: ``apt install mantid``. Installs to ``/opt/Mantid``
- nightly build: ``apt install mantidnightly``. Installs to ``/opt/mantidnightly``

Run
###

To run MantidWorkbench:

- stable release: ``/opt/Mantid/bin/mantidworkbench``
- nightly build: ``/opt/mantidnightly/bin/mantidworkbench``
