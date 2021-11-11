FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm
RUN ls -sd /bin/true /sbin/initctl && \
	sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d

RUN apt-get update && \
	apt install php7.0-cli php7.0-xml php7.0-mysql mysql-server git wget subversion curl -y

RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash && \
	. ~/.nvm/nvm.sh && nvm install 7.6.0

RUN git clone https://github.com/xwp/wp-dev-lib.git /root/devlib
ENV DEV_LIB_PATH /root/devlib

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD install-wp-tests.sh /root/install-wp-tests.sh
RUN chmod +x /root/install-wp-tests.sh
RUN bash -lc "/root/install-wp-tests.sh wordpress_tests root '' ''"

ADD testrun /root/testrun
RUN chmod +x /root/testrun
RUN bash -lc /root/testrun

ENV PATH /tmp/dev-lib-bin:$PATH
ENV WP_INSTALL_TESTS true
ENV WP_TESTS_DIR /tmp/wordpress-tests-lib

COPY docker-entrypoint.sh /usr/local/bin

WORKDIR /repo
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/root/devlib/pre-commit"]
