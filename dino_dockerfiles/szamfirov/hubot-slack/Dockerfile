FROM node:latest

# Install base packages
RUN npm install -g hubot coffee-script

# Create new hubot and setup for slack.
RUN cd /root && \
  hubot --create myhubot && \
  cd myhubot && \
  npm install hubot-slack --save && \
  npm install hubot-reactions --save && \
  npm install && \
  echo '["hubot-reactions"]' > external-scripts.json


# Set environment variables
ENV TZ Europe/Berlin

# Run hubot("-a slack")
WORKDIR /root/myhubot
ENTRYPOINT ["/root/myhubot/bin/hubot", "-a", "slack"]
CMD ["-n", "hubot"]
