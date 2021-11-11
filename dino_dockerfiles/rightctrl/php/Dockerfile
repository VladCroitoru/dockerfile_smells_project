FROM rightctrl/centos
MAINTAINER RightCtrl <support@RightCtrl.com>
#Virtual hosting
RUN yum install -y httpd epel-release wget
RUN wget -q http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
#RUN wget -q https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN rpm -Uvh remi-release-7.rpm
RUN yum-config-manager --enable remi-php70
RUN yum update -y
RUN yum install -y --skip-broken httpd php mod_php php-devel php-mysqlnd php-common php-pdo php-gd php-cli php-mcrypt php-mbstring php-xml php-imap php-curl php-soap mod_ssl pwgen

RUN mkdir -p /data/php/session
RUN mkdir -p /data/php/tmp
RUN mkdir -p /fileserver
RUN chown -R apache: /data/php/ /fileserver

RUN sed -i \
        -e 's/^expose_php = .*/expose_php = Off/' \
        -e 's/^display_errors = .*/display_errors = On/' \
        -e 's/^log_errors = .*/log_errors = Off/' \
        -e 's/^short_open_tag = .*/short_open_tag = On/' \
        -e 's/^error_reporting = .*/error_reporting = E_WARNING \& ~E_NOTICE \& ~E_DEPRECATED/' \
        -e 's/^memory_limit = .*/memory_limit = 1024M/' \
        -e 's/^max_execution_time = .*/max_execution_time = 0/' \
        -e 's/^session.gc_maxlifetime = .*/session.gc_maxlifetime = 2880/' \
        -e 's#^;error_log = syslog#;error_log = syslog\nerror_log = /data/php/log/scripts-error.log#' \
        -e 's/^file_uploads = .*/file_uploads = On/' \
        -e 's/^upload_max_filesize = .*/upload_max_filesize = 50M/' \
        -e 's/^allow_url_fopen = .*/allow_url_fopen = On/' \
        -e 's/^allow_url_include = .*/allow_url_include  = Off/' \
        -e 's/^sql.safe_mode = .*/sql.safe_mode = On/' \
        -e 's/^post_max_size = .*/post_max_size = 100M/' \
        -e 's/^session.name = .*/session.name = PSID/' \
        -e 's#^;session.save_path = .*#session.save_path = /data/php/session#' \
        -e 's/^session.cookie_httponly.*/session.cookie_httponly = On/' \
        -e 's#^;upload_tmp_dir.*#upload_tmp_dir = /data/php/tmp#' \
        -e 's#^;date.timezone.*#date.timezone = Asia\/Tokyo#' \
        -e 's#^;mbstring.language.*#mbstring.language = Neutral , English , Japanese#' \
        -e 's#^;mbstring.internal_encoding.*#mbstring.internal_encoding = UTF-8#' \
        -e 's#^;mbstring.http_input.*#mbstring.http_input = pass , UTF-8, SJIS, EUC-JP#' \
        -e 's#^;mbstring.http_output.*#mbstring.http_output = SJIS , UTF-8#' \
        /etc/php.ini



EXPOSE 80
EXPOSE 443

#RUN rm -rf /run/httpd/* /tmp/httpd*
#CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh
CMD ["/run-httpd.sh"]
