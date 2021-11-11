FROM mafiascum/phpbb
EXPOSE 80

ARG BRANCH_NAME

# ADD config.php.docker /var/www/html/config.php
ADD install-config.yml.docker /var/www/html/install/install-config.yml.template

ADD zip_extensions /tmp/zip_extensions
ADD install_zip_extensions.sh /tmp/install_zip_extensions.sh
RUN chmod +x /tmp/install_zip_extensions.sh
RUN /tmp/install_zip_extensions.sh
RUN rm /tmp/install_zip_extensions.sh /tmp/zip_extensions

ADD git_extensions /tmp/git_extensions
ADD install_git_extensions.sh /tmp/install_git_extensions.sh
RUN chmod +x /tmp/install_git_extensions.sh
RUN /tmp/install_git_extensions.sh
RUN rm /tmp/install_git_extensions.sh /tmp/git_extensions

ADD git_styles /tmp/git_styles
ADD install_git_styles.sh /tmp/install_git_styles.sh
RUN chmod +x /tmp/install_git_styles.sh
RUN /tmp/install_git_styles.sh
RUN rm /tmp/install_git_styles.sh /tmp/git_styles

RUN chown -R www-data:www-data /var/www/

ADD ./start.sh /start.sh
RUN chmod +x /start.sh
CMD /start.sh
