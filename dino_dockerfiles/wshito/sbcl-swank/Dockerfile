FROM wshito/roswell-base

MAINTAINER W.Shito (@waterloo_jp)

RUN mkdir /root/lisp && cd /root/lisp

# OpenSSL is referred by many packages so is included.
RUN apk --no-cache --update add openssl

COPY pre-load.lisp /root/lisp/pre-load.lisp
COPY swank.lisp /root/lisp/swank.lisp

# Load some libraries into the docker image.
RUN ros run -- --load /root/lisp/pre-load.lisp

# Run SBCL and start the swank server
CMD ["ros", "run", "--", "--load", "/root/lisp/swank.lisp"]
