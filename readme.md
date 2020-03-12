+ All projects should have a virtual environment dedicated just for that project, including plugins and add-ons
+ virtual envs should be located right next to the project folder, so that it's easy to know why it's thert
+ in order to install virtual env, type this
    ```bash
    pip3 install virtualenv     # install virtual environment plugin
    virtualenv my_venv          # create virtual env for this project
    source my_venv/bin/activate   # activate your newly found god powers!
    ```
+ install all we need

+ migrations should be included in your project ... makes sense
    https://stackoverflow.com/questions/28035119/should-i-be-adding-the-django-migration-files-in-the-gitignore-file