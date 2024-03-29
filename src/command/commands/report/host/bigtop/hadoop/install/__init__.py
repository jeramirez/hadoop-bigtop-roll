#$Id$
# 
# @Copyright@
# 
# $Log$
# Revision 0.10  2012/10/26 05:48:54  eduardo
# Creation
#

import sys
import os
import pwd
import string
import types
import rocks.commands
from syslog import syslog

class Command(rocks.commands.HostArgumentProcessor,
	rocks.commands.report.command):
	"""

	Output the BIGTOP hadoop wrapper install script
	Uses Rocks Attributes: BIGTOP_HADOOP,rocks_version_major,
        BIGTOP_Hadoop_StartDaemonDataNode,BIGTOP_Hadoop_StartDaemonNameNode,
	BIGTOP_Hadoop_StartDaemonSecondaryNameNode

	<arg type='string' name='host'>
	One host name.
	</arg>

	<example cmd='report host bigtop hadoop install hadoop-0-0'>
	Create wrapper script to install BIGTOP hadoop for hadoop-0-0
	</example>

	"""

	def writeProperty(self, Pname, Pvalue, xmlFile):
		self.addOutput(self.host, '   echo "&lt;property>" &gt;&gt; %s' % xmlFile)
		self.addOutput(self.host, '   echo "&lt;name>%s&lt;/name>" &gt;&gt; %s' % (Pname,xmlFile))
		self.addOutput(self.host, '   echo "&lt;value>%s&lt;/value>" &gt;&gt; %s' % (Pvalue,xmlFile))
		self.addOutput(self.host, '   echo "&lt;/property>" &gt;&gt; %s' % xmlFile)

	def OpenConfiguration(self, xmlFile):
		self.addOutput(self.host, '   echo "&lt;?xml version=\\"1.0\\"?>" &gt;&gt; %s' % xmlFile )
		self.addOutput(self.host, '   echo "&lt;?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>" &gt;&gt; %s' % xmlFile )
		self.addOutput(self.host, '   echo "" &gt;&gt; %s' % xmlFile)
		self.addOutput(self.host, '   echo "&lt;!-- Template created by rocks report bigtop hadoop install -->" &gt;&gt; %s' % xmlFile)
		self.addOutput(self.host, '   echo "" &gt;&gt; %s' % xmlFile)
		self.addOutput(self.host, '   echo "&lt;configuration>" &gt;&gt; %s' %xmlFile)

	def CloseConfiguration(self, xmlFile):
		self.addOutput(self.host, '   echo "&lt;/configuration>" &gt;&gt; %s' % xmlFile)

#	def FixGid(self, thegid, thegroup):
#		self.addOutput(self.host, 'swapgid=`getent group %s | cut -d: -f3`' % thegroup)
#		self.addOutput(self.host, 'swapgroup=`getent group %s | cut -d: -f1`' % thegid)
#		self.addOutput(self.host, '[ ! -z "$swapgroup" ]&amp;&amp;[ "x$swapgroup" != "x%s" ]&amp;&amp;/usr/sbin/groupmod -o -g $swapgid $swapgroup' % thegroup)
#		self.addOutput(self.host, '/usr/sbin/groupmod -g %s %s' % (thegid,thegroup))

