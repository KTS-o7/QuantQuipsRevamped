# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt


# update and install tkinter
RUN apt update -y
RUN apt install python3-tk -y
# Copy the rest of the application code to the working directory
COPY . /app

# Expose the port on which the Streamlit app will run
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
