FROM readytalk/nodejs:0.10.36
MAINTAINER nathan@hurel.me

RUN apt-get update && apt-get install -y git\
	pkg-config\
	libgnome-keyring1.0-cil\
	libgnome-keyring1.0-cil-dev\
	libgnome-keyring-dev\
	libgnome-keyring-common\
	fakeroot\
	rpm
WORKDIR /tmp
ENV N1_RELEASE 0.4.9
RUN curl -L https://github.com/nylas/N1/archive/$N1_RELEASE.tar.gz | tar xvz
WORKDIR /tmp/N1-$N1_RELEASE
RUN script/bootstrap

COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENV ENGINE_URL http://selfhosted:5555
CMD /entrypoint.sh
