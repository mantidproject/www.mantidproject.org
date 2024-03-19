:orphan:

Conda Troubleshooting
=====================

Before using the troubleshooting below please ensure you are using Mambaforge. Using mamba is preferable over conda as it's faster and better at resolving dependencies.
To install mambaforge please follow `this documentation <https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html>`__

Issues
------

- :ref:`Unable to find mantid or mantidworkbench <unable_to_find>`
- :ref:`Installing on Apple silicon devices <osx_install>`
- :ref:`Unable to resolve dependencies <dependency_fail>`
- :ref:`404 error when trying to install <404_error>`

.. _unable_to_find:

Unable to find `mantid` or `mantidworkbench`
############################################

.. code-block:: sh
	PackagesNotFoundError: The following packages are not available from current channels
	
If you get this error it may be because you have not included the mantid channel in your download command. Please ensure you include `-c mantid` when installing. 

Example

.. code-block:: sh

   mamba create -n mantid_env -c mantid mantid
   
You can also get this error when trying to install on Apple silicon devices. See :ref:`Installing on Apple silicon devices <osx_install>` for help.

.. _osx_install:

Installing on Apple silicon devices 
###################################

For macOS we currently only provide x86 packages. These can still be used by those with Apple silicon devices (M1, M2). You will need to have Rosetta installed and precede the setup commands with 'CONDA_SUBDIR=osx-64'.
For example if you want to install mantidworkbench use the following command:

.. code-block:: sh

	CONDA_SUBDIR=osx-64 mamba create -n mantid_env -c mantid mantidworkbench

.. _dependency_fail:

Unable to resolve dependencies
##############################

If you are having problems with dependencies we recommend installing Mantid into a new clean environment. Please do not specify any dependency versions e.g. Python. Any dependencies will be installed automatically of the version required to use Mantid.

.. _404_error:

404 error when trying to install
################################

Mantid is available through `conda-forge`. To access the Mantid channel please check your `.condarc` file. It should contain the following

.. code-block:: sh

	channels:
		- conda-forge

or

.. code-block:: sh

	channels: [conda-forge]
	
If either of these are in the file then please make sure there are no other channels added for accessing Mantid. For example any of the following will cause a 404 error and should be removed from `.condarc`

.. code-block:: sh

	channels:
		- https://anaconda.org/mantid
		- mantid

Still having problems?
######################

If the above has not resolved your problem please post to our `community forum <https://forum.mantidproject.org>` or e-mail the tean directly on ``mantid-help@mantidproject.org``.
