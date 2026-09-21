#!/usr/bin/env bash

set -e

if [ -f /etc/iptables.rules ]; then
    iptables-restore < /etc/iptables.rules
    rm -f /etc/iptables.rules
fi

systemctl is-active --quiet squid && sudo systemctl stop squid
rm -rf /etc/squid /var/lib/squid /var/spool/squid /var/log/squid /usr/lib/squid
apt-get purge -y --auto-remove squid-openssl
