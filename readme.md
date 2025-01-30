# CV Assistant

## Getting Started

This guide will help you set up and run the CV Assistant application on your local machine.

### Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.8 or higher
- Git

### Installation

1. **Clone the Repository**

   Open your terminal and run:
   ```bash
   git clone https://github.com/segave/RRHH-assistant
   cd cv-assistant
   ```

2. **Install Pipenv**

   ```bash
   pip install -r requirements.txt
   ```

    **Add Pipenv to Your PATH** (if necessary):

   - On **Windows**:

     1. Open the Start Menu and search for "Environment Variables".

     2. Click on "Edit the system environment variables".

     3. In the System Properties window, click on the "Environment Variables" button.

     4. In the Environment Variables window, find the "Path" variable in the "System variables" section and select it, then click "Edit".

     5. Click "New" and add the path to your Python Scripts directory (usually `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<version>\Scripts`).

     6. Click "OK" to close all dialog boxes.



   - On **macOS/Linux**:

     1. Open your terminal.

     2. Add the following line to your shell configuration file (e.g., `.bashrc`, `.bash_profile`, or `.zshrc`):

        ```bash

        export PATH="$PATH:$(python -m site --user-base)/bin"

        ```

     3. Save the file and run:

        ```bash

        source ~/.bashrc  # or source ~/.bash_profile or source ~/.zshrc

        ```


3. **Create and Activate Virtual Environment with Pipenv**

   ```bash
   # Create virtual environment and install dependencies in the same directory as the project
   pipenv install

   # Activate the virtual environment
   pipenv shell
   ```

4. **Run the Application**

   Once you have activated the virtual environment with `pipenv shell`, you can run the application:
   ```bash
   # Make sure you are in the project directory
   streamlit run app.py
   ```

   The application will start and automatically open in your default web browser. If it doesn't open automatically, you can access it at:
   - Local URL: http://localhost:8501
   - Network URL: http://192.168.X.X:8501 (for accessing from other devices on your network)

## Environment Configuration

1. **Create Environment File**
   
   Copy the example environment file and fill in your credentials:
   ```bash
   cp .env.example .env
   ```

2. **Required Environment Variables**
   
   The following environment variables are required to run the application:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `PINECONE_API_KEY`: Your Pinecone API key for vector storage
   - `INDEX_NAME`: Name of your Pinecone index
   - `NAMESPACE`: Namespace for your vector storage

## Features and Functionality

### 1. User Profile and Job Description Setup
- Configure your recruiter profile with personal and company information
- Set up detailed job descriptions including:
  * Position title and department
  * Job requirements and responsibilities
  * Location and contract type
  * Salary range and benefits

### 2. CV Management
- Upload and process multiple CV documents
- Search through CVs using flexible criteria:
  * Search by candidate name
  * Search by specific skills or experience
  * Search by location
- View and analyze CV content directly in the application

### 3. Candidate Communication
- Generate personalized professional emails to candidates
- Features for email management:
  * Automatic email template generation based on job description
  * Personalization using candidate information
  * Preview emails before sending
  * Send emails directly from the application (requires email configuration)

### 4. Job Matching
- Compare candidate profiles with job requirements
- Get matching scores and detailed analysis
- Identify best-fit candidates for your positions

### 5. Email Configuration
- Set up email credentials for sending messages
- Support for Gmail and other email providers
- Secure credential management

### 6. AI Model Selection
- Choose between different AI models for processing
- Adjust settings for optimal performance

### 7. Email Generation
- Automated generation of personalized emails to candidates
- Templates for different types of communications
- Integration with job descriptions and candidate data

### 8. Email Management and Sending
- View and edit generated emails in a dedicated interface
- Edit recipients, subjects, and content before sending
- Direct email sending from the application
- Automatic tracking of email history
- Successfully sent emails are automatically archived

## Docker Installation

If you prefer to use Docker, you can run the application using our Docker image 
([available on Docker Hub](https://hub.docker.com/r/sergiogaliana/cv-assistant-langchain)):

### Option 1: Using Docker Run

1. **Pull the Docker image**:
   ```bash
   docker pull sergiogaliana/cv-assistant-langchain:latest
   ```

2. **Run the container with environment variables**:
   ```bash
   docker run -p 8501:8501 \
     -e OPENAI_API_KEY=your_key \
     -e PINECONE_API_KEY=your_key \
     -e INDEX_NAME=your_index \
     -e NAMESPACE=your_namespace \
     sergiogaliana/cv-assistant-langchain:latest
   ```

### Option 2: Using Docker Compose (Recommended)

1. **Create a docker-compose.yml file**:
   ```bash
   cp docker-compose.yml.example docker-compose.yml
   ```

2. **Add your environment variables**:
   Either edit the docker-compose.yml directly or create a .env file with your variables:
   ```env
   OPENAI_API_KEY=your_key
   PINECONE_API_KEY=your_key
   INDEX_NAME=your_index
   NAMESPACE=your_namespace
   ```

3. **Run the container**:
   ```bash
   docker-compose up
   ```

The application will be available at:
- Local URL: http://localhost:8501

More sections about configuration and usage will be added soon...