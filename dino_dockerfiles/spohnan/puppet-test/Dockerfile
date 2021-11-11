FROM centos:latest

# Set working dir as variable
ENV module_dir /module

# Update the base system and install main packages, then clean up
RUN yum -y update && \
    yum -y install rubygems ruby-devel rubygem-nokogiri libxml2-devel \
                   libxslt-devel augeas-devel git gcc gcc-c++ make tar && \
    yum clean all

ADD Gemfile /

# Configure to never install a ruby gem docs, install gems and clean up afterwards
RUN printf "gem: --no-rdoc --no-ri" >> /etc/gemrc && \
    gem install json -v '1.8.3' && \
    gem install bundler && \
    bundler install --clean --system --gemfile /Gemfile

# Directory to load module under test
VOLUME ${module_dir}
WORKDIR ${module_dir}

# Run tests
CMD rm -rf Gemfile.lock && \
    bundle exec rake spec_clean && \
    bundle exec rake spec
