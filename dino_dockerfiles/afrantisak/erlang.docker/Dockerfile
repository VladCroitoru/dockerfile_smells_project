FROM ubuntu:14.10
MAINTAINER Aaron Frantisak <afrantisak@gmail.com

RUN apt-get update
RUN apt-get install -y curl git build-essential libncurses5-dev openssl libssl-dev m4

# install kerl using curl (don't confuse the two)
RUN curl -O https://raw.githubusercontent.com/spawngrid/kerl/master/kerl
RUN chmod +x kerl
RUN sudo mv kerl /usr/bin
RUN kerl update releases

# install erlang using kerl
RUN KERL_CONFIGURE_OPTIONS=--enable-hipe kerl build 17.3 17.3.hipe
RUN kerl install 17.3.hipe /usr/lib/erlang.kerl.17.3.hipe
RUN kerl cleanup all
RUN rm -f /.kerl/archives/*.tar.gz

# configure it as the default erlang
RUN ln -s /usr/lib/erlang.kerl.17.3.hipe /usr/lib/erlang
ENV PATH /usr/lib/erlang/bin:$PATH

# install awscli
RUN apt-get install -y python-pip groff
RUN pip install awscli

# install mg just in case
RUN apt-get install -y mg
 
