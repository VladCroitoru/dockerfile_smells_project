FROM python:2.7-alpine
RUN pip install j2cli

# Add all template files to /source. Anything there (recursively) is going to 
# be considered as jinja2 template and preprocessed to /destination directory

VOLUME /destination

ADD convert.sh /bin/
ENTRYPOINT ["/bin/convert.sh"]

