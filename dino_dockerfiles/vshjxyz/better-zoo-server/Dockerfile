FROM debian:stretch

WORKDIR /usr/src

RUN apt-get update
RUN apt-get install wget sed build-essential -y

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 7.7.4

RUN wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.7/install.sh | bash

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# install node and npm
RUN source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION

RUN echo "source ${NVM_DIR}/nvm.sh" > $HOME/.bashrc && \
    source $HOME/.bashrc

# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

COPY . /src
COPY .nvmrc /src/.nvmrc

WORKDIR /src

RUN npm i -g yarn
RUN yarn --frozen-lockfile

WORKDIR /usr/src
RUN wget "http://downloads.sourceforge.net/project/mad/libmad/0.15.1b/libmad-0.15.1b.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fmad%2Ffiles%2Flibmad%2F0.15.1b%2F&ts=1476010202&use_mirror=ufpr" -O libmad-0.15.1b.tar.gz
RUN tar zxf libmad-0.15.1b.tar.gz

WORKDIR /usr/src/libmad-0.15.1b
# The following line is a patch to fix the build with newer GCC's that don't have the -fforce-mem option
RUN sed -i '/-fforce-mem/d' configure
RUN ./configure --prefix=/usr/libmad-0.15.1b --enable-static --disable-shared
RUN make
RUN make install

WORKDIR /usr/src
RUN wget "https://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz" -O lame-3.99.5.tar.gz
RUN tar zxf lame-3.99.5.tar.gz

WORKDIR /usr/src/lame-3.99.5
RUN ./configure --prefix=/usr/lame-3.99.5 --enable-static --disable-shared
RUN make
RUN make install

WORKDIR /usr/src
RUN wget "https://downloads.sourceforge.net/project/sox/sox/14.4.2/sox-14.4.2.tar.bz2?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fsox%2Ffiles%2Fsox%2F14.4.2%2F&ts=1476009578&use_mirror=ufpr" -O sox-14.4.2.tar.bz2
RUN tar jxf sox-14.4.2.tar.bz2

WORKDIR /usr/src/sox-14.4.2

RUN CPPFLAGS="-I/usr/libmad-0.15.1b/include -I/usr/lame-3.99.5/include " \
    LDFLAGS="-L/usr/libmad-0.15.1b/lib -L/usr/lame-3.99.5/lib -L/usr/libgsm-1.0.10/lib" \
    ./configure --prefix=/usr/sox-14.4.2 --disable-shared --enable-static --with-lame
RUN make
RUN make install

RUN ln -s /usr/sox-14.4.2/bin/sox /usr/bin

RUN apt-get remove --purge wget build-essential -y
RUN apt-get clean

WORKDIR /src

CMD [ "yarn", "start" ]
