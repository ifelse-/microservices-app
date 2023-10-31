# This line specifies the base image for your Docker container, which is Python 3.11 slim version.
FROM 3.11-slim

# Set the working directory within the container to /backend.
WORKDIR /backend

# Expose port 5051 for external access to your Flask application.
EXPOSE 5050

# Copy Pipfile and Pipfile.lock from your local directory to the /backend directory in the container.
COPY Pipfile Pipfile.lock ./

# Install 'pipenv' within the container to manage Python dependencies.
RUN pip install pipenv

# Generate a 'requirements.txt' file using 'pipenv' which represents your project's dependencies.
RUN pipenv requirements > requirements.txt

# Install the Python dependencies listed in the 'requirements.txt' file.
RUN pip install -r requirements.txt

# Copy the entire content of your local directory to the /backend directory in the container.
COPY . ./

# Define the command to run your Flask application when the container starts.
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0", "--port=5050"]