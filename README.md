
# Project Setup Script

This script automates the setup of various types of web development projects, including Frontend, Django, React, Node.js, and MERN stack projects. It also provides functionality for creating React components, deploying React projects to GitHub Pages, setting up Tailwind CSS.

Usage:

    python web_auto.py <project_type> [project_name] [additional_options]

## Project Types:

- ```fe```  Create a simple frontend web project. 
- ```django```        Create a Django project with optional app name.
- ```react```         Create a React project using Vite.
- ```react-ts```      Create a TypeScript React project using Vite.
- ```node```          Create a Node.js project with Express.
-mern          Create a MERN stack project with both backend (Node.js) and frontend (React).

## Additional Options:

 -   ```-start```         Start the development server for the selected project type.
-    ```-cc```            Create a React component with optional directory and CSS flag.
-   ```-mp```            Deploy a React project to GitHub Pages with optional page name.
-   ```-tw```            Set up Tailwind CSS for a React project.   

## Examples:





## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ProgrammerAditya36/web-auto.git
    cd web-auto
    ```

2. **Install the Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python web_auto.py <project_type> [project_name] [additional_options]
```
Create a frontend project 
    
```python web_auto.py -fe myfrontendapp```  

Create a Django project with an app

```python web_auto.py -django mydjangoproject mydjangoapp```  

Create a React project  
```python web_auto.py -react my-react-app```

Create a TypeScript React project  
    ```python web_auto.py -react-ts my-react-ts-app```

Create a Node.js project  
    ```python web_auto.py -node my-node-app```

Create a MERN stack project  
    ```python web_auto.py -mern my-mern_project```

Start the development server for a React project  
    ```python web_auto.py -react -start```

Create a React component with a directory and CSS  
    ```python web_auto.py -react -cc MyComponent -css```

Deploy a React project to GitHub Pages  
    ```python web_auto.py -react -mp mypage```

Set up Tailwind CSS for a React project  
    ```python web_auto.py -react -tw```


## Environment Variables

For deploying React projects to GitHub Pages, you need to set the following environment variables:

- `GITHUB_TOKEN`: Your GitHub personal access token.
- `USERNAME`: Your GitHub username.
- `HOMEPAGE`: The homepage URL for your GitHub Pages.

You can set these variables in your shell profile (e.g., `.bashrc`, `.zshrc`, etc.):

```bash
export GITHUB_TOKEN=your_github_token
export USERNAME=your_github_username
export HOMEPAGE=https://your_github_username.github.io/
```


## Making the Scripts Global
To make the best use of the file make them global so that they can be accessed from any directory.
#### Linux

1. **Move the script to a directory in your PATH:**

    ```bash
    sudo mv web_auto.py /usr/local/bin/web_auto
    sudo chmod +x /usr/local/bin/web_auto
    ```

2. **Verify the command:**

    ```bash
    web_auto 
    ```

 Windows

1. **Add the script directory to your PATH:**

    - Right-click on 'This PC' or 'Computer' on the desktop or in File Explorer.
    - Select 'Properties'.
    - Click on 'Advanced system settings'.
    - Click on the 'Environment Variables' button.
    - In the 'System variables' section, find the 'Path' variable and select it. Click 'Edit'.
    - Click 'New' and add the directory where `web_auto.py` is located.
    - Click 'OK' to close all dialog boxes.

2. **Create a batch file to run the script:**

    - Open Notepad and paste the following lines, replacing `path_to_script` with the actual path:

        ```batch
        @echo off
        python path_to_script\web_auto.py %*
        ```

    - Save the file as `web_auto.bat` in a directory that is in your PATH.

3. **Verify the command:**

    ```cmd
    web_auto 
    ```

By following these steps, you can run the script globally on your system by using the `web_auto` command.