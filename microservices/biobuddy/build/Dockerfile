# Use a PyTorch base image with CUDA support
FROM python:3.11

# Install Python 3.11 and curl
RUN apt-get update && apt-get install -y curl python3-pip

# Set a working directory
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/

# Install dependencies
RUN python3.11 -m pip install --upgrade pip
RUN python3.11 -m pip install --default-timeout=100 -r requirements.txt

# Now copy the rest of the application files into the container
COPY ./biobuddy /app/biobuddy

# Set the command to run the FastAPI app
ENTRYPOINT ["uvicorn", "biobuddy.api:app"]