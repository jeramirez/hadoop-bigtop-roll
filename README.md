hadoop-bigtop-roll
==================

Download and Compile Roll
-------------------------

```shell
git clone https://github.com/jeramirez/hadoop-bigtop-roll.git
cd hadoop-bigtop-roll
wget https://archive.apache.org/dist/bigtop/bigtop-1.5.0/repos/centos-7/bigtop.repo
make roll
```

Improve roll documentation by recompiling
-----------------------------------------
```shell
yum -y install RPMS/x86_64/rocks-command-bigtop-7.0-0.x86_64.rpm
make roll
```

Install Roll on a Running System
--------------------------------
```shell
rocks add roll hadoop-bigtop-1.5.0-0.x86_64.disk1.iso
rocks enable roll hadoop-bigtop
cd /export/rocks/install
rocks create distro
rocks run roll hadoop-bigtop | bash
rocks add attr BIGTOP_HadoopNameNode value=compute-0-0
rocks add attr BIGTOP_HadoopSecondaryNameNode value=compute-0-1
rocks add attr BIGTOP_HadoopDataDir value="file:///hadoop"
rocks add attr BIGTOP_HadoopData value="file:///hadoop/data"
rocks add attr BIGTOP_HadoopCheckPointDirs value="file:///hadoop"
rocks add attr BIGTOP_HadoopNamenodeNameDir value="file:///hadoop/dfs/name"
rocks add attr BIGTOP_HadoopCheckPointPeriod value=600
rocks add attr BIGTOP_HadoopUpdateFstab value=1
rocks add attr BIGTOP_HadoopReplicationDefault value=2
yum clean metadata
yum -y reinstall rocks-command-bigtop
yum -y install roll-hadoop-bigtop-usersguide
#Regenerate cluster home page after adding a new roll on the fly
/opt/rocks/bin/gen-home-page > /var/www/html/index.html
```
