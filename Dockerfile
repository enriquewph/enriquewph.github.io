FROM jekyll/jekyll

# expose 4000
EXPOSE 4000

# Preinstall gems
COPY Gemfile Gemfile.lock /srv/jekyll/
WORKDIR /srv/jekyll
RUN chmod -R 777 /srv/jekyll && bundle install

# Set the default shell to bash instead of sh
ENV SHELL /bin/bash

# CMD
CMD ["jekyll", "serve"]