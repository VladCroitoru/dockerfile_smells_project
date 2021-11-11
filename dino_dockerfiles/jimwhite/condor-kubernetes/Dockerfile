FROM centos:centos6
MAINTAINER Jim White <mailto:jimwhite@uw.edu>

USER root
WORKDIR /root

# If you want to submit when running inside this container, 
# then you'll need a user other than 'root' because Condor requires that.
# The directories that Condor daemons talk to need to be accessible.
RUN adduser --comment "Condor submitter inside Docker" --create-home --shell /bin/bash submit && \
	chmod go+rx /home/submit

# Here I only install tools which we must have:
RUN yum -y install yum-utils wget which tar file && \
	wget https://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor && \
	rpm --import RPM-GPG-KEY-HTCondor && \
	yum-config-manager --add-repo https://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel6.repo && \
	yum -y install condor.x86_64 condor-debuginfo condor-python && \
	yum clean all

COPY userfiles /root
COPY condor_config.local /etc/condor/condor_config.local

# Expose the standard Condor port and our shared CCB port.
EXPOSE 9618 9886

CMD [ "./start-condor.sh" ]
