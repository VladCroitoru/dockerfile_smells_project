

FROM centos:centos7

# add npm package
RUN rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
RUN rpm -ivh http://ftp.riken.jp/Linux/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm

# update epel-release
RUN yum remove -y epel-release
RUN yum install -y epel-release

# add required packages
RUN yum install -y git python openssl-devel gcc gcc-c++

# nginx
RUN yum install -y nginx --enablerepo=nginx
RUN rm /usr/share/nginx/html/*
RUN sed -i "s/        index  index.html index.htm;/        index  index.html index.htm; try_files \$uri \$uri\/ \/index.html =404;/g" /etc/nginx/conf.d/default.conf

# node
# RUN git clone https://github.com/creationix/nvm.git ~/.nvm && cd ~/.nvm && git checkout `git describe --abbrev=0 --tags`
# RUN echo ". ~/.nvm/nvm.sh" >> ~/.bash_profile

# RUN /bin/bash -c '. ~/.nvm/nvm.sh && nvm install 4.2.1 && nvm use 4.2.1 && nvm alias default 4.2.1 && ln -s ~/.nvm/4.2.1/bin/node /usr/bin/node && ln -s ~/.nvm/4.2.1/bin/npm /usr/bin/npm'

# ruby
# RUN yum install -y ruby ruby-devel
# RUN gem install sass -v "3.4.19"

# clone repository
RUN git clone https://github.com/makky3939/EscapeGoat.git

# build
# RUN /bin/bash -c '. ~/.nvm/nvm.sh && cd EscapeGoat && npm install'
# RUN /bin/bash -c '. ~/.nvm/nvm.sh && cd EscapeGoat && npm run build'
RUN cp -r EscapeGoat/escapegoat/* /usr/share/nginx/html/

# port open
EXPOSE 80

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
