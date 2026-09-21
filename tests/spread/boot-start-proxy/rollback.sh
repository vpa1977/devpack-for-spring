#!/usr/bin/env bash

set -e

if [ -f /etc/iptables.rules ]; then
    iptables-restore < /etc/iptables.rules
fi
