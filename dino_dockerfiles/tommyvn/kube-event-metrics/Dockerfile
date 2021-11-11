FROM alpine:3.6
ADD https://storage.googleapis.com/kubernetes-release/release/v1.7.4/bin/linux/amd64/kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl
RUN /usr/local/bin/kubectl config set-cluster proxy --server=http://127.0.0.1:8001
RUN /usr/local/bin/kubectl config set-context proxy --cluster=proxy
RUN /usr/local/bin/kubectl config use-context proxy
RUN apk add --no-cache python3
ADD requirements.txt event_metrics.py ./
RUN pip3 install -r requirements.txt
EXPOSE 8080
ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["/usr/bin/env", "python3", "event_metrics.py"]
