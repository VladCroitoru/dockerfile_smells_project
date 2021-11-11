FROM eboraas/debootstrap:minbase-jessie
LABEL maintaner="Aldi Dipasanta"

# Based on the Ed Boraas's Debian Jessie
# Based on the manually-generated base image (i.e. a minbase debootstrap), simply ensure
# everything is up to date, providing a current base image for other Docker images without
# needing to frequently regenerate the manual base image

# Set apt-get to automatically retry if a package download fails
RUN echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/99AcquireRetries

# The ADD lines below ensurs that the docker build cache is invalidated if the contents of the
# mirror and/or security archive changes, necessary for apt-get to be actually executed.
# As an added bonus, you can use it to check which version of the upstream archives that
# an image was built against.
ADD http://httpredir.debian.org/debian/project/trace/ftp-master.debian.org /etc/trace_ftp-master.debian.org
ADD http://security.debian.org/project/trace/security-master.debian.org /etc/trace_security-master.debian.org
RUN apt-get update && apt-get -y dist-upgrade && apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
