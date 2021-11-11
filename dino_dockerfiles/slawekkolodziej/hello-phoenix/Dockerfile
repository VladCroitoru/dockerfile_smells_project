FROM slawekkolodziej/phoenix-base

ADD . $APP_HOME

# Install Elixir dependencies
RUN mix deps.get --force

# Install node modules
RUN npm set progress=false && npm install -g brunch && npm install

# Compile the app
RUN mix do hex.info, compile

# Run server
EXPOSE 4000
CMD ["mix", "phoenix.server"]
