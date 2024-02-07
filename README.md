# How to set up the template for the project:
(While using the terminal, please make sure that the directory is correct and Git Bash is being used.)
1. Run the template file present in the repository using this command in the terminal: python template.py
2. Before running the setup.py file, make the necessary changes in the following files, according to the need of the project:
>requirements.txt/requirements_dev.txt: Type in the names of the libraries with/without their specific versions.
>
>setup.cfg: Update the "YOUR_REPO_NAME" to your repo name or your project name.
>
>setup.py: Update the "REPO_NAME", "AUTHOR_USER_NAME", "SRC_REPO" and "AUTHOR_EMAIL" in accordance to the project's needs.
>
>tox.ini (OPTIONAL): Update the python versions in accordance to the needs of the project.
3. For the setup, run the following command in your terminal: bash init_setup.sh
4. From the ci.yml file, remove the first line and un-comment everything.
5. Create the files needed for the project. Go through Step 2 again to update the files as per the need of the project.
6. Commit the changes made to the repository for the workflow.
7. Check your workflow on your GitHub repository by clicking on the "Actions" tab.
