FROM java:6

# Image with Oracle Java 7
#FROM williamyeh/java7

ENV PLAYFRAMEWORK_VERSION=2.3.10

ADD https://raw.githubusercontent.com/guilhem/apt-get-install/master/apt-get-install /usr/bin/
RUN chmod +x /usr/bin/apt-get-install

RUN apt-get-install git patch unzip

RUN cd / && git clone git://github.com/playframework/playframework.git

RUN cd /playframework && \
	git reset --hard $PLAYFRAMEWORK_VERSION

# NOTE: the patch 422ca97c54a7ab84cb965df1474f2cd0d11e5fc6 is used to make
# Play Framework work on WebLogic 12c. This is already in the branch 2.3.x
ENV PATCHES="422ca97c54a7ab84cb965df1474f2cd0d11e5fc6"

RUN cd /playframework && \
	for hash in $PATCHES; do \
		git show -s $hash && \
		git show $hash | patch -p1 || exit 1; \
	done

# NOTE: this should be the default but if you change the base Docker image
# you may encounter an issue because part of the source code is in UTF-8.
# If the base image doesn't use UTF-8 as default encoding, the build will
# fail.
ENV LANG=C.UTF-8

RUN cd /playframework/framework && ./build publish-local

# NOTE: this is an extra layer only to make sure the Play Framework is working
# properly. You could remove this line if you want to get a lighter version of
# this image.
# NOTE: removed for now because I believe that multiple tests are broken.
# The fact that they didn't update an SSL certificate used in the tests makes
# me think that there is no more automatic build for this version and/or the
# version is not maintained anymore.
# RUN cd /playframework/framework && ./runtests

ENV ACTIVATOR_VER=1.3.4

RUN wget --progress=dot http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VER/typesafe-activator-${ACTIVATOR_VER}-minimal.zip && \
	unzip typesafe-activator-${ACTIVATOR_VER}-minimal.zip -d / && \
	rm typesafe-activator-${ACTIVATOR_VER}-minimal.zip && \
	chmod a+x /activator-${ACTIVATOR_VER}-minimal/activator

ENV PATH $PATH:/activator-$ACTIVATOR_VER-minimal

# NOTE: install activator dependencies in the image already
RUN activator list-templates || exit 0

VOLUME /root/.ivy2

RUN mkdir /app

WORKDIR /app

EXPOSE 9000 8888

ENTRYPOINT ["activator"]
