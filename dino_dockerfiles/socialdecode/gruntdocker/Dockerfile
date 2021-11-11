FROM monostream/nodejs-gulp-bower
RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates software-properties-common lsb-release
RUN curl -fsSL https://yum.dockerproject.org/gpg | apt-key add -
RUN add-apt-repository "deb https://apt.dockerproject.org/repo/ debian-$(lsb_release -cs) main"
RUN apt-get update
RUN apt-get -y install docker-engine