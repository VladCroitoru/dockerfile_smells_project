FROM catmaid/catmaid:stable
LABEL maintainer="Tom Kazimiers <tom@voodoo-arts.net>"

RUN service postgresql restart
RUN service nginx restart

ENTRYPOINT ["/home/scripts/docker/catmaid-entry.sh"]

EXPOSE 80
WORKDIR /home/django/projects
CMD ["standalone"]
