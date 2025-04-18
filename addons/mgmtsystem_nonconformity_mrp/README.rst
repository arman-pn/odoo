=====================================
Management System - Nonconformity MRP
=====================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:02a07e8ff707a192020188869ca41827debb716599dcf23dfae9f04bf3c4ab4c
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fmanagement--system-lightgray.png?logo=github
    :target: https://github.com/OCA/management-system/tree/18.0/mgmtsystem_nonconformity_mrp
    :alt: OCA/management-system
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/management-system-18-0/management-system-18-0-mgmtsystem_nonconformity_mrp
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/management-system&target_branch=18.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This is a bridge module between Management System and MRP

This module contains some new features for Management System modules.

Nonconformity (NC)

- Workcenter: add a field to link a specific workcenter. Manage Work
  Order Operations option has to be checked to show the field.

**Table of contents**

.. contents::
   :local:

Installation
============

This module will be automatically installed

Configuration
=============

Workcenter has to be enabled:

- Go to Settings → Users and select a user.
- Go to Technical Settings and check Manage Work Order Operations

Usage
=====

NC Workcenter

- Go to Manufacturing → Work Centers → create a new one
- Go to Management System → Nonconformity
- Create new Nonconformity
- Select a Workcenter on the list

Known issues / Roadmap
======================



Changelog
=========

11.0.1.0.0 (2019-04-01)
-----------------------

- [INI] Initial development

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/management-system/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/management-system/issues/new?body=module:%20mgmtsystem_nonconformity_mrp%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Associazione PNLUG - Gruppo Odoo

Contributors
------------

- Marcelo Frare <mf2965@gmail.com>
- Stefano Consolaro <stefano.consolaro@mymage.it>
- [Heliconia Solutions Pvt. Ltd.](https://www.heliconia.io)

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/management-system <https://github.com/OCA/management-system/tree/18.0/mgmtsystem_nonconformity_mrp>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
