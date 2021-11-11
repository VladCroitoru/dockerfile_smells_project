FROM rebootshen/selenium

EXPOSE 4444

ADD start_grid.sh /var/start_grid.sh
RUN chmod 755 /var/start_grid.sh

CMD ["/bin/bash", "/var/start_grid.sh"]
