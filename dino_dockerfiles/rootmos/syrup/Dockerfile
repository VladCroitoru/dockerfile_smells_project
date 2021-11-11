FROM unbalancedparentheses/erlang:17.4

COPY rebar.config /root/rebar.config

RUN mkdir /root/src
COPY src /root/src

RUN mkdir /root/rel
COPY rel/reltool.config /root/rel/reltool.config
RUN mkdir /root/rel/files
COPY rel/files /root/rel/files

WORKDIR /root
RUN rebar get-deps compile generate

CMD rel/syrup/bin/syrup foreground
