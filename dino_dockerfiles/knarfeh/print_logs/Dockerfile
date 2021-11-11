FROM ubuntu:14.04
MAINTAINER knarfeh@outlook.com

# Update
RUN apt-get update && apt-get install -y \
        python-dev \
        libpq-dev \
        libsasl2-dev \
        libldap2-dev \
        libssl-dev \
        libffi-dev \
        curl

RUN curl https://bootstrap.pypa.io/get-pip.py | python

RUN pip install -U pip
RUN pip install supervisor supervisor-stdout && \
    rm -rf /root/.cache/pip/


COPY . /print_logs
WORKDIR /print_logs
RUN ln -s /print_logs/supervisord.conf /etc/supervisord.conf
RUN mkdir /var/log/mathilde
RUN chmod +w /var/log/mathilde
RUN chmod +x /print_logs/print_log.sh

CMD ["/print_logs/print_log.sh"]
