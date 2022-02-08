Privacy Policy
==============

General Scope
-------------

This policy covers personally identifiable information collected or stored by the Mantid
project on its servers in relation to the Project and its community.
Consistent with the UK Data Protection Policy, the project collects and retains
the least amount of personally identifiable information needed to fulfill the Projects
operational needs.

The Public and Collaborative Nature of the Projects
---------------------------------------------------

The Mantid project requires users to register an account in order to contribute
within the Mantid Project, either to the project Wiki or to the project code.
By editing documents in the wiki, users create a published document,
and a public record of every word added, subtracted, or changed.
This is a public act, and editors are identified publicly as the author of such changes.
All contributions made to the Project, and all publicly available information about
those contributions, are irrevocably licensed and may be freely copied,
quoted, reused and adapted by third parties with few restrictions.

Activities on Mantid Collaboration Projects
-------------------------------------------

In general, this Policy only applies to private information stored or held by the
Mantid project which is not publicly available.

Interactions with the Mantid not covered by this Policy include,
but are not limited to, aspects of browsing and editing pages,
use of the wiki "email user" function, subscribing and posting to mantid
hosted email lists, and corresponding with collaborators via the projects ticketing system.
These interactions may reveal a contributor's IP address, and possibly other personal information,
indiscriminately to the general public, or to specific groups of volunteers acting independently
of the collaboration.

Users may also interact with one another outside of Mantid project site, via email, IRC or other chat,
or independent websites, and should assess the risks involved, and their personal need for
privacy, before using these methods of communication.

Purpose of the Collection of Private Information
------------------------------------------------

The Mantid project limits the collection of personally identifiable user data to
purposes which serve the well-being of the project, including but not limited to
the following:

- To enhance the public accountability of the project.
  The project recognizes that any system that is open enough to allow the greatest
  possible participation of the general public will also be vulnerable to certain
  kinds of abuse and counterproductive behavior.
  In this case the Administrators of the site may remove access to those users or
  block specified IP addresses.

- To provide site statistics. The project statistically samples raw log data from
  users' visits. These logs are used to produce the site statistics pages; the
  raw log data is not made public.

- To solve technical problems. Log data may be examined by developers in the course
  of solving technical problems and in tracking down badly-behaved web spiders that
  overwhelm the site.

Details of Data Retention
-------------------------

.. _usage_data_recorded_in_mantid:

Usage Data Recorded in Mantid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/workbench_startup_window.png
   :alt: Image of first-time startup screen in Workbench
   :align: right
   :scale: 30 %

Mantid records a limited number of metrics that are
used to help direct the future direction of the
project and allow the resources of the development
team to focus on the more commonly used areas of
functionality.
All of this usage recording is
optional, and can be opted out of in the "Welcome
to Mantid" first use screen, and can be revisited
at any time using the Help->First Time Setup menu
option.
The information recorded is stored in an
off site server, the sections below detail what
information is stored.

Startup Usage
#############

Mantid reports when it is started, and again once per day, to allow us to monitor
its daily usage.
The startup reports record the following:

- A user ID
- A computer ID
- The operating system name and version of the computer
- The Paraview version (if any) on the computer
- The version of Mantid
- The application name using Mantid
- The data and time of Mantid starting
- The nearest city that can be identified for the
  location of the computer

The User and Computer ids are unique but not identifiable.
They are transmitted and stored using an MD5 checksum so the computer or user
account cannot be identified.
The IP address from which the usage report is sent is briefly processed to geolocate
the nearest city, but neither the more detailed location or ip address is stored.

All of this data is visible through our publicly available usage reporting
service at https://reports.mantidproject.org.

Feature Usage
#############

Mantid also records some summary information about the features that are used
within Mantid, this information is accumulated within the application
and set out every 5 minutes (by default).
We only record how many times a feature is used within a version of Mantid,
no identifiable information is stored.

We store:

- The type of feature used (e.g. Algorithm, Interface,
  or feature within an interface)
- The name of the feature used
- Whether that feature was used directly by a
  user, or as part of some internal process
- The version of Mantid it was used in
- The number of times this feature has been used

Error Report Data Recorded in Mantid
####################################

After encountering serious errors, Mantid collects a limited number of metrics.
This collection is important for helping us to identify those parts of
the code that require attention and it helps us to provide a more stable package
over all. All of this reporting is optional.
If usage reporting is disabled (see :ref:`usage_data_recorded_in_mantid`),
then nothing will be collected.
If usage data is being recorded, then upon error detection a pop-up
window will ask for permission to collect additional information.
There are three options for reporting, the information collected; each case is
detailed below.

Yes, share information
^^^^^^^^^^^^^^^^^^^^^^

In this case, we will collect information that
allows us to identify who has had the error; we may
contact you directly to see if we can help with the
problem. We will collect:

- The fact that an error occurred
- Username (optional)
- Email (optional)
- Exit error code
- Operating system
- Mantid uptime (how long has the current instance been running)
- Default facility
- Default instrument
- Text in the free text box
- User ID
- Host ID
- A copy of the Mantid recovery files on your
  machine (These contain the information required
  to replicate the state of the Mantid session
  which just crashed as well as any other open
  Mantid sessions)

Share non-identifiable information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, we will collect only information that
cannot be traced back to the specific user. There
is still a lot of information that is useful to us
here. **Note** hashing is a one-way function that
encrypts the arbitrary length ID to a fixed length
string; this operation cannot be reversed.

- The fact that an error occurred
- Exit error code
- Operating system
- Mantid uptime (how long has the current instance been running)
- Default facility
- Default instrument
- Text in the free text box
- Hashed user ID
- Hashed host ID

Don't share any information
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case we will only report back that Mantid
has encountered an error, nothing else.

-  The fact that an error occurred

Recalling Information
---------------------

As these records are potentially identifiable, we will remove any records
for a particular user, on request. This can be requested by contacting the
Mantid team using ``mantid-help@mantidproject.org``.

Disclaimer
----------

The Mantid project believes that maintaining and preserving the privacy of
user data is an important value.
This Privacy Policy, together with other policies, resolutions, and actions
by the collaboration, represents a committed effort to safeguard the security
of the limited user information that is collected and retained on our servers.
Nevertheless, the project cannot guarantee that user information will remain
private.
We acknowledge that, in spite of our committed effort to protect private user
information, determined individuals may still develop data-mining and other
methods to uncover such information and disclose it.
For this reason, the project can make no guarantee against unauthorized access
to information provided in the course of participating in the Mantid project.
