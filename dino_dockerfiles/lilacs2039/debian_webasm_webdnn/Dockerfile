FROM apiaryio/emcc

MAINTAINER lilacs

USER root

RUN mv /bin/sh /bin/sh_tmp && ln -s /bin/bash /bin/sh

RUN apt-get update && \
	apt-get install -y git wget

RUN git clone --depth 1 https://github.com/pyenv/pyenv /root/.pyenv && \
	echo 'eval "$(pyenv init -)"' >> /root/.bashrc && \
	echo 'PYENV_ROOT="$HOME/.pyenv"' >> /root/.bashrc && \
	echo 'PATH="$PYENV_ROOT/bin:$PATH"' >> /root/.bashrc

# anaconda�����C����python�ɐݒ��B
# activate��pyenv��anaconda�Ńo�b�e�B���O�����̂ŁApath�ɖ������Ă����B
RUN source /root/.bashrc && \
	pyenv install anaconda3-5.0.1 && \
	pyenv rehash && \
	pyenv global anaconda3-5.0.1 && \
	echo 'export PATH="$PYENV_ROOT/versions/anaconda3-5.0.1/bin/:$PATH"' >> /root/.bashrc && \
	source /root/.bashrc && \
	conda update conda && \
	conda create -n py36 python=3.6 && \
	pyenv local anaconda3-5.0.1/envs/py36


RUN source /root/.bashrc && \
	git clone --depth 1 https://github.com/mil-tokyo/webdnn /webdnn && \
	cd /webdnn && python3 setup.py install

RUN source /root/.bashrc && \
	pip install chainer keras tensorflow


RUN cd / && \
	wget http://bitbucket.org/eigen/eigen/get/3.3.3.tar.bz2 && \
	tar jxf 3.3.3.tar.bz2 && \
	rm 3.3.3.tar.bz2 && \
	echo 'export CPLUS_INCLUDE_PATH=/eigen-eigen-67e894c6cd8f' >> /root/.bashrc && \
	cd /usr/local/bin && \
	ln emcc emcc.py

RUN rm /bin/sh && mv /bin/sh_tmp /bin/sh
