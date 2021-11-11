# BUILD-USING:        docker build -t qualia/qualifi .
# RUN-USING:          docker run -i -name qualifi qualia/qualifi && docker wait qualifi && docker cp qualifi:/root/app/bin/QualiFi-release.apk . && docker rm qualifi

FROM          ubuntu:12.04
RUN           DEBIAN_FRONTEND=noninteractive apt-get update -y
MAINTAINER    Drew Carey Buglione <me@drewb.ug>
WORKDIR       root

RUN           DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-properties
RUN           DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:webupd8team/java && apt-get update -y
RUN           echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN           DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java7-installer

RUN           wget http://jruby.org.s3.amazonaws.com/downloads/1.7.11/jruby-bin-1.7.11.tar.gz && \
                tar xvfz jruby-bin-1.7.11.tar.gz && \
                mv jruby-1.7.11 jruby && \
                rm jruby-bin-1.7.11.tar.gz
ENV           PATH /root/jruby/bin:$PATH

RUN           wget http://archive.apache.org/dist/ant/binaries/apache-ant-1.9.3-bin.tar.gz && \
                tar -xvzf apache-ant-1.9.3-bin.tar.gz && \
                mv apache-ant-1.9.3 apache-ant && \
                rm apache-ant-1.9.3-bin.tar.gz
ENV           ANT_HOME /root/apache-ant
ENV           PATH $ANT_HOME/bin:$PATH

RUN           DEBIAN_FRONTEND=noninteractive apt-get install -y fakeroot && \
                DEBIAN_FRONTEND=noninteractive fakeroot apt-get install -y fuse && \
                DEBIAN_FRONTEND=noninteractive apt-get remove -y fakeroot

RUN           DEBIAN_FRONTEND=noninteractive apt-get install -y ia32-libs

RUN           wget http://dl.google.com/android/android-sdk_r22.6.1-linux.tgz && \
                tar xvfz android-sdk_r22.6.1-linux.tgz && \
                mv android-sdk-linux android-sdk && \
                rm android-sdk_r22.6.1-linux.tgz
ENV           ANDROID_HOME /root/android-sdk
ENV           PATH $ANDROID_HOME/tools:$PATH

RUN           echo 'y' | android update sdk --all --no-ui --filter platform-tools
ENV           PATH $ANDROID_HOME/platform-tools:$PATH

RUN           echo 'y' | android update sdk --all --no-ui --filter build-tools-19.0.3
ENV           PATH $ANDROID_HOME/build-tools/19.0.3:$PATH

RUN           echo 'y' | android update sdk --all --no-ui --filter android-10

RUN           jruby -S gem install ruboto && jruby -S ruboto setup

###

ADD           . /root/app
WORKDIR       /root/app
CMD           jruby -S rake release
