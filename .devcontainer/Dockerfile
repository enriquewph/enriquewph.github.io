ARG VARIANT="3.0.5"
ARG NODE_VERSION="14"
FROM ruby:${VARIANT}

# Update the package lists and install Node.js
RUN apt-get update && \
    curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - && \
    apt-get install -y nodejs

# Optionally set a non-root user
RUN groupadd --gid 1000 node \
    && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

# Install dependencies for Jekyll
RUN gem install bundler jekyll

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash instead of sh
ENV SHELL /bin/bash

