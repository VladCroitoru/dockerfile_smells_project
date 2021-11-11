FROM ubuntu
RUN apt update && apt -y install \
    curl \
    && rm -rf /var/lib/apt/lists
#WORKDIR /root
RUN curl -L https://github.com/luvit/lit/raw/master/get-lit.sh | sh
# manual:
#RUN curl -L 'https://github.com/luvit/luvi/releases/download/v2.10.1/luvi-regular-Linux_x86_64' -o luvi && chmod +x luvi && ls -lah
#RUN file luvi
#RUN curl -L 'https://lit.luvit.io/packages/luvit/lit/v3.8.1.zip' -o lit.zip && /root/luvi lit.zip -- make lit.zip lit luvi && rm -f lit.zip
#RUN ./lit make lit://luvit/luvit luvit luvi

LABEL org.opencontainers.image.source "https://github.com/j2ghz/discordbot-lua"

ADD . /app

WORKDIR /app
RUN /lit install

WORKDIR /app/src
ENTRYPOINT ["/luvit", "./main.lua"]
