# Use the official Python image as the base image
FROM python:3.8

# Set environment variables for Flask
ENV FLASK_APP=products.py
ENV FLASK_RUN_HOST=0.0.0.0

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Copy the entire project directory into the container
COPY . /app

# Expose the port that Flask will run on
EXPOSE 5000

#ENTRYPOINT ["gunicorn"]
#For production deployments, you should use a production-ready server like Gunicorn or uWSGI.


# Define the command to run your Flask app
#CMD ["flask", "run"]
# Define the command to run your Flask app with Gunicorn
CMD ["gunicorn", "products:app", "-b", "0.0.0.0:5000"]





