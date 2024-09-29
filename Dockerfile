FROM public.ecr.aws/amazonlinux/amazonlinux:latest
# Download updates and install python3, pip and vim
RUN yum update -y 
RUN yum install python3 -y
RUN yum install python3-pip -y

# Declaring working directory in our container
WORKDIR /opt/apps/custom_gps_api

COPY requirements.txt .

# Install all requrements for our app
RUN pip3 install -r requirements.txt

# Copy source files to $WORKDIR
COPY . . 

# Expose container port to outside host
EXPOSE 5000



# Run the application
CMD [ "gunicorn", "main:app", "--bind", "0.0.0.0:5000", "-k", "gevent", "-w", "1" ]