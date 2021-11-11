FROM oraclelinux:7.4

WORKDIR /build

RUN yum-config-manager --enable ol7_optional_latest && \
    yum install -y tar wget ruby-devel ruby2.2-dev ruby2.0-dev gcc make rpm-build rubygems libffi-devel && \
    gem install --no-ri --no-rdoc fpm && \
    mkdir -p /build /output

COPY create_repo.sh /build/

CMD "/build/create_repo.sh"
  

