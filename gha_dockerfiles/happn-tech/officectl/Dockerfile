# ================================
# Build image
# ================================
FROM swift:5.4-focal as build

# Install OS updates and required packages
RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true \
    && apt-get -q update \
    && apt-get -q dist-upgrade -y \
    && apt-get install -y libldap2-dev libncurses-dev libssl-dev pkg-config zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up a build area
WORKDIR /build

# First just resolve dependencies.
# This creates a cached layer that can be reused as long as your
# Package.swift/Package.resolved files do not change.
COPY ./Package.* ./
RUN swift package resolve

# Copy entire repo into container
COPY . .

# Build everything, with optimizations and test discovery
RUN swift build --enable-test-discovery -c release

# Switch to the staging area
WORKDIR /staging

# Copy main executable to staging area
RUN cp "$(swift build --package-path /build -c release --show-bin-path)/officectl" ./

# Copy any resouces from the public directory and views directory if the directories exist
# Ensure that by default, neither the directory nor any of its contents are writable.
RUN [ -d /build/Public ]    && { mv /build/Public    ./Public    && chmod -R a-w ./Public;    } || true
RUN [ -d /build/Resources ] && { mv /build/Resources ./Resources && chmod -R a-w ./Resources; } || true


# ================================
# Run image
# ================================
FROM swift:5.4-focal-slim

# Make sure all system packages are up to date and install required libs
RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true \
    && apt-get -q update \
    && apt-get -q dist-upgrade -y \
    && apt-get install -y libldap-2.4-2 libncurses6 libncursesw6 libssl1.1 zlib1g \
    && rm -rf /var/lib/apt/lists/*

# TODO: Find how to do this properly!
ADD https://ca.1e42.net/happn_Root_CA.crt           /usr/local/share/ca-certificates/happn_Root_CA.crt
ADD https://ca.1e42.net/happn_Intermediate_CA_2.crt /usr/local/share/ca-certificates/happn_Intermediate_CA_2.crt
ADD https://ca.1e42.net/happn_Intermediate_CA_5.crt /usr/local/share/ca-certificates/happn_Intermediate_CA_5.crt
RUN /usr/sbin/update-ca-certificates

# Create a vapor user and group with /app as its home directory
RUN useradd --user-group --create-home --system --skel /dev/null --home-dir /app vapor

# Switch to the new home directory
WORKDIR /app

# Copy built executable and any staged resources from builder
COPY --from=build --chown=vapor:vapor /staging /app

# Ensure all further commands run as the vapor user
USER vapor:vapor

# Let Docker bind to port 8080
EXPOSE 8080

# Start the Vapor service when the image is run, default to listening on 8080 in production environment
ENTRYPOINT ["./officectl"]
CMD ["server", "serve", "--env", "production", "--hostname", "0.0.0.0", "--port", "8080"]
