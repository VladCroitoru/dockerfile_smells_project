FROM ubuntu:14.10
MAINTAINER Aleksander Marchenko, maappdev@gmail.name

ENV workspace /opt/workspace
RUN mkdir -p $workspace > /dev/null

ENV user nodesrv
RUN useradd -ms /bin/bash $user && \
    chown $user $workspace

WORKDIR $workspace

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    libssl-dev \
    gcc \
    git \
    g++ \
    make \
    python2.7 \
    ssh \
    wget \
    zsh \
    nginx \
    && apt-get autoremove \
    && apt-get clean \

# Config python
ENV python_path  /usr/bin/python2.7

RUN ln -sf $python_path /usr/bin/python > /dev/null

# NodeJS version
ENV node_ver 0.10.33 
RUN cd $workspace && \
    wget http://nodejs.org/dist/v$node_ver/node-v$node_ver.tar.gz && \
    tar vfx $workspace/node* && \
    rm node*.gz && \
    cd node* 

RUN cd $workspace/node* && \
    ./configure && \
    make -j8 && \
    make install

RUN npm install -g bower && \
    npm install -g gulp && \
    npm install -g forever && \
    npm install -g grunt-cli && \
    npm install -g yo && \
    npm install -g generator-angular

# USER $user
#oh myzsh install
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git /home/$user/.oh-my-zsh && \
    cp /home/$user/.oh-my-zsh/templates/zshrc.zsh-template /home/$user/.zshrc && \
    chown $user /home/$user/.oh-my-zsh && \
    chown $user /home/$user/.zshrc && \
    chsh -s /bin/zsh

EXPOSE  9000

CMD /bin/zsh

