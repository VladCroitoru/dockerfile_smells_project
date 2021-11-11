# docker build -t nkonev/rendertron-docker:0.0.4 -t nkonev/rendertron-docker:latest .
FROM centos
ARG OPT_DIR=/opt/rendertron
RUN mkdir -p $OPT_DIR
WORKDIR $OPT_DIR
RUN yum install -y epel-release && \
        yum install -y python36 && \
	yum -y install nodejs chromium
RUN npm install -g rendertron --unsafe && \
	rm -rf ~/.cache/node-gyp
EXPOSE 3000
ENTRYPOINT ["rendertron"]
