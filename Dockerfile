# OS
FROM ubuntu:18.04 
# Update and install python and pip
RUN apt-get update && apt-get install -y python3 python3-pip sudo
# Adding User: Foedtra
RUN useradd -m foedtra
# Change the Owner home/foedtra
RUN chown -R foedtra:foedtra /home/foedtra/
# copying the current folder to /home/foedtra/app/
COPY --chown=foedtra . /home/foedtra/app/
# Use user foedtra
USER foedtra
# upgrade pip
RUN pip3 install --upgrade pip
# install the requirements
RUN cd /home/foedtra/app/ && pip3 install -r requirements.txt
# moving to working direktory
WORKDIR /home/foedtra/app
# exposing port 8080
EXPOSE 8080
# Set the entrypoint
ENTRYPOINT python3 main.py