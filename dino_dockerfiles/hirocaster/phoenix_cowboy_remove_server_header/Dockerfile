FROM hirocaster/docker-elixir

RUN mkdir /root/workspace

WORKDIR /root/workspace

ENTRYPOINT [ \
  "prehook", \
    "elixir -v", \
    "mix deps.get", "--", \
  "switch", \
    "shell=/bin/sh", "--", \
  "codep", \
    "mix test" \
]
