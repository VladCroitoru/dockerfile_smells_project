FROM library/jenkins:2.32.1

MAINTAINER piotr.figlarek@gmail.com

USER root

# Buildroot requirements and some handy tools used during software compilation, testing, etc.
RUN apt-get update && apt-get install -y sudo sed make binutils build-essential gcc g++ bash patch \
    gzip bzip2 perl tar cpio python unzip rsync wget cvs git mercurial subversion bc graphviz \
    python-pip python-matplotlib doxygen cmake git ruby vim locales file curl

# Upgrade pip version
RUN pip install -I --upgrade pip

# Sphinx documentation generator
RUN pip install -U Sphinx sphinxcontrib-plantuml

# C++ lint
RUN pip install -U cpplint 

# allow to use sudo in the future
RUN rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

# default terminal
ENV TERM vt100

# set LOCALE to UTF8
## uncomment chosen locale to enable it's generation
RUN sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
## generate chosen locale
RUN locale-gen en_US.UTF-8
## set system-wide locale settings
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US
ENV LC_ALL en_US.UTF-8
# verify modified configuration
RUN dpkg-reconfigure --frontend noninteractive locales

# repo command (from Android), see https://source.android.com/source/using-repo.html
RUN curl https://storage.googleapis.com/git-repo-downloads/repo > /bin/repo
RUN chmod a+x /bin/repo

USER jenkins
