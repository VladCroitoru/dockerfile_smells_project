FROM phusion/baseimage:0.9.22
MAINTAINER bveldhuis

ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" TERM="xterm"

COPY sources.list /etc/apt/sources.list
COPY *.sh /etc/my_init.d/

RUN useradd -u 911 -U -d /config -s /bin/false abc && \
      usermod -G users abc && \
      mkdir -p /app/aptselect /config /defaults && \
      LATEST_TAG=$(curl -sX GET "https://api.github.com/repos/jblakeman/apt-select/releases/latest" | awk '/tag_name/{print $4;exit}' FS='[""]') && \
      curl -L https://github.com/jblakeman/apt-select/archive/${LATEST_TAG}.tar.gz | tar xvz -C /app/aptselect --strip-components=1 && \
      add-apt-repository -y ppa:ondrej/php && \
	  apt-get update && \
      apt-get install -y tzdata python3-bs4 && \
      apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
      chmod +x /etc/my_init.d/*.sh && \
      apt-get clean && \
      rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/sbin/my_init"]

# Set correct environment variables
ENV APTLIST="apache2 apache2-bin perl libaprutil1-dbd-mysql libapache2-mod-fastcgi openssl wget inotify-tools php7.1 php7.1-curl libapache2-mod-php7.1 php7.1-cli php7.1-common php7.1-mbstring php7.1-gd php7.1-intl php7.1-xml php7.1-mysql php7.1-mcrypt php7.1-zip php7.1-bcmath" LANG="en_US.UTF-8" LANGUAGE="en_US:en" LC_ALL="en_US.UTF-8"

# Set the locale
RUN locale-gen en_US.UTF-8

# install main packages
RUN apt-get update -qy && \
apt-get install $APTLIST -qy && \

# cleanup 
apt-get clean -y && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add some files 
ADD defaults/ /defaults/
ADD init/ /etc/my_init.d/
ADD services/ /etc/service/
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh
	
# enable apache mods
RUN cp /etc/apache2/ports.conf /defaults/ports.conf && \
mv /defaults/envvars /etc/apache2/envvars && \
sed -i "s#/var/www#/config/www#g" /etc/apache2/apache2.conf && \
sed -i "s#IncludeOptional sites-enabled#IncludeOptional /config/apache/site-confs#g" /etc/apache2/apache2.conf && \
sed -i '/Include ports.conf/s/^/#/g' /etc/apache2/apache2.conf && \
echo "Include /config/apache/ports.conf"  >> /etc/apache2/apache2.conf && \
cp /etc/apache2/apache2.conf /defaults/apache2.conf && \
a2enmod actions rewrite fastcgi alias ssl

# add some files
ADD services/ /etc/service/
RUN chmod -v +x /etc/service/*/run /etc/service/*/finish /etc/my_init.d/*.sh

# Update apache configuration with this one
RUN a2enmod proxy proxy_http proxy_ajp rewrite deflate substitute headers proxy_balancer proxy_connect proxy_html xml2enc authnz_ldap

# expose ports
EXPOSE 80 443

# set volumes
VOLUME /config
