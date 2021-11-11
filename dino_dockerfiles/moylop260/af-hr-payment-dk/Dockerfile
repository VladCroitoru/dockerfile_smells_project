FROM ubuntu:xenial-20180123
ENV DEBIAN_FRONTEND="noninteractive"

# Configure locales to avoid coding errors
RUN apt-get update && apt-get install locales \
   && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
   && locale-gen en_US.UTF-8 \
   && dpkg-reconfigure locales \
   && update-locale LANG=en_US.UTF-8

ENV LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" LC_ALL="en_US.UTF-8" PYTHONIOENCODING="UTF-8" 

COPY files/pip_requirements.txt files/apk_requirements.txt /tmp/

RUN apt-get update \
  && apt-get install -y wget sudo \
  && echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' >> /etc/apt/sources.list.d/pgdg.list \
  && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - \
  && apt-get update \
  && apt-get install -y postgresql-10 postgresql-server-dev-10 \
  postgresql-client-10 postgresql-client-common postgresql-common postgresql-contrib \
  postgresql-plpython-10 \
  tmux pgbadger
RUN apt-get install -y $(grep -vE "^\s*#" /tmp/apk_requirements.txt | tr "\n" " ") \
    && npm install -g less clean-css \
    && wget https://downloads.wkhtmltopdf.org/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb -O /tmp/wk.deb \
    && dpkg -i /tmp/wk.deb; apt-get install -yf && dpkg -i /tmp/wk.deb
RUN pip install -U pip \
  && python2.7 -m pip install -Ur /tmp/pip_requirements.txt \
  && python2.7 -m pip install -U gevent==1.0.2 psycogreen==1.0 pstats_print2list
RUN useradd -d "/home/odoo" -m -s "/bin/bash" "odoo" \
  && su - odoo -c "git config --global user.name odoo" \
  && su - odoo -c "git config --global user.email odoo@email.com" \
  && /etc/init.d/postgresql start 10 \
  && su - postgres -c "createuser -s odoo"
