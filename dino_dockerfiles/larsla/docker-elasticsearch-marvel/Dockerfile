FROM elasticsearch

RUN plugin install license
RUN plugin install marvel-agent

EXPOSE 9200 9300
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