#	def FixUid(self, theuid, theuser):
#		self.addOutput(self.host, 'swapuid=`getent passwd %s | cut -d: -f3`' % theuser)
#		self.addOutput(self.host, 'swapuser=`getent passwd %s | cut -d: -f1`' % theuid)
#		self.addOutput(self.host, '[ ! -z "$swapuser" ]&amp;&amp;[ "x$swapuser" != "x%s" ]&amp;&amp;/usr/sbin/usermod -o -u $swapuid $swapuser' % theuser)
#		self.addOutput(self.host, '/usr/sbin/usermod -u %s %s' % (theuid,theuser))

	def run(self, params, args):

		self.beginOutput()

                for host in self.getHostnames(args):
			self.host = host
			loginstall  = '/var/log/hadoop-install.log'
			hostexclude = '/etc/hadoop/conf/hosts_exclude'
			envsh       = '/etc/hadoop/conf/hadoop-env.sh'
			hadoopenvsh = '/etc/hadoop/conf/hadoop-env.sh.template'
			hdfssitexml = '/etc/hadoop/conf/hdfs-site.xml.template'
			coresitexml = '/etc/hadoop/conf/core-site.xml.template'
			maprsitexml = '/etc/hadoop/conf/mapred-site.xml.template'
			hadoopconfg = '/root/HadoopConfigurator'
			bigtop_hadoop   = self.db.getHostAttr(host,'BIGTOP_HADOOP')
			rocks_ver       = self.db.getHostAttr(host,'rocks_version_major')
			datadaemon      = self.db.getHostAttr(host,'BIGTOP_Hadoop_StartDaemonDataNode')
			namedaemon      = self.db.getHostAttr(host,'BIGTOP_Hadoop_StartDaemonNameNode')
			seconddaemon    = self.db.getHostAttr(host,'BIGTOP_Hadoop_StartDaemonSecondaryNameNode')
			trigger_install = bigtop_hadoop 
			if trigger_install:
