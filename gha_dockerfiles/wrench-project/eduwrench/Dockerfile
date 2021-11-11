FROM wrenchproject/wrench:unstable

USER root

# install Node and Gatsby client
RUN apt-get update
RUN apt-get upgrade ca-certificates -y
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt install -y nodejs
RUN npm install -g gatsby-cli --unsafe-perm

USER wrench
WORKDIR /home/wrench/

# download eduWRENCH repository
RUN git clone https://github.com/wrench-project/eduwrench.git
RUN cd eduwrench && git checkout

# set volume for data server
RUN mkdir /home/wrench/eduwrench/data_server
VOLUME /home/wrench/eduwrench/data_server

# run build script
WORKDIR /home/wrench/eduwrench
RUN mkdir db
RUN bash build.sh -j2

# run applications
WORKDIR /home/wrench/eduwrench
USER root
COPY ./docker.sh .
RUN chown wrench:users docker.sh

USER wrench
CMD ./docker.sh
