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

More sections about configuration and usage will be added soon...