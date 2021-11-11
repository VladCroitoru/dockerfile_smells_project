FROM jfloff/alpine-python:2.7-slim

MAINTAINER Signiant DevOps <devops@signiant.com>

# Add all files starting with report
ADD report* /
ADD command_runner.sh /command_runner.sh

RUN pip install boto3
RUN chmod a+x /report* /command_runner.sh

ENTRYPOINT ["/command_runner.sh"]

CMD ["-h"]
