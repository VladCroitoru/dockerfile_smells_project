FROM crisbal/torch-rnn:base

RUN apt-get -y update
RUN apt-get -y install wget

RUN luarocks install hdf5

RUN git clone https://github.com/torch/senna.git
WORKDIR senna
RUN wget http://ml.nec-labs.com/senna/senna-v3.0.tgz
RUN tar -zxvf senna-v3.0.tgz
RUN luarocks make rocks/senna-scm-1.rockspec

RUN luarocks install https://raw.githubusercontent.com/benglard/htmlua/master/htmlua-scm-1.rockspec
RUN luarocks install https://raw.githubusercontent.com/benglard/waffle/master/waffle-scm-1.rockspec

RUN luarocks install penlight
RUN luarocks install rnn
RUN luarocks install torch