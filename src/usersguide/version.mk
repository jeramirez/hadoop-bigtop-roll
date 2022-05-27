ROLL			= hadoop-bigtop
VERSION			= 1.5.0
NAME    		= roll-$(ROLL)-usersguide
RELEASE			= 0

SUMMARY_COMPATIBLE	= $(VERSION)
SUMMARY_MAINTAINER	= Rocks Group
SUMMARY_ARCHITECTURE	= x86_64

ROLL_REQUIRES		= base kernel os
ROLL_CONFLICTS		=

RPM.ARCH = noarch
RPM.FILES = /var/www/html/roll-documentation/$(ROLL)/$(VERSION)
