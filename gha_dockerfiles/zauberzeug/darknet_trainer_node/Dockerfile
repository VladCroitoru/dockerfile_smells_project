FROM nvidia/cuda:11.0.3-cudnn8-devel-ubuntu20.04

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt-get install -y curl python3.8 python3-distutils python3-pip git-all vim build-essential libopencv-dev jpeginfo && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN ln -sf /usr/bin/python3.8 /usr/bin/python3 && ln -sf /usr/bin/python3.8 /usr/bin/python

# darknet
COPY conf.sh /tmp/
ARG CONFIG
WORKDIR /
RUN git clone https://github.com/zauberzeug/darknet_alexeyAB.git darknet && cd darknet && git checkout 211bb29e9988f6204a32cd38d0720d171135873d 
RUN cd darknet && /tmp/conf.sh $CONFIG && make clean && make

RUN ls
RUN curl -sSL https://gist.githubusercontent.com/b01/0a16b6645ab7921b0910603dfb85e4fb/raw/5186ea07a06eac28937fd914a9c8f9ce077a978e/download-vs-code-server.sh | bash

ENV VSCODE_SERVER=/root/.vscode-server/bin/*/server.sh

RUN $VSCODE_SERVER --install-extension ms-python.vscode-pylance \
    $VSCODE_SERVER --install-extension ms-python.python \
    $VSCODE_SERVER --install-extension himanoa.python-autopep8 \
    $VSCODE_SERVER --install-extension esbenp.prettier-vscode \
    $VSCODE_SERVER --install-extension littlefoxteam.vscode-python-test-adapter

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir "uvicorn[standard]" numpy async_generator aiofiles retry debugpy pytest-asyncio psutil icecream psutil pytest autopep8
RUN python3 -m pip install --no-cache-dir "learning-loop-node==0.4.6"

WORKDIR /app/
RUN mkdir -p /data
ADD ./app /app
ENV PYTHONPATH=/app

EXPOSE 80

CMD /app/start.sh
