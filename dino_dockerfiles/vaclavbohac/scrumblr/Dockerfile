FROM hepsw/slc-base:6.5

RUN yum upgrade -y; yum install -y nodejs redis git npm

RUN cd /opt && git clone https://github.com/vaclavbohac/scrumblr

WORKDIR /opt/scrumblr
RUN npm install

CMD chown redis /var/lib/redis && service redis start && npm start

