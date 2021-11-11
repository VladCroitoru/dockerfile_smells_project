FROM centos:7
MAINTAINER Nhan Nguyen <nxtnhan@gmail.com>
RUN yum -y update
# Install Nginx Latest
ADD nginx.repo /etc/yum.repos.d/nginx.repo
RUN yum -y install nginx

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# Install build tools
RUN yum -y install gcc-c++ pcre-devel zlib-devel make unzip 
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
# Install PHP 7
RUN yum -y install --enablerepo=webtatic php70w php70w-opcache
# Install Git latest  
RUN yum -y install curl-devel expat-devel gettext-devel openssl openssl-devel zlib-devel bzip2
RUN yum -y install gcc perl-ExtUtils-MakeMaker

RUN cd /usr/src && \
    git clone https://github.com/git/git
RUN cd /usr/src/git && make prefix=/usr/local/git all && make prefix=/usr/local/git install
RUN yum -y remove git

# Use new Git
env PATH /usr/local/git/bin:$PATH

# Install Depot Tools
RUN cd /usr/src && git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
env PATH /usr/src/depot_tools:$PATH

# Install v8
RUN cd /usr/src && fetch v8
RUN cd /usr/src/v8 && make native library=shared snapshot=off -j 4

RUN cp -R /usr/src/v8/out/native/lib.target/lib* /lib64/
RUN cp /usr/src/v8/out/native/obj.target/tools/gyp/libv8_libplatform.a /usr/lib64/
RUN cp -R /usr/src/v8/include /usr/local

# Install v8js
RUN yum -y --enablerepo=webtatic install php70w-pear
RUN yum -y --enablerepo=webtatic install php70w-devel
RUN echo "/usr/lib64" | pecl install v8js-1.0.0 

ENV NO_INTERACTION 1
RUN echo extension=v8js.so > /etc/php.d/v8js.ini
RUN php -m | grep v8

# Check V8Js class
RUN php -r 'var_dump(get_declared_classes());' | grep V8
RUN php -r '$class = new ReflectionClass("V8Js"); var_dump($class->getMethods());'
# Excute test v8js
RUN php -r '$v8 = new V8Js(); var_dump($v8->executeString("1+2+3"));'