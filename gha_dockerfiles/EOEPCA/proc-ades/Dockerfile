FROM centos/devtoolset-7-toolchain-centos7
USER root

SHELL ["/bin/bash", "-c"]

RUN yum install -y epel-release                                                                 && \
    yum update -y                                                                               && \
    yum install -y json-c json-c-devel zlib-devel libxml2 libxml2-devel bison openssl  python-devel subversion libxslt-devel libcurl-devel gdal gdal-devel proj-devel libuuid-devel openssl-devel fcgi-devel wget unzip autoconf flex cmake3 && \
    yum install -y bzip2 kernel-devel which && ln -s /opt/rh/devtoolset-7/enable /etc/profile.d/rhgccenable.sh && chmod +x /etc/profile.d/rhgccenable.sh && \
    yum install -y git                                                                          && \
    yum install -y automake                                                                     && \
	cd                                                                                          && \
	wget http://ftp.gnu.org/gnu/cgicc/cgicc-3.2.19.tar.gz                                       && \
	tar -zxvf cgicc-3.2.19.tar.gz                                                               && \
	cd cgicc-3.2.19 && ./autogen && ./configure && make && make install                         && \
	cd && rm -fvR cgicc*
ENV PATH "$PATH:/usr/local/bin"

RUN mkdir /project
COPY 3ty /project/3ty
COPY assets /project/assets
COPY test /project/test
COPY src /project/src
COPY CMakeLists.txt /project/CMakeLists.txt
WORKDIR /project

### ZOO Build
##  from ZOO source 
RUN cp 3ty/proc-comm-zoo-1.2-alpha/assets/zoo-project.tar.gz /opt/zoo-project.tar.gz
RUN cd /opt/ && tar -zxvf zoo-project.tar.gz && rm -f zoo-project.tar.gz
### Apply patches
RUN cp 3ty/proc-comm-zoo-1.2-alpha/assets/patch/zoo/response_print.c /opt/zoo-project/zoo-project/zoo-kernel/response_print.c            && \
    cp 3ty/proc-comm-zoo-1.2-alpha/assets/patch/zoo/zoo_service_loader.c /opt/zoo-project/zoo-project/zoo-kernel/zoo_service_loader.c    && \
    cp 3ty/proc-comm-zoo-1.2-alpha/assets/patch/zoo/service_json.c /opt/zoo-project/zoo-project/zoo-kernel/service_json.c
### Make libcgi
RUN cd /opt/zoo-project/thirds/cgic206 && make libcgic.a && make install
### Configure ZOO
RUN cd /opt/zoo-project/zoo-project/zoo-kernel/ && autoconf && \
./configure  --with-json=/usr/ --with-fastcgi=${FOLDER}/libfcgi-2.4.0.orig/OUT/lib --with-xml2config=/usr/bin/xml2-config  --with-cgi-dir=/var/www/zoo-bin --with-etc-dir=yes --sysconfdir=/zooservices
### Make ZOO
RUN cd /opt/zoo-project/zoo-project/zoo-kernel/ && ls -ltr && make && make install

### Create production directories
RUN mkdir -p /opt/t2service /opt/watchjob /var/www/zoo-bin/ /var/www/data/ /etc/zoo-project/ /var/www/_run/res/statusInfos /var/www/t2dep/ /opt/watchjob/
### Make job status service
RUN cd /opt/zoo-project/zoo-project/zoo-services/utils/status && make 
### Copy it as a service
RUN cd /opt/zoo-project/zoo-project/zoo-services/utils/status/cgi-env && cp longProcess.zcfg wps_status.zo GetStatus.zcfg /opt/t2service/ && \
    cp /opt/zoo-project/zoo-project/zoo-services/utils/status/cgi-env/updateStatus.xsl /var/www/data/updateStatus.xsl
