# Use the official Ruby image
FROM ruby:2.6.10-alpine

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apk add --no-cache mariadb-connector-c-dev

# Install other dependencies
RUN apk add --no-cache build-base nodejs tzdata yarn

# Install bundler
RUN gem install bundler:2.4.7

# Copy the Gemfile and Gemfile.lock
COPY Gemfile Gemfile.lock ./

# Install gems
RUN bundle install

# Copy the application code
COPY . .

# Expose the Rails port
EXPOSE 3000

# Start the Rails server
CMD ["rails", "server", "-b", "0.0.0.0"]