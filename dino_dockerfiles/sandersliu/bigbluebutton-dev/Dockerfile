#name of container: docker-bigbluebutton development env
#versison of container: 0.5.1
FROM sandersliu/bbb090
MAINTAINER sanders liu "sandersliu@hotmail.com"
# Set correct environment variables.

RUN bbb-conf --stop

RUN apt-get install -y git-core ant openjdk-6-jdk 

RUN mkdir -p ~/dev/tools
RUN cd ~/dev/tools

RUN wget http://bigbluebutton.googlecode.com/files/gradle-0.8.tar.gz
RUN tar xvfz gradle-0.8.tar.gz

RUN wget http://bigbluebutton.googlecode.com/files/groovy-1.6.5.tar.gz
RUN tar xvfz groovy-1.6.5.tar.gz

RUN wget https://bigbluebutton.googlecode.com/files/grails-1.3.9.tar.gz
RUN tar xvfz grails-1.3.9.tar.gz

RUN wget http://fpdownload.adobe.com/pub/flex/sdk/builds/flex4.5/flex_sdk_4.5.0.20967_mpl.zip

mkdir -p ~/dev/tools/flex-4.5.0.20967
unzip flex_sdk_4.5.0.20967_mpl.zip -d flex-4.5.0.20967

RUN find ~/dev/tools/flex-4.5.0.20967 -type d -exec chmod o+rx '{}' \;
RUN chmod 755 ~/dev/tools/flex-4.5.0.20967/bin/*
RUN chmod -R +r ~/dev/tools/flex-4.5.0.20967

RUN ln -s ~/dev/tools/flex-4.5.0.20967 ~/dev/tools/flex

RUN mkdir -p flex-4.5.0.20967/frameworks/libs/player/11.2

RUN cd flex-4.5.0.20967/frameworks/libs/player/11.2

RUN wget http://download.macromedia.com/get/flashplayer/updaters/11/playerglobal11_2.swc

RUN mv -f playerglobal11_2.swc playerglobal.swc

RUN echo "export GROOVY_HOME=$HOME/dev/tools/groovy-1.6.5" >> ~/.profile \
    && echo "export PATH=$PATH:$GROOVY_HOME/bin" >> ~/.profile \
    && echo "export GRAILS_HOME=$HOME/dev/tools/grails-1.3.9" >> ~/.profile \
    && echo "export PATH=$PATH:$GRAILS_HOME/bin" >> ~/.profile \
    && echo "export FLEX_HOME=$HOME/dev/tools/flex" >> ~/.profile \
    && echo "export PATH=$PATH:$FLEX_HOME/bin" >> ~/.profile \
    && echo "export GRADLE_HOME=$HOME/dev/tools/gradle-0.8" >> ~/.profile \
    && echo "export PATH=$PATH:$GRADLE_HOME/bin" >> ~/.profile \
    && echo "export JAVA_HOME=/usr/lib/jvm/java-6-openjdk" >> ~/.profile \
    && echo "export ANT_OPTS="-Xmx512m -XX:MaxPermSize=512m"" >> ~/.profile

RUN source ~/.profile

RUN cd ~/dev/bigbluebutton

RUN git status

RUN mxmlc -version
    
    
