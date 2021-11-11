FROM ubuntu:20.04

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8

ENV HOME /root
ENV DEPLOY_DIR ${HOME}/cliphype

RUN apt update

# Set locale
RUN apt install -y locales
RUN sed -i -e "s/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/" /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install packages
RUN apt install -y mysql-server mysql-client redis libmysqlclient-dev tmux vim git

# Install Python3.8
RUN apt install -y wget build-essential zlib1g-dev libssl-dev libsqlite3-dev
RUN apt-get install --no-install-recommends -y \
    python3.8 python3-pip python3.8-dev

# Install requirements
WORKDIR ${DEPLOY_DIR}
ADD requirements.txt ${DEPLOY_DIR}
RUN pip install -U pip
RUN pip install -r requirements.txt

# Execute commands when container started
COPY ./docker_start.sh ${DEPLOY_DIR}
RUN chmod +x docker_start.sh
CMD ["./docker_start.sh"]
