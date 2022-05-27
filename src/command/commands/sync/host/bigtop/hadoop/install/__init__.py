# $Id$
# 
# @Copyright@
#
# $Log$
# Revision 0.0  2012/11/09 05:48:55  eduardo
# Copyright Storm for Mamba
#

import os
import time
import rocks.commands
import threading

max_threading = 512
timeout = 30.0

class Parallel(threading.Thread):
	def __init__(self, cmd):
		threading.Thread.__init__(self)
		self.cmd = cmd

	def run(self):
		os.system(self.cmd)


class Command(rocks.commands.sync.host.command):
	"""
	Install hadoop on the named hosts.

	<param type="bool" name="test">
	If want to test output set this parameter.
	Default is no.
	</param>


	<example cmd='sync host bigtop hadoop install node-0-0'>
	add hdfs user, add hadoop group, and install hadoop rpms
        on host node-0-0 if attr BIGTOP_HADOOP is set on host.
	</example>

	<example cmd='sync host bigtop hadoop install node-0-0 test=yes'>
	Show the bash script that will run to install hadoop on host node-0-0
	</example>
	"""

	def run(self, params, args):
		hosts = self.getHostnames(args, managed_only=1)
		istest, = self.fillParams([ ('test', 'n') ])
		istest = self.str2bool(istest)

		threads = []
		for host in hosts:
			if max_threading > 0:
				while threading.activeCount() > max_threading:
					#
					# need to wait for some threads to
					# complete before starting any new ones
					#
					time.sleep(0.001)

			#
			# get the attributes for the host
			#
			attrs           = self.db.getHostAttrs(host)
			bigtop_hadoop   = self.db.getHostAttr(host,'BIGTOP_HADOOP')
			trigger_install = bigtop_hadoop

			cmd = '/opt/rocks/bin/rocks report host bigtop hadoop install '
			cmd += '%s | ' % host
			cmd += '/opt/rocks/bin/rocks report script '

			if istest:
				cmd += 'attrs="%s" ' % attrs
				cmd += ';echo " | ssh %s bash" ' % host
				if trigger_install :
					cmd += ';echo " [BIGTOP_HADOOP =%s] will run on host %s" ' % (bigtop_hadoop,host)
				else:
					cmd += ';echo " [BIGTOP_HADOOP =%s] will NOT run on host %s" ' % (bigtop_hadoop,host)
			else:
				cmd += 'attrs="%s" | ' % attrs
				cmd += 'ssh %s bash > /dev/null 2>&1 ' % host


			if trigger_install or istest:
				p = Parallel(cmd)
				threads.append(p)
				p.start()

		#
		# collect the threads
		#
		for thread in threads:
			thread.join(timeout)

		threads = []
