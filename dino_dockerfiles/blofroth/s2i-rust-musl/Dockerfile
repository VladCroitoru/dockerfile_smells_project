
ARG TOOLCHAIN=nightly
FROM ekidd/rust-musl-builder:${TOOLCHAIN}

MAINTAINER Björn Löfroth <bjorn.lofroth@gmail.com>

LABEL io.k8s.description="Platform for building Rust Applications" \
     io.k8s.display-name="Rust Musl S2I Builder" \
     io.openshift.expose-services="8000:http" \
     io.openshift.tags="rust" \
     io.openshift.s2i.scripts-url="image:///usr/libexec/s2i" 

COPY ./s2i/bin/ /usr/libexec/s2i

# to 'Support Arbitrary User IDs'
# https://docs.openshift.org/latest/creating_images/guidelines.html#openshift-specific-guidelines
USER root
RUN chgrp -R 0 /home/rust /usr/libexec/s2i && \
    chmod -R g=u /home/rust /usr/libexec/s2i

# unsure, according to documentation in parent image, this should be 
# the uid of the rust user
USER 1000

CMD ["/usr/libexec/s2i/usage"]
