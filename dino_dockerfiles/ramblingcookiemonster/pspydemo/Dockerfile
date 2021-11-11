FROM centos:latest
MAINTAINER Warren Frame

RUN yum -y --setopt=tsflags=nodocs update

# Grab some PowerShell and Python goodies.  Yep, overkill : )
RUN yum -y groupinstall development && \
    yum -y install https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-alpha.9/powershell-6.0.0_alpha.9-1.el7.centos.x86_64.rpm \
                   https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y install python35u-3.5.2 \
                   python35u-pip \
                   python35u-devel

# We're not animals, use a venv
RUN mkdir /source/environments -p && \
    pyvenv-3.5 /source/environments/PSPyExample && \
    source /source/environments/PSPyExample/bin/activate && \
    pip install ldap3

# Wrap up
RUN yum clean all
WORKDIR /source/environments/PSPyExample
CMD [ "/bin/bash"]
