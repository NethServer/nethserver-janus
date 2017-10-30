==================
nethserver-janus
==================

This package configure Janus Gateway https://github.com/meetecho/janus-gateway

NAT modes
=========

Janus-gateway can operate in three different NAT mode:

- STUN (default)

- ICE

- 1:1 NAT

there are 4 prop in janus-gateway key to configure NAT mode and options:

`NatMode`  <stun|ice|1:1>

`StunServer` is the STUN server to use. Default is stun1.l.google.com. Ignored if mode isn't stun

`StunPort` is the STUN server port. Default is 19302. Ignored if mode isn't stun

`PublicIP` is the public IP address of the server that runs janus-gateway . Ignored if mode isn't 1:1

For configuring TURN, create a template custom

