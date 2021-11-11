FROM cryoflamer/nynja_docker

#example for build:
# $ docker build -t roster_docker --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" --build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)" .

ARG ssh_prv_key
ARG ssh_pub_key

USER ubuntu
ENV HOME /home/ubuntu

# Authorize SSH Host
RUN mkdir -p /home/ubuntu/.ssh && \
    chmod 0700 /home/ubuntu/.ssh && \
    ssh-keyscan github.com > /home/ubuntu/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > ~/.ssh/id_rsa && \
    echo "$ssh_pub_key" > ~/.ssh/id_rsa.pub && \
    chmod 600 ~/.ssh/id_rsa && \
    chmod 644 ~/.ssh/id_rsa.pub

WORKDIR $HOME
RUN git clone git@github.com:NYNJA-MC/server.git
WORKDIR $HOME/server
RUN mad dep com pla

#TODO run sevice from command line
#CMD make start