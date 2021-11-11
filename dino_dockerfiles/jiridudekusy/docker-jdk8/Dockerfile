FROM centos:latest
MAINTAINER mikemckibben@gmail.com

ENV JAVA_HOME /usr/java/default
ENV LANG en_US.UTF-8
ENV JCE_POLICY_DOWNLOAD_URL http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip
ENV JRE_HOME $JAVA_HOME/jre

RUN yum -y install curl wget tar zip unzip ca-certificates libgcc libstdc++ tzdata-java zlib

RUN echo LANG=en_US.UTF-8 > /etc/sysconfig/i18n

RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u144-b01/090f390dda5b47b9b721c7dfaa008135/jdk-8u144-linux-x64.rpm > jdk-8u144-linux-x64.rpm &&\
    yum install ./jdk-8u144-linux-x64.rpm -y &&\
    yum clean all &&\
    rm jdk-8u144-linux-x64.rpm

RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" ${JCE_POLICY_DOWNLOAD_URL} > jce_policy.zip &&\
    unzip -oj -d ${JAVA_HOME}/jre/lib/security jce_policy.zip \*/\*.jar && \
    rm jce_policy.zip

RUN alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 10 \
  --slave /usr/bin/appletviewer appletviewer $JAVA_HOME/bin/appletviewer \
  --slave /usr/bin/extcheck extcheck $JAVA_HOME/bin/extcheck \
  --slave /usr/bin/idlj idlj $JAVA_HOME/bin/idlj \
  --slave /usr/bin/jar jar $JAVA_HOME/bin/jar \
  --slave /usr/bin/jarsigner jarsigner $JAVA_HOME/bin/jarsigner \
  --slave /usr/bin/javac javac $JAVA_HOME/bin/javac \
  --slave /usr/bin/javadoc javadoc $JAVA_HOME/bin/javadoc \
  --slave /usr/bin/javafxpackager javafxpackager $JAVA_HOME/bin/javafxpackager \
  --slave /usr/bin/javah javah $JAVA_HOME/bin/javah \
  --slave /usr/bin/javap javap $JAVA_HOME/bin/javap \
  --slave /usr/bin/javapackager javapackager $JAVA_HOME/bin/javapackager \
  --slave /usr/bin/jcmd jcmd $JAVA_HOME/bin/jcmd \
  --slave /usr/bin/jconsole jconsole $JAVA_HOME/bin/jconsole \
  --slave /usr/bin/jdb jdb $JAVA_HOME/bin/jdb \
  --slave /usr/bin/jdeps jdeps $JAVA_HOME/bin/jdeps \
  --slave /usr/bin/jhat jhat $JAVA_HOME/bin/jhat \
  --slave /usr/bin/jinfo jinfo $JAVA_HOME/bin/jinfo \
  --slave /usr/bin/jjs jjs $JAVA_HOME/bin/jjs \
  --slave /usr/bin/jmap jmap $JAVA_HOME/bin/jmap \
  --slave /usr/bin/jmc jmc $JAVA_HOME/bin/jmc \
  --slave /usr/bin/jps jps $JAVA_HOME/bin/jps \
  --slave /usr/bin/jrunscript jrunscript $JAVA_HOME/bin/jrunscript \
  --slave /usr/bin/jsadebugd jsadebugd $JAVA_HOME/bin/jsadebugd \
  --slave /usr/bin/jstack jstack $JAVA_HOME/bin/jstack \
  --slave /usr/bin/jstat jstat $JAVA_HOME/bin/jstat \
  --slave /usr/bin/jstatd jstatd $JAVA_HOME/bin/jstatd \
  --slave /usr/bin/jvisualvm jvisualvm $JAVA_HOME/bin/jvisualvm \
  --slave /usr/bin/keytool keytool $JAVA_HOME/bin/keytool \
  --slave /usr/bin/native2ascii native2ascii $JAVA_HOME/bin/native2ascii \
  --slave /usr/bin/orbd orbd $JAVA_HOME/bin/orbd \
  --slave /usr/bin/pack200 pack200 $JAVA_HOME/bin/pack200 \
  --slave /usr/bin/policytool policytool $JAVA_HOME/bin/policytool \
  --slave /usr/bin/rmic rmic $JAVA_HOME/bin/rmic \
  --slave /usr/bin/rmid rmid $JAVA_HOME/bin/rmid \
  --slave /usr/bin/rmiregistry rmiregistry $JAVA_HOME/bin/rmiregistry \
  --slave /usr/bin/schemagen schemagen $JAVA_HOME/bin/schemagen \
  --slave /usr/bin/serialver serialver $JAVA_HOME/bin/serialver \
  --slave /usr/bin/servertool servertool $JAVA_HOME/bin/servertool \
  --slave /usr/bin/tnameserv tnameserv $JAVA_HOME/bin/tnameserv \
  --slave /usr/bin/unpack200 unpack200 $JAVA_HOME/bin/unpack200 \
  --slave /usr/bin/wsgen wsgen $JAVA_HOME/bin/wsgen \
  --slave /usr/bin/wsimport wsimport $JAVA_HOME/bin/wsimport \
  --slave /usr/bin/xjc xjc $JAVA_HOME/bin/xjc

RUN sed -i "s|securerandom.source=file:/dev/random|securerandom.source=file:/dev/urandom|g" $JRE_HOME/lib/security/java.security
