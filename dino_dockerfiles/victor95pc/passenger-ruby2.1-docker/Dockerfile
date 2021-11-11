# === 1 ===
# Use phusion/passenger-full as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/passenger-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/passenger-ruby21:0.9.15

# Set environment variables.
ENV HOME /home/app/webapp
ENV RAILS_ENV production


# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# === 2 ===
# Start Nginx / Passenger
RUN rm -f /etc/service/nginx/down


# === 3 ====
# Remove the default site
RUN rm /etc/nginx/sites-enabled/default

# Add the nginx info
ADD nginx /etc/nginx/sites-enabled/webapp.conf
ADD rails-env /etc/nginx/main.d/rails-env.conf

# === 4 ====
# Setup SSH server
RUN rm -f /etc/service/sshd/down
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



