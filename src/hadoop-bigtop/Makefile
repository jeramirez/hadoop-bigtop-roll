# $Id$
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWinder)
# 		         version 7.0 (Manzanita)
# 
# Copyright (c) 2000 - 2017 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log$

REDHAT.ROOT = $(CURDIR)/../../
REDHAT.RPMS = $(REDHAT.ROOT)/RPMS

ROCKS.OS.VERSION.MAJOR=$(shell lsb_release -rs | cut -d . -f 1)

ifeq ($(strip $(ROCKS.OS.VERSION.MAJOR)), 6)
VERSION.MAJOR = 6
else
ifeq ($(strip $(ROCKS.OS.VERSION.MAJOR)), 7)
VERSION.MAJOR = 7
else
VERSION.MAJOR = 8
endif
endif

rpm pkg::
	./download.$(VERSION.MAJOR)
	for i in $(CURDIR)/$(VERSION.MAJOR)/x86_64/* ; do \
		if [ ! -d $(REDHAT.RPMS)/x86_64 ] ; then \
			mkdir $(REDHAT.RPMS)/x86_64 ; \
		fi ; \
		if [ ! -f $(REDHAT.RPMS)/x86_64/$$i ] ; then \
			cp -p $$i $(REDHAT.RPMS)/x86_64 ; \
		fi ; \
	done
	for i in $(CURDIR)/$(VERSION.MAJOR)/noarch/* ; do \
		if [ ! -d $(REDHAT.RPMS)/noarch ] ; then \
			mkdir $(REDHAT.RPMS)/noarch ; \
		fi ; \
		if [ ! -f $(REDHAT.RPMS)/noarch/$$i ] ; then \
			cp -p $$i $(REDHAT.RPMS)/noarch ; \
		fi ; \
	done

clean::
	echo rm -rf $(REDHAT.RPMS)/*
