#!/usr/bin/env bash

set -e

systemctl stop squid
apt-get purge --auto-remove squid-openssl
rm -rf /etc/squid /var/lib/squid /var/spool/squid /var/log/squid /usr/lib/squid

if [ -f /etc/iptables.rules ]; then
    iptables-restore < /etc/iptables.rules
fi
