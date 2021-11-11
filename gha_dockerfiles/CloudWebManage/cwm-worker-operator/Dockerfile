FROM python:3-alpine@sha256:bd7f0719874c7de4ca47418de143ab4de79731dc0b01fdcf2425b8a32f4823ce
RUN apk update && apk add --no-cache git curl nfs-utils
RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl" &&\
    chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl &&\
    kubectl version --client &&\
    curl -Ls https://get.helm.sh/helm-v3.2.4-linux-amd64.tar.gz -ohelm.tar.gz &&\
    tar -xzvf helm.tar.gz && mv linux-amd64/helm /usr/local/bin/helm &&\
    chmod +x /usr/local/bin/helm &&\
    rm -rf linux-amd64 && rm helm.tar.gz &&\
    helm version
RUN pip install --upgrade pip
RUN mkdir -p /usr/local/src/cwm-worker-operator
WORKDIR /usr/local/src/cwm-worker-operator
COPY requirements.txt requirements-cwm-worker-deployment.txt ./
RUN pip install -r requirements.txt
COPY setup.py .
COPY cwm_worker_operator ./cwm_worker_operator
RUN pip install -e .
ENV PYTHONUNBUFFERED=no
ENTRYPOINT ["cwm_worker_operator"]
