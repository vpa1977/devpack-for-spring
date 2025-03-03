#!/bin/sh

make prepare
(cd devpack-for-spring-manifest && snapcraft)
(cd devpack-for-spring && snapcraft)
spread $*
