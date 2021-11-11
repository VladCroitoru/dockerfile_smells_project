FROM gcr.io/cloud-solutions-images/jenkins-k8s-slave:latest
MAINTAINER Yosi Taguri yosi@taguri.com
ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
RUN gcloud components update
RUN apt-get update && apt-get install -y libcairo2-dev libjpeg62-turbo-dev libpango1.0-dev libgif-dev build-essential g++ && apt-get clean