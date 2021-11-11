FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#================================================================
# pip install required modules
#================================================================

RUN pip install --upgrade setuptools pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#==================================================
# Copy the latest code
#==================================================

RUN mkdir -p /fyle-slack-app
WORKDIR /fyle-slack-app
COPY . /fyle-slack-app

# Run pylint checks
RUN pylint --rcfile=.pylintrc fyle_slack_app/ fyle_slack_service/

# Expose server port
EXPOSE 8000

CMD /bin/bash run.sh