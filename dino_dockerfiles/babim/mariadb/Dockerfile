# vim:set ft=dockerfile:
FROM babim/debianbase:9
ENV OSDEB stretch

# Download option
RUN apt-get update && \
    apt-get install -y curl bash && \
    curl https://raw.githubusercontent.com/babim/docker-tag-options/master/z%20SCRIPT%20AUTO/option.sh -o /option.sh && \
    chmod 755 /option.sh

# clean
RUN apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/start.sh"]
CMD ["mysqld"]
#CMD ["supervisord", "-nc", "/etc/supervisor/supervisord.conf"]