# Pull base image.
FROM jziub/ubuntu-java8:v2.0

# Copy the source code
RUN mkdir -p HTRC-Random-Sampling
COPY . ./HTRC-Random-Sampling

# Build
RUN cd ./HTRC-Random-Sampling && \
  mvn package

# Define default command.
CMD ["bash"]