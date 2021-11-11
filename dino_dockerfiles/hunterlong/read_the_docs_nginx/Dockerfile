FROM ubuntu:16.04

EXPOSE 80

# Env Vars for Github
ENV GIT_EMAIL $GIT_EMAIL
ENV GIT_NAME $GIT_NAME
ENV GIT_REPO $GIT_REPO
ENV GIT_BRANCH master
ENV GIT_USERNAME $GIT_USERNAME
ENV GIT_PERSONAL_TOKEN $GIT_PERSONAL_TOKEN
ENV DOCS_FOLDER $DOCS_FOLDER

RUN apt-get update
RUN apt-get install -y nginx python git python-setuptools
RUN easy_install pip

RUN pip install sphinx
RUN pip install sphinx_rtd_theme

RUN rm /etc/nginx/sites-enabled/default
ADD conf/nginx/app.conf /etc/nginx/sites-enabled/webapp.conf

RUN mkdir /root/docs_source
WORKDIR /root
RUN git clone https://github.com/snide/sphinx_rtd_theme

ADD docs/* /root/docs_source/

ADD start.sh /root/start.sh
RUN chmod 777 /root/start.sh

WORKDIR /root

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["/root/start.sh"]
