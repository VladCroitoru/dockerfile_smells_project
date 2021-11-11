FROM telegraf:alpine
LABEL maintainer="José Antonio Perdiguero López <perdy@perdy.io>"

ENV APP=barrenero-telegraf

# Install system dependencies
ENV RUNTIME_PACKAGES python3
RUN apk --no-cache add $RUNTIME_PACKAGES

# Create project dirs
RUN mkdir -p /srv/apps/$APP
WORKDIR /srv/apps/$APP

# Install python requirements
COPY Pipfile Pipfile.lock /srv/apps/$APP/
RUN python3 -m pip install --no-cache-dir --upgrade pip pipenv && \
    pipenv install --system --deploy --ignore-pipfile && \
    rm -rf $HOME/.cache/pip/*

COPY . /srv/apps/$APP/

ENTRYPOINT ["telegraf"]
