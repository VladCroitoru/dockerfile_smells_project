FROM ubuntu:14.04
# does not work with 16.04 because of newer python version

MAINTAINER Bastian Lemke

ENV DEBIAN_FRONTEND noninteractive

# Enable backports repository - needed for jq 1.4
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse" >> \
    /etc/apt/sources.list

# Prerequisites
RUN apt-get update && \
    apt-get install -y \
    git \
    python3-dev \
    python3-pip \
    python-dev \
    python-pip \
    python-virtualenv \
    ruby-sass \
    nodejs \
    postfix \
    apache2 \
    libapache2-mod-wsgi \
    jq/trusty-backports \
    expect \
    rsyslog \
    npm && \
    npm install -g less && \
    ln -s /usr/bin/nodejs /usr/bin/node && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./config/rsyslog.conf /etc/rsyslog.conf

# Install mailman bundler
RUN git clone https://gitlab.com/mailman/mailman-bundler.git mailman
WORKDIR /mailman
# set deployment to production
RUN sed -i "s/^deployment =.*$/deployment = production/" buildout.cfg

# build mailman
RUN virtualenv venv && \
    . venv/bin/activate && \
    pip install zc.buildout && \
    buildout && \
    mkdir /var/log/mailman-web && \
    touch /var/log/mailman-web/mailman-web.log

# configure apache
RUN sed -i '/ *WSGIProcessGroup mailman-web$/d' /mailman/deployment/apache.conf && \
    ln -s /mailman/deployment/apache.conf /etc/apache2/sites-available/ && \
    a2dissite 000-default > /dev/null && \
    a2ensite apache > /dev/null

# Disable SSLMidleware
RUN sed -i 's/^\(.*hyperkitty.middleware.SSLRedirect.*\)$/#\1/' /mailman/mailman_web/production.py

# Fix authentication (Mailman Bug?)
RUN sed -i 's/, {"SSL": True}//g' /mailman/mailman_web/urls.py
# Downgrade to compatible falcon version - see https://gitlab.com/mailman/postorius/issues/122
RUN . venv-3.4/bin/activate && pip install --upgrade falcon==0.3
# Workaround for Mailman-Client Bug - see https://gitlab.com/mailman/mailmanclient/issues/10
RUN sed -i 's/moderation_reasons=/#moderation_reasons=/' /mailman/eggs/mailmanclient-1.0.1-py2.7.egg/mailmanclient/_client.py
# Fix for wrong user activation link in Hyperkitty
RUN sed -i 's/\({{ postorius_installed }}\/\)/\1..\//' /mailman/eggs/HyperKitty-1.0.3-py2.7.egg/hyperkitty/templates/hyperkitty/fragments/send_as.html && \
    sed -i 's/\({{ postorius_installed }}\/\)/\1..\//' /mailman/eggs/HyperKitty-1.0.3-py2.7.egg/hyperkitty/templates/hyperkitty/user_profile.html

# Configure boot scripts
COPY boot /
COPY boot.d /boot.d
RUN chmod 755 /boot /boot.d/*

ENV MAILMAN3=true
ENV MAILMAN_HOME=/mailman

EXPOSE 80 8024
VOLUME /mailman/var
VOLUME /mailman/deployment
VOLUME /mail_settings

CMD /boot; rsyslogd -n
