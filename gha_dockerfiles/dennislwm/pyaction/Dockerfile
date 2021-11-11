#----------------------
# From linux base image
FROM python:3.7-slim as step1

#----------------------
# Update system
#   Clean up temp files
FROM step1 as step2-a
RUN apt-get update \
  && apt-get clean && rm -rf /tmp/* /var/tmp/*
# RUN apt-get --assume-yes 

#--------------------------------------------------
# GitHub Action ignores WORKDIR, ENTRYPOINT and CMD
#   Copy files from source to container
FROM step1 as step2-b
COPY . /app

#--------------------------
# Merge step2-a and step2-b
#   Set working dir
#   Install app dependencies
FROM step2-a as final
COPY --from=step2-b /app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

#-------------------------------------
# Set default script and arguments
#   This can be overridden at runtime
ENTRYPOINT [ "python3" ]
