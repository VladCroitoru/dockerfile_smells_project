FROM amazonlinux:latest

ADD . .

RUN yum update -y
RUN yum install aws-cli -y
RUN yum install ruby -y
RUN yum install wget -y

RUN sh elastic.sh

RUN yum install filebeat -y
RUN chkconfig --add filebeat
RUN chkconfig filebeat on

RUN yum install htop -y

RUN sh pip.sh
RUN pip install --upgrade pip
RUN pip install ansible

#RUN sh codedeploy.sh
#RUN curl -SLO "https://s3.amazonaws.com/codeship-jet-releases/1.19.3/jet-linux_amd64_1.19.3.tar.gz"
#RUN tar -xaC /usr/local/bin -f jet-linux_amd64_1.19.3.tar.gz
#RUN chmod +x /usr/local/bin/jet

RUN yum install nginx -y
RUN yum install php56-fpm php56 php56-opcache php56-xml php56-mcrypt php56-gd php56-devel php56-mysql php56-intl php56-mbstring php56-bcmath php56-pecl-memcache php56-soap php56-mysqlnd -y


RUN yum install git -y
RUN yum install gcc -y
RUN yum install cronie -y
RUN yum install memcached -y

#RUN easy_install supervisor
#RUN sh -c '/usr/local/bin/echo_supervisord_conf > /etc/supervisord.conf'
#RUN chmod 600 /etc/supervisord.conf

#RUN sh -c 'curl -L https://raw.githubusercontent.com/Supervisor/initscripts/master/redhat-init-jkoppe > /etc/init.d/supervisord'
#RUN chmod +x /etc/init.d/supervisord
#RUN chkconfig --add supervisord
#RUN chkconfig supervisord on

RUN chkconfig --add php-fpm
RUN chkconfig php-fpm on

RUN chkconfig --add nginx
RUN chkconfig nginx on

RUN yum install unzip zip -y
RUN yum install mysql -y
RUN curl -sS https://getcomposer.org/installer | php -- --install -dir=/usr/bin/ --filename=composer
RUN sh -c 'echo -e "short_open_tag=On" > /etc/php-5.6.d/shortopentags.ini'
RUN sh -c 'echo -e "date.timezone=\"Asia/Singapore\"" > /etc/php-5.6.d/timezone.ini'

#RUN mkdir /log