#				self.addOutput(self.host, '/usr/sbin/groupadd -g &OSG_fusegid; fuse')
#				self.FixGid('&OSG_fusegid;','fuse')
#				self.addOutput(self.host, '/usr/sbin/groupadd -g &OSG_hadoopgid; hadoop')
#				self.FixGid('&OSG_hadoopgid;','hadoop')
#				self.addOutput(self.host, '/usr/sbin/groupadd -g &OSG_mapredgid; mapred')
#				self.FixGid('&OSG_mapredgid;','mapred')
#				self.addOutput(self.host, '/usr/sbin/groupadd -g &OSG_zookeepergid; zookeeper')
#				self.FixGid('&OSG_zookeepergid;','zookeeper')
#				self.addOutput(self.host, '/usr/sbin/groupadd -g &OSG_gratiagid; gratia')
#				self.FixGid('&OSG_gratiagid;','gratia')
#				self.addOutput(self.host, '/usr/sbin/useradd -r -u &OSG_hdfsuid; -g &OSG_hadoopgid; -c "Hadoop HDFS" -s /bin/bash -d /home/hadoop -m -k /etc/skel hdfs')
#				self.FixUid('&OSG_hdfsuid;','hdfs')
#				self.addOutput(self.host, '/usr/sbin/useradd -r -u &OSG_mapreduid; -g &OSG_mapredgid; -c "Hadoop MapReduce" -s /bin/bash -d /usr/lib/hadoop-hdfs mapred')
#				self.FixUid('&OSG_mapreduid;','mapred')
#				self.addOutput(self.host, '/usr/sbin/useradd -r -u &OSG_zookeeperuid; -g &OSG_zookeepergid; -c "ZooKeeper" -s /bin/nologin -d /var/run/zookeeper zookeeper')
#				self.FixUid('&OSG_zookeeperuid;','zookeeper')
#				self.addOutput(self.host, '/usr/sbin/useradd -r -u &OSG_gratiauid; -g &OSG_gratiagid; -c "gratia runtime user" -s /bin/nologin -d /etc/gratia gratia')
#				self.FixUid('&OSG_gratiauid;','gratia')
#				self.addOutput(self.host, '')
				self.addOutput(self.host, 'touch %s' % loginstall )
				self.addOutput(self.host, 'yum -y install hadoop-client  &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				self.addOutput(self.host, 'yum -y install hadoop-hdfs-fuse  &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				self.addOutput(self.host, 'yum -y install hadoop-hdfs-datanode  &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				self.addOutput(self.host, 'yum -y install hadoop-hdfs-namenode  &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				self.addOutput(self.host, 'yum -y install hadoop-hdfs-secondarynamenode  &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				self.addOutput(self.host, 'yum -y install java  &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				self.addOutput(self.host, 'touch %s' % hostexclude )
				self.addOutput(self.host, '')
				self.addOutput(self.host, '#Make sure services are turned off to prevent upgrade cases')
				if rocks_ver == "7":
					self.addOutput(self.host, 'systemctl disable hadoop-hdfs-datanode &gt;&gt; %s 2&gt;&amp;1' % loginstall)
					self.addOutput(self.host, 'systemctl disable hadoop-hdfs-namenode &gt;&gt; %s 2&gt;&amp;1' % loginstall)
					self.addOutput(self.host, 'systemctl disable hadoop-hdfs-secondarynamenode &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				else:
					self.addOutput(self.host, 'chkconfig hadoop-hdfs-datanode off &gt;&gt; %s 2&gt;&amp;1' % loginstall)
					self.addOutput(self.host, 'chkconfig hadoop-hdfs-namenode off &gt;&gt; %s 2&gt;&amp;1' % loginstall)
					self.addOutput(self.host, 'chkconfig hadoop-hdfs-secondarynamenode off &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				self.addOutput(self.host, '')
				self.addOutput(self.host, '#Turn on services if flags are set')
				if rocks_ver == "7" and datadaemon:
					self.addOutput(self.host, 'systemctl enable hadoop-hdfs-datanode &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				if rocks_ver == "7" and namedaemon:
					self.addOutput(self.host, 'systemctl enable hadoop-hdfs-namenode &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				if rocks_ver == "7" and seconddaemon:
					self.addOutput(self.host, 'systemctl enable hadoop-hdfs-secondarynamenode &gt;&gt; %s 2&gt;&amp;1' % loginstall)
				self.addOutput(self.host, '#Make sure config templates exists')
#				template for hadoop-env.sh
				self.addOutput(self.host, 'hadoopenvshcreate=0')
				self.addOutput(self.host, '[ -f %s ]||echo "Creating %s" &gt;&gt; %s 2&gt;&amp;1' % (hadoopenvsh,hadoopenvsh,loginstall) )
				self.addOutput(self.host, '[ -f %s ]||hadoopenvshcreate=1' % hadoopenvsh)
				self.addOutput(self.host, 'echo "   hadoopenvshcreate=$hadoopenvshcreate" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, 'if [ "x$hadoopenvshcreate" == "x1" ]; then')
				self.addOutput(self.host, '   echo "passed if hadoopenvshcreate is 1" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, '   hadoopenvshcopy=1')
				self.addOutput(self.host, '   [ -f %s ]||hadoopenvshcopy=0' % envsh)
				self.addOutput(self.host, '   echo "   hadoopenvshcopy=$hadoopenvshcopy" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, '   if [ "x$hadoopenvshcopy" == "x1" ]; then')
				self.addOutput(self.host, '      echo "   passed if hadoopenvshcopy is 1" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, '      sed -e "s/#export HADOOP_HEAPSIZE=/export HADOOP_HEAPSIZE=@HADOOP_NAMENODE_HEAP@/" &lt; %s &gt; %s' % (envsh,hadoopenvsh) )
				self.addOutput(self.host, '   else')
				self.addOutput(self.host, '      touch %s' % hadoopenvsh )
				self.addOutput(self.host, '      echo "# The maximum amount of heap to use, in MB. Default is 1000." &gt;&gt; %s' % hadoopenvsh )
				self.addOutput(self.host, '      echo "export HADOOP_HEAPSIZE=@HADOOP_NAMENODE_HEAP@" &gt;&gt; %s' % hadoopenvsh )
				self.addOutput(self.host, '   fi')
				self.addOutput(self.host, '')
				self.addOutput(self.host, 'else')
				self.addOutput(self.host, '   echo "NOT created hadoopenvshcreate is 0" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, 'fi')
				self.addOutput(self.host, '')
#				template for hdfs-site.xml
				self.addOutput(self.host, 'hdfssitexmlcreate=0')
				self.addOutput(self.host, '[ -f %s ]||echo "Creating %s" &gt;&gt; %s 2&gt;&amp;1' % (hdfssitexml,hdfssitexml,loginstall) )
				self.addOutput(self.host, '[ -f %s ]||hdfssitexmlcreate=1' % hdfssitexml)
				self.addOutput(self.host, 'echo "   hdfssitexmlcreate=$hdfssitexmlcreate" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, 'if [ "x$hdfssitexmlcreate" == "x1" ]; then')
				self.addOutput(self.host, '   echo "passed if hdfssitexmlcreate is 1" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, '   touch %s' % hdfssitexml )
				self.OpenConfiguration(hdfssitexml)
				self.writeProperty('dfs.block.size','@HADOOP_DATANODE_BLOCKSIZE@',hdfssitexml)
				self.writeProperty('dfs.replication','@HADOOP_REPLICATION_DEFAULT@',hdfssitexml)
				self.writeProperty('dfs.replication.max','@HADOOP_REPLICATION_MAX@',hdfssitexml)
				self.writeProperty('dfs.replication.min','@HADOOP_REPLICATION_MIN@',hdfssitexml)
				self.writeProperty('dfs.datanode.du.reserved','10000000000',hdfssitexml)
				self.writeProperty('dfs.balance.bandwidthPerSec','2000000000',hdfssitexml)
				self.writeProperty('dfs.data.dir','@HADOOP_DATA@',hdfssitexml)
				self.writeProperty('dfs.datanode.handler.count','10',hdfssitexml)
				self.writeProperty('dfs.hosts.exclude','@HADOOP_CONF_DIR@/hosts_exclude',hdfssitexml)
				self.writeProperty('dfs.namenode.name.dir','@HADOOP_NAMENODE_NAME_DIR@',hdfssitexml)
				self.writeProperty('dfs.namenode.handler.count','40',hdfssitexml)
				self.writeProperty('dfs.namenode.logging.level','all',hdfssitexml)
				self.writeProperty('fs.checkpoint.dir','@HADOOP_CHECKPOINT_DIRS@',hdfssitexml)
				self.writeProperty('topology.script.file.name','@HADOOP_RACKAWARE_SCRIPT@',hdfssitexml)
				self.writeProperty('dfs.secondary.http.address','@HADOOP_SECONDARY_HTTP_ADDRESS@',hdfssitexml)
				self.writeProperty('dfs.http.address','@HADOOP_PRIMARY_HTTP_ADDRESS@',hdfssitexml)
				self.writeProperty('fs.checkpoint.period','@HADOOP_CHECKPOINT_PERIOD@',hdfssitexml)
				self.writeProperty('dfs.permissions.supergroup','root',hdfssitexml)
				self.writeProperty('dfs.client.read.shortcircuit','true',hdfssitexml)
				self.writeProperty('dfs.client.file-block-storage-locations.timeout.millis','10000',hdfssitexml)
				self.writeProperty('dfs.domain.socket.path','/var/run/hadoop-hdfs/dn._PORT',hdfssitexml)
				self.writeProperty('dfs.datanode.hdfs-blocks-metadata.enabled','true',hdfssitexml)
				self.CloseConfiguration(hdfssitexml)
				self.addOutput(self.host, '')
				self.addOutput(self.host, 'else')
				self.addOutput(self.host, '   echo "NOT created hdfssitexmlcreate is 0" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, 'fi')
				self.addOutput(self.host, '')
#				template for core-site.xml
				self.addOutput(self.host, 'coresitexmlcreate=0')
				self.addOutput(self.host, '[ -f %s ]||echo "Creating %s" &gt;&gt; %s 2&gt;&amp;1' % (coresitexml,coresitexml,loginstall) )
				self.addOutput(self.host, '[ -f %s ]||coresitexmlcreate=1' % coresitexml)
				self.addOutput(self.host, 'echo "   coresitexmlcreate=$coresitexmlcreate" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, 'if [ "x$coresitexmlcreate" == "x1" ]; then')
				self.addOutput(self.host, '   echo "passed if coresitexmlcreate is 1" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, '   touch %s' % coresitexml )
				self.OpenConfiguration(coresitexml)
				self.writeProperty('fs.default.name','hdfs://@HADOOP_NAMENODE@:@HADOOP_NAMEPORT@',coresitexml)
				self.writeProperty('hadoop.tmp.dir','@HADOOP_SCRATCH@',coresitexml)
				self.writeProperty('dfs.umaskmode','@HADOOP_UMASK@',coresitexml)
				self.writeProperty('io.bytes.per.checksum','4096',coresitexml)
				self.writeProperty('hadoop.log.dir','@HADOOP_LOG@',coresitexml)
				self.CloseConfiguration(coresitexml)
				self.addOutput(self.host, '')
				self.addOutput(self.host, 'else')
				self.addOutput(self.host, '   echo "NOT created coresitexmlcreate is 0" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, 'fi')
				self.addOutput(self.host, '')
#				template for mapred-site.xml
				self.addOutput(self.host, 'maprsitexmlcreate=0')
				self.addOutput(self.host, '[ -f %s.original ]||echo "Creating %s" &gt;&gt; %s 2&gt;&amp;1' % (maprsitexml,maprsitexml,loginstall) )
				self.addOutput(self.host, '[ -f %s.original ]||maprsitexmlcreate=1' % maprsitexml)
				self.addOutput(self.host, 'echo "   maprsitexmlcreate=$maprsitexmlcreate" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, 'if [ "x$maprsitexmlcreate" == "x1" ]; then')
				self.addOutput(self.host, '   echo "passed if maprsitexmlcreate is 1" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, '   mv %s %s.original' % (maprsitexml,maprsitexml) )
				self.addOutput(self.host, '   touch %s' % maprsitexml )
				self.OpenConfiguration(maprsitexml)
				self.writeProperty('mapred.job.tracker','@HADOOP_TRACKER@:@HADOOP_TRACKERPORT@',maprsitexml)
				self.writeProperty('mapred.map.tasks','7919',maprsitexml)
				self.writeProperty('mapred.reduce.tasks','1543',maprsitexml)
				self.writeProperty('mapred.tasktracker.map.tasks.maximum','4',maprsitexml)
				self.writeProperty('mapred.tasktracker.reduce.tasks.maximum','4',maprsitexml)
				self.writeProperty('tasktracker.http.threads','50',maprsitexml)
				self.CloseConfiguration(maprsitexml)
				self.addOutput(self.host, '')
				self.addOutput(self.host, 'else')
				self.addOutput(self.host, '   echo "NOT created maprsitexmlcreate is 0" &gt;&gt; %s 2&gt;&amp;1' % (loginstall) )
				self.addOutput(self.host, 'fi')
				self.addOutput(self.host, '')
#				Hadoop Configurator
				self.addOutput(self.host, 'echo "Creating %s" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg,loginstall) )
				self.addOutput(self.host, 'echo "#! /bin/bash" &gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo ". /etc/sysconfig/hadoop" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "sed -i -e \\"s/servers=.*/servers=\${HADOOP_GANGLIA_ADDRESS}:8649/\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s/period=.*/period=\${HADOOP_GANGLIA_INTERVAL}/\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s/^# dfs\./dfs./\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s/^# jvm\./jvm./\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t/etc/hadoop/conf/hadoop-metrics.properties" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "if gmond -V 2>/dev/null | grep -q \'gmond 3.1\' ; then" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "   sed -i -e \'s/^#\\(dfs.*GangliaContext31\\)/\\1/\' \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \'s/^#\\(jvm.*GangliaContext31\\)/\\1/\' \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "     /etc/hadoop/conf/hadoop-metrics.properties" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "else" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "sed -i -e \'s/^#\\(dfs.*GangliaContext\$\\)/\\1/\' \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \'s/^#\\(jvm.*GangliaContext\$\\)/\\1/\' \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "     /etc/hadoop/conf/hadoop-metrics.properties" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "fi" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "sed -e "s#@HADOOP_NAMENODE_HEAP@#\${HADOOP_NAMENODE_HEAP}#" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "&lt; /etc/hadoop/conf/hadoop-env.sh.template > /etc/hadoop/conf/hadoop-env.sh" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "sed -e "s#@HADOOP_CONF_DIR@#\${HADOOP_CONF_DIR}#" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_NAMENODE@#\${HADOOP_NAMENODE}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_NAMEPORT@#\${HADOOP_NAMEPORT}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_SCRATCH@#\${HADOOP_SCRATCH}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_UMASK@#\${HADOOP_UMASK}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_LOG@#\${HADOOP_LOG}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "&lt; /etc/hadoop/conf/core-site.xml.template > /etc/hadoop/conf/core-site.xml" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "sed -e \\"s#@HADOOP_CONF_DIR@#\${HADOOP_CONF_DIR}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_DATADIR@#\${HADOOP_DATADIR}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_DATA@#\${HADOOP_DATA}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_DATANODE_BLOCKSIZE@#\${HADOOP_DATANODE_BLOCKSIZE}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_REPLICATION_DEFAULT@#\${HADOOP_REPLICATION_DEFAULT}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_REPLICATION_MIN@#\${HADOOP_REPLICATION_MIN}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_REPLICATION_MAX@#\${HADOOP_REPLICATION_MAX}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_CHECKPOINT_DIRS@#\${HADOOP_CHECKPOINT_DIRS}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_NAMENODE_NAME_DIR@#\${HADOOP_NAMENODE_NAME_DIR}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_PRIMARY_HTTP_ADDRESS@#\${HADOOP_PRIMARY_HTTP_ADDRESS}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_SECONDARY_HTTP_ADDRESS@#\${HADOOP_SECONDARY_HTTP_ADDRESS}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_CHECKPOINT_PERIOD@#\${HADOOP_CHECKPOINT_PERIOD}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_RACKAWARE_SCRIPT@#\${HADOOP_RACK_AWARENESS_SCRIPT}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t&lt; /etc/hadoop/conf/hdfs-site.xml.template > /etc/hadoop/conf/hdfs-site.xml" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "sed -e \\"s#@HADOOP_CONF_DIR@#\${HADOOP_CONF_DIR}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_TRACKER@#\${HADOOP_NAMENODE}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t-e \\"s#@HADOOP_TRACKERPORT@#\${HADOOP_NAMEPORT}#\\" \\\\" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "\t&lt; /etc/hadoop/conf/mapred-site.xml.template > /etc/hadoop/conf/mapred-site.xml" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "if [ \\"\$HADOOP_UPDATE_FSTAB\\" == \\"1\\" ] ; then" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "   if [ ! -e /usr/bin/hdfs ] ; then" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "      echo \\"Not updating fstab because /usr/bin/hdfs not found.  Is hadoop-hdfs installed?\\"" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "   fi" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "   mkdir -p /mnt/hadoop" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "   if grep -q \'^hdfs#\' /etc/fstab ; then" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "      sed -i -e \\"s;^hdfs#.*;hadoop-fuse-dfs# /mnt/hadoop fuse server=\${HADOOP_NAMENODE},port=\${HADOOP_NAMEPORT},rdbuffer=131072,allow_other 0 0;\\" /etc/fstab" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "   else" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "      if grep -q \'^hadoop-fuse-dfs#\' /etc/fstab ; then" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "         sed -i -e \\"s;^hadoop-fuse-dfs#.*;hadoop-fuse-dfs# /mnt/hadoop fuse server=\${HADOOP_NAMENODE},port=\${HADOOP_NAMEPORT},rdbuffer=131072,allow_other 0 0;\\" /etc/fstab" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "      else" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "         echo \\"hadoop-fuse-dfs# /mnt/hadoop fuse server=\${HADOOP_NAMENODE},port=\${HADOOP_NAMEPORT},rdbuffer=131072,allow_other 0 0\\" &gt;&gt; /etc/fstab" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "      fi" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "   fi" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "fi" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, 'echo "" &gt;&gt; %s 2&gt;&amp;1' % (hadoopconfg) )
				self.addOutput(self.host, '/bin/chmod 755 %s' % (hadoopconfg) )
				self.addOutput(self.host, '')

		self.endOutput(padChar='')

