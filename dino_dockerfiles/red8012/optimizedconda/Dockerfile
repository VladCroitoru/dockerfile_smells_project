FROM clearlinux:base
ENV LANG=C.UTF-8

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

ADD https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh miniconda3.sh
RUN /bin/bash miniconda3.sh -b -p /conda && rm miniconda3.sh && echo export PATH=/conda/bin:$PATH >> .bashrc

ENV PATH="/conda/bin:${PATH}"
ENTRYPOINT ["/tini", "--"]
CMD ["/bin/bash"]
