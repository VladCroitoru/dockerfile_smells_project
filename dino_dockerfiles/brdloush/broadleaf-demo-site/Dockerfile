FROM java:8

ENV M2_HOME=/opt/apache-maven-3.3.3

WORKDIR /opt/broadleaf
RUN apt-get update && apt-get install -y git ant wget && \
  git clone https://github.com/BroadleafCommerce/DemoSite.git && \
  cd DemoSite && \
  wget http://mirror.hosting90.cz/apache/maven/maven-3/3.3.3/binaries/apache-maven-3.3.3-bin.tar.gz && \
  tar xvvzf apache-maven-3.3.3-bin.tar.gz -C /opt && \
  ln -s /opt/apache-maven-3.3.3/bin/mvn /usr/bin/mvn && \
  ln -s /opt/apache-maven-3.3.3/ /usr/share/maven && \
  mvn -DskipTests clean install

# needed for JVM-8 + Apache Maven 3 combination
RUN sed -i '42i   <jvmarg value="-Dmaven.multiModuleProjectDirectory=/usr/share/maven" />' /opt/broadleaf/DemoSite/site/build.xml

EXPOSE 8080
EXPOSE 8443

WORKDIR /opt/broadleaf/DemoSite/site
CMD ["ant", "tomcat"]
