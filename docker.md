# first time install
sudo pacman -S docker docker-compose
sudo systemctl enable --now docker

//run once! this is not a sevice yet
sudo systemctl status docker
    ● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: disabled)
     Active: active (running) since Sun 2026-06-28 09:22:08 CEST; 1min 11s ago



#New Project
git clone https://github.com/Hapkin/*
cd *
nano Dockerfile
#######
####### example dockerfile for static site that runs a local http server

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Make the shell scripts executable
RUN chmod +x build.sh main.sh

# Install any needed packages specified in requirements.txt, if exists
# RUN pip install --no-cache-dir -r requirements.txt  # Uncomment if you have Python dependencies

# Run the main shell script by default when the container runs
CMD ["./main.sh"]



############
####
docker build -t static_site .
docker run -d -p 8888:8888 static_site