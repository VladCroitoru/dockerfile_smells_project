#############
# http://blog.livedoor.jp/s-koide/archives/2287418.html
#############

FROM ubuntu:15.04
MAINTAINER moremagic <itoumagic@gmail.com>

RUN apt-get update && apt-get install -y vim openssh-server openssh-client
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config


RUN apt-get install -y curl emacs cl-swank slim sbcl

RUN curl -O http://beta.quicklisp.org/quicklisp.lisp
RUN curl -O http://beta.quicklisp.org/quicklisp.lisp.asc
RUN gpg --verify quicklisp.lisp.asc quicklisp.lisp; return 0

ADD setup.lisp /tmp/
RUN sbcl --disable-debugger --load quicklisp.lisp --script /tmp/setup.lisp; return 0
ADD .sbclrc /root/
RUN echo \(require :sb-aclrepl\) >> /root/.sbclrc

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
