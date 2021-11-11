FROM mysql:5.7.23
ENV WARTEZEIT=15
COPY assets/lazy_entrypoint.sh /
ENTRYPOINT ["/lazy_entrypoint.sh"]
CMD ["mysqld"]
