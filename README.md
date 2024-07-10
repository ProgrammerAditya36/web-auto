
# Project Setup Script

This script automates the setup of various types of web development projects, including Frontend, Django, React, Node.js, and MERN stack projects. It also provides functionality for creating React components, deploying React projects to GitHub Pages, setting up Tailwind CSS, and copying custom hooks.

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
python script.py <project_type> [project_name] [additional_options]
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