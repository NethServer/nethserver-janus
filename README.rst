==================
nethserver-janus
==================

This package configure Janus Gateway https://github.com/meetecho/janus-gateway

Start Janus Gateway at boot
===========================

To start Janus Gateway and enable it at boot, execute: ::

  config setprop janus-gateway status enabled
  signal-event nethserver-janus-update


NAT modes
=========

Janus-gateway can operate in three different NAT mode:

- STUN (default)

- ICE

- 1:1 NAT

There are 4 prop under ``janus-gateway`` key to configure NAT mode and options:

- ``NatMode``  <stun|ice|1:1>

- ``StunServer`` is the STUN server to use. Default is stun1.l.google.com. Ignored if mode isn't stun

- ``StunPort`` is the STUN server port. Default is 19302. Ignored if mode isn't stun

- ``PublicIP`` is the public IP address of the server that runs janus-gateway . Ignored if mode isn't 1:1

For configuring TURN, create a template custom

STUN and ICE enforced interfaces
================================

You can choose which interface should be used for the ICE candidates gathering. In default configuration Janus try to use all interfaces, except 'vmnet*', that is VMware interface which is known to cause problems, 'tun*' and 'tap*' interfaces. You can modify this behavior by explicit list interfaces to use or by listing interfaces to exclude. You can configure one of those two props:

- ``ICEEnforceList`` comma separated list of interfaces to use for ICE gathering. For instances "e0,e1".

- ``ICEIgnoreList`` comma separated list of interfaces to exclude from ICE gathering. Janus will use all interfaces except those. For instance 'e3,vmnet,10.0.0'.

Disable plugins
===============

All plugins are enabled by default. To disable some of them execute:

.. code:: bash

  config setprop janus-gateway DisabledPlugins "<PLUGINS_NAMES_SEPARATED_BY_COMMAS>"
  signal-event nethserver-janus-update
  
Example:

.. code:: bash

  config setprop janus-gateway DisabledPlugins "libjanus_voicemail.so,libjanus_recordplay.so"
  signal-event nethserver-janus-update
  
To re-enable them:

.. code:: bash

  config setprop janus-gateway DisabledPlugins ""
  signal-event nethserver-janus-update
