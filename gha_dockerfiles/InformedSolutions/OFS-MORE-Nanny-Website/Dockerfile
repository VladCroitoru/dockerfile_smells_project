FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
ARG PROJECT_SETTINGS

# If dev env install additional packages
RUN  if [ "`echo $PROJECT_SETTINGS | rev | cut -c -3 | rev`" = "dev" ]; then \
       apt-get update; \
       apt-get install -y build-essential graphviz vim tree git tig; \
     fi

RUN apt-get update && \
        apt-get install -y \
                netcat \
                git \
        && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /source/
WORKDIR /source
RUN pip install -r requirements.txt

ADD . /source/

RUN chmod +x /source/docker-entrypoint.sh
EXPOSE 8000
CMD ["/source/docker-entrypoint.sh"]
