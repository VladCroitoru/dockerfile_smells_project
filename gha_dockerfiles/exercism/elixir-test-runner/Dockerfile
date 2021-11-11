FROM hexpm/elixir:1.12.1-erlang-24.0.1-ubuntu-focal-20210325

# Install SSL ca certificates
RUN apt-get update && \
  apt-get install bash jo -y

# Create appuser
RUN useradd -ms /bin/bash appuser

# Get the source code
WORKDIR /opt/test-runner
COPY . .

# Compile the formatter
WORKDIR /opt/test-runner/exercism_test_helper
RUN mix local.rebar --force
RUN mix local.hex --force
RUN mix deps.get
RUN MIX_ENV=test mix compile
RUN mix test --no-compile

# Build the escript
RUN MIX_ENV=prod mix escript.build
RUN mv exercism_test_helper /opt/test-runner/bin

USER appuser

WORKDIR /opt/test-runner
ENTRYPOINT ["/opt/test-runner/bin/run.sh"]
