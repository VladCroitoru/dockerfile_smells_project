FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN git clone https://github.com/torch/distro.git ~/torch
RUN cd ~/torch && bash install-deps
RUN cd ~/torch && ./install.sh

ENV LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'
ENV LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'
ENV PATH=/root/torch/install/bin:$PATH
ENV LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH
ENV DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH

RUN luarocks install torch
RUN luarocks install nn
RUN luarocks install image
RUN luarocks install lua-cjson
RUN luarocks install https://raw.githubusercontent.com/qassemoquab/stnbhwd/master/stnbhwd-scm-1.rockspec
RUN luarocks install https://raw.githubusercontent.com/jcjohnson/torch-rnn/master/torch-rnn-scm-1.rockspec

RUN luarocks install cutorch
RUN luarocks install cunn
RUN luarocks install cudnn

# Install densecap
RUN luarocks install luasocket
RUN apt-get install -y --no-install-recommends python-pip python-dev wget

RUN git clone https://github.com/unnonouno/densecap.git ~/densecap
WORKDIR /root/densecap

RUN sh -ex scripts/download_pretrained_model.sh
RUN pip install -r webcam/requirements.txt

CMD th webcam/daemon.lua & python webcam/server.py
