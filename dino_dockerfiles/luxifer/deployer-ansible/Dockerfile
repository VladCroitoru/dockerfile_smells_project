FROM debian:jessie

RUN apt-get -y update && apt-get -y install git \
                openssh-client \
                locales \
                python-dev \
                python-pip \
                python-paramiko \
                python-jinja2 \
                python-httplib2 \
                python-six \
                build-essential \
                libffi-dev \
                libssl-dev \
                libyaml-dev \
        --no-install-recommends && rm -r /var/lib/apt/lists/*

ENV ANSIBLE_VERSION 2.2.1.0
RUN pip install -U pip
RUN pip install ansible==$ANSIBLE_VERSION
ADD ./requirements.txt .
RUN pip install -r requirements.txt

ADD ./exec /bin/exec
ADD ./config /root/.ssh/config
ADD ./ansible.cfg /etc/ansible/ansible.cfg
ADD ./roles /etc/ansible/roles
ADD ./hosts /etc/ansible/hosts

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
ENV TERM xterm

ENTRYPOINT ["/bin/exec"]
