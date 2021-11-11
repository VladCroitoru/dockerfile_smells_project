FROM google/debian:wheezy

ADD . /docker-registry

RUN /docker-registry/build.sh

# This is the default port that docker-registry is listening on.
# Needs to be set into 5000 or the value of REGISTRY_PORT environment variable
# if the latter one is set.
EXPOSE 5000

# Credentials. Use --volumes-from gcloud-config (google/cloud-sdk).
VOLUME ["/.config"]

# These should be set if credentials are obtained with google/cloud-sdk.
ENV OAUTH2_CLIENT_ID 32555940559.apps.googleusercontent.com
ENV OAUTH2_CLIENT_SECRET ZmssLNjJy2998hD4CTg2ejr2
ENV USER_AGENT "Cloud SDK Command Line Tool"

CMD cd /docker-registry && ./setup-configs.sh && exec ./run.sh
