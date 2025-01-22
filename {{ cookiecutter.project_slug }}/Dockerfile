FROM docker.io/nvidia/cuda:12.0.0-base-ubuntu22.04

# Arguments
# - USER_UID: User ID of the user 'app'
ARG USER_UID=1000
# - USER_GID: Group ID of the user 'app'
ARG USER_GID=1000

# Change working directory
WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    bash \
    fish \
    python3.11 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user called app and switch to it
# USe the same UID and GID as in the .env file to avoid permission issues
RUN groupadd -g $USER_GID app && useradd -u $USER_UID -g $USER_GID -m app
USER app
ENV PATH="/home/app/.local/bin:${PATH}"

# Configure Python

# Copy the requirements.txt file first for better cache on later pushes

# Copy all other files
COPY . /app
