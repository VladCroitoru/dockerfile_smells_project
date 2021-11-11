FROM centos/php-70-centos7

USER root

COPY tideways.repo /etc/yum.repos.d/tideways.repo

RUN rpm --import https://s3-eu-west-1.amazonaws.com/qafoo-profiler/packages/EEB5E8F4.gpg && \
    yum makecache --disablerepo=* --enablerepo=tideways && \
    yum -y install tideways-php tideways-cli tideways-daemon && \
    yum clean all && \
    cp /usr/lib/tideways/tideways-php-7.0.so /opt/rh/rh-php70/root/usr/lib64/php/modules/tideways.so && \
    cp /etc/php.d/40-tideways.ini /etc/opt/rh/rh-php70/php.d/40-tideways.ini && \
    wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    wget https://rpms.remirepo.net/enterprise/remi-release-7.rpm && \
    rpm -Uvh remi-release-7.rpm epel-release-latest-7.noarch.rpm && \
    yum -y install environment-modules tcl && \
    rpm -Uvh --nodeps $(repoquery --location php70-php-ast) && \
    yum clean all && \
    cp -v /opt/remi/php70/root/usr/lib64/php/modules/ast.so /opt/rh/rh-php70/root/usr/lib64/php/modules/ast.so && \
    cp -v /etc/opt/remi/php70/php.d/40-ast.ini /etc/opt/rh/rh-php70/php.d/40-ast.ini && \
    rm remi-release-7.rpm epel-release-latest-7.noarch.rpm

USER 1001
