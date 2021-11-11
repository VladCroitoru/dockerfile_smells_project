FROM debian:stable-slim

# install packages
RUN apt-get update && apt-get install --no-install-recommends -y nano vim vim-scripts git rsync apt-transport-https \
    mariadb-client socat wget gnupg curl patch less ssh-client ca-certificates bzip2 file xz-utils vim-addon-manager \
    php-cli php-bcmath php-bz2 php-curl php-gd php-gmp php-json php-mbstring \
    php-mysql php-opcache php-readline php-soap php-sqlite3 php-xml php-zip zip unzip

# INSTALL additional php versions
RUN echo "deb https://packages.sury.org/php/ stretch main" > /etc/apt/sources.list.d/sury.list \
    && curl https://packages.sury.org/php/apt.gpg | apt-key add -  \
    && apt-get update && apt-get install --no-install-recommends -y php5.6-cli php5.6-bcmath php5.6-bz2 php5.6-curl php5.6-gd php5.6-gmp php5.6-json \
        php5.6-mbstring  php5.6-mysql php5.6-opcache php5.6-readline php5.6-soap php5.6-sqlite3 php5.6-xml php5.6-zip \
        php7.1-cli php7.1-bcmath php7.1-bz2 php7.1-curl php7.1-gd php7.1-gmp php7.1-json \
        php7.1-mbstring  php7.1-mysql php7.1-opcache php7.1-readline php7.1-soap php7.1-sqlite3 php7.1-xml php7.1-zip \
        php7.2-cli php7.2-bcmath php7.2-bz2 php7.2-curl php7.2-gd php7.2-gmp php7.2-json \
        php7.2-mbstring  php7.2-mysql php7.2-opcache php7.2-readline php7.2-soap php7.2-sqlite3 php7.2-xml php7.2-zip \
    && rm -rf /var/lib/apt/lists/*


# remove unneeded and potentially unsecure binaries
RUN find / -type f -perm -4000 ! -path "/proc/*" -exec chmod -s {} \; \
    && for f in \
	/bin/mount /usr/bin/chage /usr/bin/chfn /usr/bin/chsh /usr/bin/gpasswd /usr/bin/passwd \
	/usr/sbin/chgpasswd /usr/sbin/chpasswd /usr/sbin/cpgr /usr/sbin/cppw /usr/sbin/groupadd \
	/usr/sbin/groupdel /usr/sbin/groupmems /usr/sbin/groupmod /usr/sbin/grpck /usr/sbin/grpconv \
	/usr/sbin/grpunconv /usr/sbin/newusers /usr/sbin/pwck /usr/sbin/pwconv /usr/sbin/pwunconv \
	/usr/sbin/useradd /usr/sbin/userdel /usr/sbin/usermod /usr/sbin/vigr /usr/sbin/vipw \
	/usr/bin/faillog /usr/bin/lastlog /usr/bin/newgrp /usr/bin/sg /usr/sbin/update-passwd \
	/usr/sbin/addgroup /usr/sbin/adduser /usr/sbin/delgroup /usr/sbin/deluser \
	/bin/mount /bin/umount /sbin/losetup /sbin/swapoff /sbin/swapon; \
    do rm -rf $f; done
