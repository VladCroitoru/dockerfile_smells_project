# use the ui container to pull in webpack artifacts
FROM helxplatform/helx-ui:2.0.0-dev.7 as builder

FROM python:3.9.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Least privilege: Run as a non-root user.
ENV USER appstore
ENV APP_HOME /usr/src/inst-mgmt
ENV HOME /home/$USER
ENV UID 1000

RUN mkdir $APP_HOME

RUN adduser --disabled-login --home $HOME --shell /bin/bash --uid $UID $USER && \
   chown -R $UID:$UID $HOME

RUN set -x && apt-get update && \
	chown -R $UID:$UID $APP_HOME && \
	apt-get install -y build-essential git xmlsec1
   
WORKDIR $APP_HOME
COPY . .
COPY --from=builder /usr/share/nginx/html/index.html ./appstore/frontend/templates/frontend
COPY --from=builder /usr/share/nginx/static/ ./appstore/frontend/static

RUN make install

RUN chown -R 1000:0 /usr/src/inst-mgmt
RUN chmod -R g+w /usr/src/inst-mgmt
EXPOSE 8000
CMD ["make","start"]
