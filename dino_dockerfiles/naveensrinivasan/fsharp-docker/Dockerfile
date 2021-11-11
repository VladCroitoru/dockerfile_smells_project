FROM debian:wheezy
MAINTAINER Naveen Srinivasan <nsrinivasan1976@gmail.com>
#based on dockerfile by Michael Friis <friism@gmail.com>

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb http://download.mono-project.com/repo/debian alpha main" | tee /etc/apt/sources.list.d/mono-xamarin-alpha.list \
&& apt-get update \
&& apt-get install -y mono-complete 

# Installing FSharp

RUN apt-get install -y autoconf libtool pkg-config make git && \
    git clone https://github.com/fsharp/fsharp && \
    cd fsharp && ./autogen.sh --prefix /usr && make && make install && \
    cd / && rm -rf fsharp
ENTRYPOINT ["/bin/bash"]
CMD ["fsharpi"]
