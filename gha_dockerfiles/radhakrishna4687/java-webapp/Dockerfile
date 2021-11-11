FROM ubuntu:latest

ENV GITHUB_BRANCH=java-servlet-login-and-display
ENV TOMCAT_VERSION=8.5.50


# to skip the eographic area:
ENV DEBIAN_FRONTEND=nonintercative 
RUN apt-get update &&  apt-get upgrade -y &&\
    apt-get install -y apt-file && \
    apt-file update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y wget && \
    apt-get install -y maven && \
    apt-get install -y git && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Setup JAVA_HOME -- useful for docker commandline
ENV M2_HOME /usr/share/maven/
RUN export M2_HOME

#Make dir in /usr/local/tomcat
RUN mkdir -pv /usr/local/tomcat/
CMD [ "chmod ugo+rwx /usr/local/tomcat/" ]

# Download the code form github 
RUN apt-get update && \ 
    mkdir -pv /home/samplecode && \
    cd /home/samplecode && \

#ENV GITHUB_BRANCH=war-web-project
    git clone https://github.com/radhakrishna4687/${GITHUB_BRANCH}.git
    
WORKDIR /home/samplecode/  

# maven pacakage for war file
RUN java -version && \
    mvn -version;
WORKDIR /home/samplecode/${GITHUB_BRANCH}/
RUN mvn -f /home/samplecode/${GITHUB_BRANCH}/pom.xml clean package

#Install tomcat8
RUN wget --quiet --no-cookies https://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tar.gz

RUN cd /tmp && tar xvfz tomcat.tar.gz
#RUN cd /usr/local/tomcat/
RUN cp -Rv /tmp/apache-tomcat-8.5.50/* /usr/local/tomcat/

#PORT EXPOSE
EXPOSE 8080
WORKDIR /home/samplecode/${GITHUB_BRANCH}/target/
RUN cp /home/samplecode/${GITHUB_BRANCH}/target/*.war /usr/local/tomcat/webapps/app.war

RUN cd /usr/local/tomcat/conf
RUN sed -i '/<\/tomcat-users>/ i\  <user username="tomcat" password="tomcat" roles="manager-gui"/>' /usr/local/tomcat/conf/tomcat-users.xml
RUN cd /usr/local/tomcat/bin && \
    ./shutdown.sh && \
    ./startup.sh;

CMD ["/usr/local/tomcat/bin/catalina.sh", "run" ]


#URL Link : http://localhost:8090/app/
