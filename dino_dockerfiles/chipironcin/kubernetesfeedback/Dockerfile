FROM bitnami/base-ubuntu:14.04
MAINTAINER Jorge Marin <jorge@bitnami.com>

COPY feedbackScript.sh feedbackScript.sh

CMD echo "Welcome to the feedback app client for the Bitnami Kubernetes Workshop" && \
    echo "Please execute the following from your server to begin" && \
    echo "Kubernetes - kubectl exec -it <pod_name> ./feedbackScript.sh" && \
    echo "Docker - docker exec -it <container_id> ./feedbackScript.sh" && \
    tail -f /dev/null
