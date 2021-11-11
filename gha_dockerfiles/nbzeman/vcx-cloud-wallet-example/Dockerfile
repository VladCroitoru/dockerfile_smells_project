FROM ubuntu:18.04

#### Needed Packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends\
        add-apt-key \
        apt-transport-https \
        dirmngr \
        ca-certificates  \
        curl \
         unzip \
        software-properties-common \
        vim \
        supervisor \
        netcat \
        nginx \
        libpq-dev \
        gcc \
        make \
        g++ \
        jq \
        python3-pip \
        pwgen \
        mysql-client

#### Needed Repos
RUN echo "deb https://repo.sovrin.org/sdk/deb bionic stable" > /etc/apt/sources.list.d/sovrin.list && \
    cnt=0 ;\
    while ! apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 97080EBDA5D46DAF 2>&1; do \
        echo "Waiting 1 second before retrying gpg key download.($cnt/10)" ;\
        sleep 1 ;\
        cnt=$((cnt + 1)); \
        if [ $cnt -ge 10 ] ; then \
            echo "Could not add gpg key. Aborting" ;\
            exit 1 ;\
        fi ;\
    done

# RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 97080EBDA5D46DAF

#### Install Libindy/Sovtoken and Dependencies
COPY install/* /root/install/
COPY config/* /root/config/
COPY data/* /root/data/
COPY server/* /root/server/
COPY web/* /var/www/html/


EXPOSE 3000


# Add Keys and Update apt-get Libraries:
WORKDIR /root/install
RUN apt-get update && \
    apt-get install -y \
      libsodium23 \
      libzmq5 \
      libssl1.0.0 
      
RUN dpkg -i libindy_1.15*.deb
RUN dpkg -i libsovtoken_1.0.5_amd64.deb
RUN dpkg -i libmysqlstorage_0.1.1131_amd64.deb
RUN dpkg -i libvcx_0.10*
RUN apt-get install -f

# NodeJS 10.x install
RUN . /etc/os-release && \
    curl -f -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
    echo "deb https://deb.nodesource.com/node_10.x ${UBUNTU_CODENAME} main" > /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && \
    apt-get install -y nodejs --no-install-recommends
# 

# Install Ngrok
RUN curl -O -s https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && \
    unzip ngrok-stable-linux-amd64.zip && \
    cp ngrok /usr/local/bin/.

#### Cleanup
# clean up apt lists
RUN rm -rf /var/lib/apt/lists/*

COPY config/supervisord.conf /etc/supervisord.conf
#### Entrypoint
ENTRYPOINT [ "/root/install/install-vcx-portal.sh" ]
