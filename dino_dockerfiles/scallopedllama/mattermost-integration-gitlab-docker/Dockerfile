FROM ubuntu:14.04

MAINTAINER Joe Balough, <jbb5044@gmail.com>

# Install dependencies for mattermost-integration-gitlab
RUN apt-get update
RUN apt-get install -y python python-pip python-dev build-essential git-core

# Install mattermost-integration-gitlab
RUN pip install git+https://github.com/NotSqrt/mattermost-integration-gitlab

# Run the integration as a service after making sure that the webhook url variable is set
CMD if [ "${MATTERMOST_WEBHOOK_URL}" = "" ]; then echo "FAILED. MATTERMOST_WEBHOOK_URL environment variable is not set."; echo "Consult README for more information."; exit 1; fi; mattermost_gitlab "${MATTERMOST_WEBHOOK_URL}"

