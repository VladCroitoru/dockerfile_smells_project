FROM registry.devshift.net/fabric8-analytics/f8a-kronos-base:latest
LABEL maintainer="Avishkar Gupta <avgupta@redhat.com>"

# --------------------------------------------------------------------------------------------------
# install python packages
# --------------------------------------------------------------------------------------------------
COPY ./analytics_platform/kronos/requirements.txt /
# To accomodate for any additional requirements that are not
# added to base for some reason, ex: local testing.
RUN pip install -r /requirements.txt && rm /requirements.txt

# --------------------------------------------------------------------------------------------------
# copy src code and scripts into root dir /
# the rest_api.py code assumes this dir structure
# --------------------------------------------------------------------------------------------------
COPY ./analytics_platform/kronos/deployment/rest_api.py /rest_api.py
COPY ./analytics_platform/kronos/scripts/bootstrap_action.sh /
COPY ./tagging_platform/helles/scripts/bootstrap_action.sh /helles_bootstrap_action.sh
COPY ./evaluation_platform/uranus/scripts/bootstrap_action.sh /uranus_bootstrap_action.sh
COPY ./analytics_platform /analytics_platform
COPY ./tagging_platform /tagging_platform
COPY ./evaluation_platform /evaluation_platform
COPY ./util /util
COPY ./analytics_platform/kronos/src/config.py.template /analytics_platform/kronos/src/config.py

# --------------------------------------------------------------------------------------------------
# add entrypoint scripts for the container
# --------------------------------------------------------------------------------------------------
ADD ./analytics_platform/kronos/scripts/entrypoint.sh /bin/entrypoint.sh

ENTRYPOINT ["/bin/entrypoint.sh"]