### Copy watchjob source
RUN cp -r 3ty/proc-comm-zoo-1.2-alpha/src/* /opt/watchjob/
### Make watchjob
RUN cd /opt/watchjob/ && make && make install

## Make ADES
RUN  rm -rf build && mkdir -p build && cd build
WORKDIR /project/build/
RUN cmake3 -DCMAKE_BUILD_TYPE=release -G "CodeBlocks - Unix Makefiles" .. && \
    make eoepcaows workflow_executor pep_resource && mkdir -p /project/zooservice

## Make deploy/undeploy service
RUN make -C ../src/deployundeploy/zoo/

## Install HTTPD
RUN yum install -y vim httpd \
	&& mkdir -p /var/www/zoo-bin/ /etc/zoo-project/ /var/www/_run/res/statusInfos \
	&& mkdir -p /zooservices &&  chmod 777 /zooservices \
	&& mkdir -p /var/www/fcgi/ /var/www/_run/zoo  /var/www/_run/wps3 /var/www/t2dep /var/www/_run/watchjob \
	&& chown -R 48:48 /var/www/zoo-bin/ /var/www/zoo-bin/ /var/www/data/ /var/www/_run/res  \
	&& echo '/usr/local/lib' > /etc/ld.so.conf.d/zoo.conf && ldconfig \
	&& mkdir -p /opt/t2build/includes  /opt/t2service/ /opt/opt/t2service/t2scripts/ \
	&& mkdir -p /var/www/zoo-bin/ /var/www/_run/zoo/

## Copy HTTP files
COPY 3ty/proc-comm-zoo-1.2-alpha/assets/zoo/httpd/htaccess_html /var/www/html/.htaccess
COPY 3ty/proc-comm-zoo-1.2-alpha/assets/zoo/httpd/htaccess_wps3 /var/www/_run/wps3/.htaccess
COPY 3ty/proc-comm-zoo-1.2-alpha/assets/zoo/httpd/htaccess_watchjob /var/www/_run/watchjob/.htaccess
COPY 3ty/proc-comm-zoo-1.2-alpha/assets/zoo/httpd/htaccess /var/www/_run/zoo/.htaccess
COPY 3ty/proc-comm-zoo-1.2-alpha/assets/zoo/httpd/zoo.conf	/etc/httpd/conf.d/zoo.conf
#COPY 3ty/proc-comm-zoo-1.2-alpha/assets/main.cfg /etc/zoo-project/main.cfg
COPY 3ty/proc-comm-zoo-1.2-alpha/assets/oas.cfg /etc/zoo-project/oas.cfg

## Build the base service interface
COPY src /project/src
COPY 3ty/proc-comm-lib-ows-1.04 /project/3ty/proc-comm-lib-ows-1.04
COPY 3ty/nlohmann /project/3ty/nlohmann
COPY 3ty/jwt-cpp /project/3ty/jwt-cpp
WORKDIR /project/zooservice

RUN make -C ../src/templates interface

## Install Workflow executor
ENV BASH_ENV=~/.bashrc                                          \
    MAMBA_ROOT_PREFIX=/srv/conda                                \
    PATH=/srv/conda/envs/workflow_executor_env/bin:$PATH

RUN wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba --strip-components=1 && \
    ./micromamba shell init -s bash -p ~/micromamba                                                                         && \
    rm -rf /var/lib/{apt,dpkg,cache,log}                                                                                    && \
    cp ./micromamba /usr/bin                                                                                                && \
    micromamba env create -n workflow_executor_env                                                                          && \
    micromamba install workflow-executor=1.0.7 -c eoepca -c conda-forge -c terradue -n workflow_executor_env                && \
    rm -fr /srv/conda/pkgs                                                                                                  && \
    rm -fr /tmp/*

COPY assets/main.cfg /opt/t2service/main.cfg
COPY assets/oas.cfg /opt/t2service/oas.cfg

COPY assets/scripts/entrypoint.sh /opt/t2scripts/entrypoint.sh
RUN chmod +x /opt/t2scripts/entrypoint.sh

COPY assets/workflowwxecutorconfig.json /opt/t2config/workflowwxecutorconfig.json
COPY src/templates/template.cpp /opt/t2template/template.cpp
COPY src/templates/Makefile /opt/t2template/Makefile
RUN cp /project/src/deployundeploy/zoo/build/libepcatransactional.zo /opt/t2service/
COPY src/deployundeploy/zoo/*.zcfg /opt/t2service/
RUN mkdir -p /opt/t2libs && cp /project/src/templates/libinterface.so /opt/t2libs/libinterface.so   && \
    cp /project/build/3ty/proc-comm-lib-ows-1.04/libeoepcaows.so /opt/t2libs/

RUN cp /project/build/libworkflow_executor.so /opt/t2service/libworkflow_executor.so                && \
    cp /project/build/libpep_resource.so /opt/t2service/libpep_resource.so                          && \
    mkdir -p /opt/zooservices_user && chown 48:48 /opt/zooservices_user
COPY assets/scripts/prepareUserSpace.sh /opt/t2scripts/prepareUserSpace.sh
COPY assets/scripts/removeservice.sh /opt/t2scripts/removeservice.sh
RUN chmod +x /opt/t2scripts/prepareUserSpace.sh /opt/t2scripts/removeservice.sh                     && \
    echo "alias ll='ls -ltr'" >> $HOME/.bashrc                                                      && \
    yum install mlocate -y

CMD ["/opt/t2scripts/entrypoint.sh"]

EXPOSE 80

