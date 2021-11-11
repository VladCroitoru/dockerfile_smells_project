# Pull the basic alpine image
# This will form the build environment
FROM alpine:latest

# Install git
# No need to update beforehand, latest versions are streamed directly because of '--no-cache'
RUN apk --no-cache add git

# Set the ENV variable(s)
ENV BUILD_FOLDER=/build
ENV APP_FOLDER=/usr/src/app
ENV REPO_BRANCH=master
ENV REPO_URL=https://github.com/cobalamin/drip-downloader.git

# Create the BUILD_FOLDER and set it as the WORKDIR
RUN mkdir $BUILD_FOLDER
WORKDIR $BUILD_FOLDER

# Clone the git repo, but only the last 1 commits from a single branch
RUN git clone --depth=1 --branch $REPO_BRANCH --single-branch $REPO_URL

# Use sed to remove the '# ruby 2.0.0' line and everything after ',' on all lines
# Removing the 'gem' versions prevents odd dependency errors when running 'bundle install' below
RUN cd $BUILD_FOLDER/drip-downloader && \
	sed -i '/#/d' Gemfile && \
	sed -i 's/,.*//' Gemfile

# Copy the app files to the APP_FOLDER
# The APP_FOLDER will be copied over to the final image in a later step
RUN mkdir -p $APP_FOLDER && \
    cp $BUILD_FOLDER/drip-downloader/Gemfile $APP_FOLDER && \
    cp $BUILD_FOLDER/drip-downloader/drip.rb $APP_FOLDER

# Pull the latest ruby:alpine image
# This will form the final image
FROM ruby:alpine3.7

# Set the ENV variable(s)
ENV APP_FOLDER=/usr/src/app

# Create the APP_FOLDER and set it as the WORKDIR
RUN mkdir -p $APP_FOLDER
WORKDIR $APP_FOLDER

# Copy from APP_FOLDER on the build image to APP_FOLDER on the final image
# Note that these paths should be exactly the same between the two images
COPY --from=0 $APP_FOLDER $APP_FOLDER

# Install the gem files
RUN bundle install

# Setup a directory for downloads
# When building the actual container, map a host volume to this volume
RUN mkdir /data
VOLUME /data
WORKDIR /data

# Set the default app to run and command to execute
ENTRYPOINT ["ruby"]
CMD ["/usr/src/app/drip.rb"]
