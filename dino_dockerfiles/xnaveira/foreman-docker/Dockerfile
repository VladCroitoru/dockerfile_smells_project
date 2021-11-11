FROM centos:centos6
RUN yum -y install http://yum.theforeman.org/releases/1.6/el6/x86_64/foreman-release.rpm
RUN yum -y install http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
RUN yum -y install foreman-installer mod_passenger
EXPOSE 80
EXPOSE 8140
EXPOSE 8443
CMD foreman-installer --foreman-locations-enabled --enable-foreman-compute-ec2 --enable-foreman-compute-gce --enable-foreman-compute-ovirt --enable-foreman-compute-vmware --enable-puppet --puppet-server-envs-dir=/etc/puppet/environments --puppet-server-environments=test && tail -f /var/log/foreman/production.log
