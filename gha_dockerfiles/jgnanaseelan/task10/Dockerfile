FROM centos7:latest
MAINTAINER Sander van Vugt <mail@sandervanvugt.nl>

# mandatory K8S labels
LABEL io.k8s.description="Simple web app" \
      io.k8s.display-name="My simple app" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="html,apache"

RUN yum install -y httpd && yum clean all -y

EXPOSE 8080

# Copy the S2I scripts from the github repo to the $STI_SCRIPTS_PATH in the image
COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# open security to allow files to be copied to /var/www/html
# needed because openshift runs containers as non-root
RUN chmod -R a+rwx /var/www/htdocs

# Set the default CMD to print the usage of this image
CMD $STI_SCRIPTS_PATH/usage
