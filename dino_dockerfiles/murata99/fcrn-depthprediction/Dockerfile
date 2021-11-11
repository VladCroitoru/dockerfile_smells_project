FROM buildpack-deps:xenial

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH

RUN apt-get update && apt-get install -y git python3-tk tk-dev
RUN git clone git://github.com/yyuu/pyenv.git $HOME/.pyenv
RUN eval "$(pyenv init -)" && pyenv install 3.5.3 && pyenv global 3.5.3
RUN eval "$(pyenv init -)" && pip install numpy tensorflow==1.2.1 pillow matplotlib

RUN echo 'PATH="$PATH:~/.pyenv/bin"' >> $HOME/.bashrc
RUN echo 'eval "$(pyenv init -)"'    >> $HOME/.bashrc

# COPY . /FCRN-DepthPrediction
RUN cd / && git clone https://github.com/iro-cp/FCRN-DepthPrediction.git

RUN cd /FCRN-DepthPrediction && git checkout e47e593026c80530f7c387c4feca24f88c1618a2
RUN cd /FCRN-DepthPrediction && curl -L -O http://campar.in.tum.de/files/rupprecht/depthpred/NYU_ResNet-UpProj.npy

CMD ["/bin/bash"]
