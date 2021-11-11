FROM docker.io/xuhui546/anaconda-centos:3.4.1.1

RUN yum install -y epel-release; yum clean all
RUN yum install -y python-devel; yum clean all
RUN yum install -y gcc gcc-c++; yum clean all
# for database
RUN yum install -y freetds*; yum clean all
RUN yum install -y unixODBC*; yum clean all
RUN yum install -y libaio*; yum clean all
# for phantomjs
RUN yum install -y freetype freetype-devel fontconfig-devel; yum clean all
# for ImageMagick
RUN yum install -y ImageMagick bitmap-fonts bitmap-fonts-cjk; yum clean all

RUN yum install -y unzip; yum clean all
RUN yum install -y nginx-1.10.1; yum clean all

RUN mkdir /opt/oracle \
    && cd /opt/oracle \
    && wget https://s3.amazonaws.com/merofile/instantclient-basic-linux.x64-12.1.0.2.0.zip \
    && wget https://s3.amazonaws.com/merofile/instantclient-sdk-linux.x64-12.1.0.2.0.zip \
    && unzip /opt/oracle/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /opt/oracle \
    && unzip /opt/oracle/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /opt/oracle \
    && ln -s /opt/oracle/instantclient_12_1/libclntsh.so.12.1 /opt/oracle/instantclient_12_1/libclntsh.so \
    && ln -s /opt/oracle/instantclient_12_1/libclntshcore.so.12.1 /opt/oracle/instantclient_12_1/libclntshcore.so \
    && ln -s /opt/oracle/instantclient_12_1/libocci.so.12.1 /opt/oracle/instantclient_12_1/libocci.so \
    && rm -rf /opt/oracle/*.zip

ENV LD_RUN_PATH /opt/oracle/instantclient_12_1
ENV ORACLE_HOME /opt/oracle/instantclient_12_1
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_12_1

RUN mkdir -p /opt/phantomjs \
    && cd /opt/phantomjs && wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2 \
    && tar -xjvf phantomjs-1.9.8-linux-x86_64.tar.bz2 --strip-components 1 \
    && ln -s /opt/phantomjs/bin/phantomjs /usr/bin/phantomjs \
    && rm /opt/phantomjs/phantomjs-1.9.8-linux-x86_64.tar.bz2

RUN pip install \
    celery==3.1.23\
    pymssql==2.1.2\
    pymysql==0.7.9\
    Django==1.9.6\
    django-autocomplete-light==3.1.5\
    django-bootstrap3==7.0.1\
    django-celery==3.1.17\
    django-cors-headers==1.1.0\
    django-crispy-forms==1.6.0\
    django-downloadview==1.9\
    django-extensions==1.6.7\
    django-filter==0.13.0\
    django-guardian==1.4.4\
    django-import-export==0.4.5\
    django-mptt==0.8.4\
    django-pandas==0.4.1\
    django-pyodbc-azure==1.9.3.0\
    django-redis==4.4.3\
    djangorestframework==3.3.3\
    djangorestframework-jwt==1.8.0\
    django-userena==2.0.1\
    pandas==0.18.1\
    python-social-auth==0.2.19\
    wechatpy==1.2.9\
    uWSGI==2.0.11.2\
    cx-Oracle==5.1.3\
    redis==2.10.3
