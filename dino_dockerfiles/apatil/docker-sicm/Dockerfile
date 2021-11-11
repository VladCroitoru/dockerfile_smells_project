FROM ubuntu:14.04

RUN apt-get update -y	 
RUN apt-get install -y emacs24 paredit-el wget xutils-dev libx11-dev libncurses5-dev

# Get MIT scheme from a third-party deb and install it
RUN wget http://www-users.cselabs.umn.edu/classes/Fall-2010/csci1901/mit-scheme-x64_9.0.1-1_amd64.deb
RUN dpkg -i mit-scheme-x64_9.0.1-1_amd64.deb
RUN ln -s /usr/local/bin/mit-scheme-x86-64 /usr/local/bin/mit-scheme

# Get scmutils and install it
RUN wget http://groups.csail.mit.edu/mac/users/gjs/6946/scmutils-tarballs/scmutils-20140302-x86-64-gnu-linux.tar.gz
RUN cd /usr/local/lib/mit-scheme-x86-64; tar -xvf /scmutils-20140302-x86-64-gnu-linux.tar.gz

# Load scmutils and save a 'band' for quick loading in future
RUN cd /usr/local/lib/mit-scheme-x86-64/scmutils/src; mit-scheme --eval "(begin (load \"load.scm\") (disk-save \"sicm.band\" \"SICM\") (%exit))"

# Add the Emacs init.el file that provides a function that starts mit-scheme in a repl with scmutils loaded.
ADD init.el /.emacs.d/init.el

# Mark the mount point for emacs' working directory
VOLUME ["/work"]

# Add a startup file to /work that tells you to bind mount
ADD start.scm /work/start.scm

CMD cd /work;emacs start.scm