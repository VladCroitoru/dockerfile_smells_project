FROM codekoala/arch:latest
MAINTAINER Matthew Wardrop <mister.wardrop@gmail.com>

# Setup environment
ENV BUDGETLESS_DB=/data/budgetless.db
ENV BUDGETLESS_LOG=/data/budgetless.log
EXPOSE 5000
RUN chpasswd <<< "root:budgetless"

# Install dependencies
RUN pacman --noconfirm -Syu
RUN pacman --noconfirm -S python-flask python-pip python-pandas python-numpy \
	python-sqlalchemy gcc cython python-sympy fcron syslog-ng python-pytz
RUN pip install gunicorn mintapi plotly==1.9.6 parampy
RUN pip install git+https://github.com/matthewwardrop/budgetless.git

# Set up automatic budget updates
RUN printf "#!/bin/sh\nbudgetless ${BUDGETLESS_DB} sync" > /etc/cron.hourly/budgetless_update
RUN chmod +x /etc/cron.hourly/budgetless_update

# Ensure that data directory exists
RUN mkdir -p $(dirname $BUDGETLESS_DB)

# Run cron daemon and deploy budgetless server
CMD syslog-ng && fcron && budgetless ${BUDGETLESS_DB} deploy &> ${BUDGETLESS_LOG} & /bin/bash
