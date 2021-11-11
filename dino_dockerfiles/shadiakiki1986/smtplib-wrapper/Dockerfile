FROM ubuntu

# prepare apt-get
RUN if [ ! -z "$USE_APT_CACHER" ]; then echo "Acquire::http::Proxy \"http://172.17.0.2:3142\";" | tee /etc/apt/apt.conf.d/01proxy; fi
RUN apt-get -qq update > /dev/null

# install postfix
RUN apt-get -qq -y install mailutils  > /dev/null
RUN apt-get -qq -y install postfix rsyslog libsasl2-2 ca-certificates libsasl2-modules > /dev/null

# for testing smtplib-wrapper
RUN apt-get -qq -y install libyaml-dev > /dev/null

# for inspection
RUN apt-get -qq -y install vim-tiny screen tree > /dev/null
RUN ln -s /usr/bin/vim.tiny /usr/bin/vim

# python
RUN apt-get -qq -y install python-pip python-virtualenv python-dev

# templating
RUN apt-get -qq -y install gettext

# complete postfix config
RUN ln -s /etc/hostname /etc/mailname

# prepare
RUN pip install pew
RUN pew new -d ENV2
RUN pew in ENV2 pip install PyYaml

# Run
COPY . /code
WORKDIR /code
ENTRYPOINT ["bash","entry.sh"]
