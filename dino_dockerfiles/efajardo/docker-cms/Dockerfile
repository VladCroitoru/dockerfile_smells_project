FROM opensciencegrid/osg-wn:3.3-el6

LABEL name="CMS Worker Node on EL 6"
LABEL build-date="20170228"
LABEL maintainer="Brian Bockelman"

# Required
# --------
# - cmsRun fails without stdint.h (from glibc-headers)
#   Tested CMSSW_7_4_5_patch1
#
# Other
# -----
# - ETF calls /usr/bin/lsb_release (from redhat-lsb-core)
# - sssd-client for LDAP lookups through the host
# - SAM tests expect cvmfs utilities
# - gcc is required by GLOW jobs (builds matplotlib)
# - 7 Feb 2018: libaio was added to enable the Oracle client, needed for T0 jobs.
#
# CMSSW dependencies
# ------------------
# Required software is listed under slc6_amd64_platformSeeds at
# http://cmsrep.cern.ch/cgi-bin/cmspkg/driver/cms/slc6_amd64_gcc472

RUN yum -y install cvmfs \
                   gcc \
                   glibc-headers \
                   openssh-clients \
                   openssh-server \
                   redhat-lsb-core \
                   sssd-client && \
    yum -y install glibc coreutils bash tcsh zsh perl tcl tk readline openssl \
                   ncurses e2fsprogs krb5-libs freetype compat-readline5 \
                   ncurses-libs perl-libs perl-ExtUtils-Embed fontconfig \
                   compat-libstdc++-33 libidn libX11 libXmu libSM libICE \
                   libXcursor libXext libXrandr libXft mesa-libGLU mesa-libGL \
                   e2fsprogs-libs libXi libXinerama libXft libXrender libXpm \
                   libcom_err libaio libgfortran && \
    yum clean all

# Various directories needed for bind mounts (as overlayfs is not available on RHEL6)

RUN mkdir -p /hdfs \
             /mnt/hadoop \
             /hadoop \
             /cms \
             /etc/cvmfs/SITECONF \
             /lfs_roots \
             /storage

