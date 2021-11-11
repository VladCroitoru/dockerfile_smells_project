FROM elixir:latest

# Install deps
RUN apt-get update \
 && apt-get install -y \
 	curl \
 	libpq-dev \
 	postgresql-client-9.4

# Get recent nodejs
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
 && apt-get install -y \
 	nodejs

# Set application dir
ENV APP_HOME /app

# Install phoenix
RUN mix archive.install --force \
	https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez

# Install hex and rebar
RUN mix local.hex --force
RUN mix local.rebar --force

# Create application directory, add application files there and set it as workdir
RUN mkdir $APP_HOME
WORKDIR $APP_HOME


# This is what remains to run in your project:
# ADD . $APP_HOME

# Install Elixir dependencies
# RUN mix deps.get --force

# Install node modules
# RUN npm set progress=false && npm install -g brunch && npm install

# Compile the app
# RUN mix do hex.info, compile


# Run server
EXPOSE 4000
CMD ["mix", "phoenix.server"]
