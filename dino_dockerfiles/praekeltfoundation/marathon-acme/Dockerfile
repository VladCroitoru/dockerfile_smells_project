# NOTE: This is a development Dockerfile for testing unreleased versions of
# marathon-acme
FROM praekeltfoundation/python-base:3.6-alpine

# NOTE: This requires that a wheel has been built using the command
# `python setup.py bdist_wheel`.
COPY dist/marathon_acme-*.whl .
RUN pip install marathon_acme-*.whl

# Set up the entrypoint script
COPY docker-entrypoint.sh /scripts/marathon-acme-entrypoint.sh
ENTRYPOINT ["marathon-acme-entrypoint.sh"]

# Listening port and storage directory volume
EXPOSE 8000
VOLUME /var/lib/marathon-acme
WORKDIR /var/lib/marathon-acme
CMD ["/var/lib/marathon-acme"]
