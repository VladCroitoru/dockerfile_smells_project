FROM redmine:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
                gcc \
                make \
                patch \
                vim \
                less \

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]

