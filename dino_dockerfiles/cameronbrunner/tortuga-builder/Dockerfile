FROM centos:7

# Add repos for Puppet and Puppet Development Kit
# Install Centos software collections repo
# Install Python 3.6 and other build tools
RUN rpm -ivh https://yum.puppetlabs.com/puppet6-release-el-7.noarch.rpm \
    && rpm -ivh https://yum.puppetlabs.com/puppet-tools-release-el-7.noarch.rpm \
    && yum install -y centos-release-scl \
    && yum update -y \
    && yum install -y \
        bzip2 \
        git \
        rh-python36 \
        rsync \
        unzip \
        pdk \
        puppet-agent \
    && . /opt/rh/rh-python36/enable \
    && pip install tox \
    && yum clean all

# Make sure the environment is set up right
ADD scripts/entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]

# Support running builds like so:
# docker run -it --rm -v `pwd`:/tortuga univa/tortuga-builder
WORKDIR /tortuga
CMD [ "bash", "-c", "pip install -r requirements.txt && paver clean && paver build" ]
