FROM python:3.9-slim
# Set working directory
WORKDIR /app
# Copy the current directory contents into the container
COPY . /app
# Install needed packages
RUN pip install --no-cache-dir -r requirements.txt
# Make port 5000 available to the world
EXPOSE 5000
# Define environment variable
ENV PORT 5000
# Run app.py when the container launches
CMD ["python", "app.py"]
