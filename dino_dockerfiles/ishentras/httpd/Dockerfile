FROM centos:latest
MAINTAINER IshentRas william17.burton@gmail.com

RUN yum install -y epel-release && yum install -y nginx --setopt=tsflags=nodocs && yum clean all
# change default port to 8080 and forward request and error logs to docker log collector (STDOUT)
RUN sed -i 's/80/8080/g;s/pid.*/pid \/tmp\/nginx.pid\;/g;s/worker_processes.*/worker_processes 1\;/' /etc/nginx/nginx.conf && \
    rm -rf /var/lib/nginx && \
    mkdir -p /var/lib/nginx/tmp && \
    chmod 777 /var/lib/nginx/tmp /var/log/nginx && \
    ln -sf /proc/1/fd/1 /var/log/nginx/access.log && \
    ln -sf /proc/1/fd/1 /var/log/nginx/error.log

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
