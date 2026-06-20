# Lab 1 Dockerfile — fill in the blanks
# Use the slide from Module 3 as reference

# Step 1: Choose a base image
# Hint: use python:3.11-slim
FROM ___

# Step 2: Set the working directory inside the container
# Hint: use /app
WORKDIR ___

# Step 3: Copy requirements.txt and install dependencies
# (copy requirements BEFORE the rest of the code — why?)
COPY ___ .
RUN pip install -r requirements.txt

# Step 4: Copy the rest of the code
COPY ___ .

# Step 5: Tell Docker how to run your script
CMD ["___", "___"]
