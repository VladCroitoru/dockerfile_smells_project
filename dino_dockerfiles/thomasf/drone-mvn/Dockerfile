# Docker image for the Drone mvn plugin runner
#

from java:8

run mkdir -p /opt \
      && cd /opt \
      && wget -q http://apache.mirrors.spacedump.net/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz \
      && tar -xf apache-maven-3.3.9-bin.tar.gz \
      && ln -s apache-maven-3.3.9 apache-maven

env PATH=/opt/apache-maven/bin:$PATH

# hacky way to get most maven dependencies into the cache
run echo '<settings></settings>' > /tmp/s \
    && mvn -B -q -s /tmp/s \
    org.apache.maven.plugins:maven-deploy-plugin:2.8.2:deploy-file \
    -Durl=file:/tmp/t \
    -DrepositoryId=t \
    -Dfile=/bin/ls \
    -DartifactId=t \
    -Dversion=1.0 \
    -DgroupId=t \
    -Dpackaging=t \
    && rm -rf /tmp/t \
    && rm -rf /tmp/s \
    && rm -rf /root/.m2/repository/t

run echo '<settings></settings>' > /tmp/s \
    && mvn -B -q -s /tmp/s \
    org.apache.maven.plugins:maven-gpg-plugin:1.6:sign-and-deploy-file \
    -Durl=file:/tmp/t \
    -DrepositoryId=t \
    -Dfile=/bin/ls \
    -DartifactId=t \
    -Dversion=1.0 \
    -DgroupId=t \
    -Dpackaging=t \
    || rm -rf /tmp/t \
    && rm -rf /tmp/s \
    && rm -rf /root/.m2/repository/t


run mkdir -p /usr/local && curl -sSL https://golang.org/dl/go1.5.1.linux-amd64.tar.gz \
        | tar -C /usr/local/ -xz
env GOPATH /go
env PATH $GOPATH/bin:/usr/local/go/bin:$PATH

add . /go/src/github.com/thomasf/drone-mvn
run GO15VENDOREXPERIMENT=1 go build -o /bin/drone-mvn /go/src/github.com/thomasf/drone-mvn/main.go

run rm -rf /go

entrypoint ["/bin/drone-mvn"]
