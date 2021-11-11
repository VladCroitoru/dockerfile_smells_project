FROM cptactionhank/atlassian-jira:latest
USER root
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh
USER daemon
ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["/opt/atlassian/jira/bin/start-jira.sh", "-fg"]