FROM phusion/passenger-ruby24:0.9.22

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get upgrade -y && apt-get install -y nodejs libpq-dev build-essential python2.7 locales tzdata && apt autoremove -y
RUN npm install --global yarn && ln -s /usr/bin/python2.7 /usr/bin/python

CMD ["bash"]
