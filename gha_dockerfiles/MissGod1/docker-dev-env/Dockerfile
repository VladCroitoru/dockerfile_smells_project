FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

ARG NAME
ARG UID
ARG PASSWORD

# Add aliyun apt-get
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" > /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list

# Install application
RUN apt-get update
RUN apt-get remove -y openssh-server --purge
RUN apt-get install -y openssh-server wget git sudo


# Configure ssh
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/g' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config
RUN sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords no/g' /etc/ssh/sshd_config
RUN mkdir -p /run/sshd

# add user
RUN useradd -m -s /bin/bash -u $UID $NAME
RUN usermod -aG sudo $NAME
RUN echo "$NAME:$PASSWORD" | chpasswd
# RUN service ssh start
# RUN echo "$NAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
#Configure jupyter
USER $NAME

# Add aliyun pipy
RUN pip3 install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple/
RUN pip3 config set install.trusted-host mirrors.aliyun.com

# Install python module
RUN pip3 install transformers tqdm wandb

WORKDIR /workspace

USER root
RUN rm -rf /usr/bin/python3 /usr/bin/python3-config
RUN ln -s /opt/conda/bin/python3 /usr/bin/python3
RUN ln -s /opt/conda/bin/python3-config /usr/bin/python3-config

ENTRYPOINT ["/usr/sbin/sshd", "-D"]