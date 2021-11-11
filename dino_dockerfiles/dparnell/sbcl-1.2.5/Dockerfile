FROM    ubuntu
MAINTAINER      Daniel Parnell <me@danielparnell.com>

RUN apt-get update
RUN apt-get install -y sbcl curl rlwrap build-essential time
RUN cd /tmp && curl -O http://iweb.dl.sourceforge.net/project/sbcl/sbcl/1.2.5/sbcl-1.2.5-source.tar.bz2 && tar jxvf sbcl-1.2.5-source.tar.bz2 && cd /tmp/sbcl-1.2.5 && sh ./make.sh  && sh ./install.sh && rm -rf /tmp/sbcl*
RUN curl -O http://beta.quicklisp.org/quicklisp.lisp && echo "(load \"quicklisp.lisp\") (quicklisp-quickstart:install :path \"/opt/quicklisp\") (ql::without-prompting (ql:add-to-init-file))" | sbcl && cp $HOME/.sbclrc /etc/sbclrc
