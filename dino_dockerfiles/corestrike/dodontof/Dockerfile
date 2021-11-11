# CentOSをベースに
FROM centos:centos6

# 作成者
MAINTAINER corestrike
 
# RUN コマンドを使って、yum コマンドを実行してインストールする 
RUN yum update -y && yum -y upgrade
RUN yum install -y sudo
RUN yum install -y passwd
RUN yum install -y httpd

# rubyをインストール
RUN yum install -y ruby rubygems
RUN ln -s /usr/bin/ruby /usr/local/bin/ruby
RUN gem update --system

# httpdの設定
RUN echo \<Directory "/var/www/html/DodontoF"\> >> /etc/httpd/conf/httpd.conf
RUN echo Options FollowSymLinks ExecCGI >> /etc/httpd/conf/httpd.conf
RUN echo AddHandler cgi-script .rb .pl >> /etc/httpd/conf/httpd.conf
RUN echo AddHandler application/x-shockwave-flash .swf >> /etc/httpd/conf/httpd.conf
RUN echo \</Directory\> >> /etc/httpd/conf/httpd.conf

# どどんとふをインストール
RUN yum install -y git
RUN mkdir dodontof
WORKDIR /dodontof
RUN git clone https://github.com/torgtaitai/DodontoF.git
RUN mv DodontoF /var/www/html
WORKDIR /var/www/html/DodontoF
RUN mv imageUploadSpace /var/www/html
RUN mv saveData /var/www
RUN chmod 705 -R /var/www/html/DodontoF
RUN chmod 703 -R /var/www/html/DodontoF/saveDataTempSpace
RUN chmod 703 -R /var/www/html/DodontoF/fileUploadSpace
RUN chmod 703 -R /var/www/html/DodontoF/replayDataUploadSpace
RUN chmod 606 -R /var/www/html/DodontoF/log.*
RUN chmod 707 -R /var/www/html/imageUploadSpace
RUN chmod 707 -R /var/www/saveData
RUN rm -rf /dodontof

# EXPOSE コマンドを使って、ポートを解放
EXPOSE 80

# ENTORYPOINT コマンドを使って、コンテナ起動時に実行するコマンドを与える
ENTRYPOINT /etc/init.d/httpd start && /bin/bash