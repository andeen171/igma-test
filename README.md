# Igma's Test

## Set up

1. Download this repository using git clone:

    ```
    git clone https://github.com/andeen171/igma-test
    ```

2. Set up a virtual environment. You may need to
   [install virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and/or
   [install Python](https://www.python.org/downloads/). I didn't use [poetry](https://python-poetry.org/) this time
   because it conflicts with the [Fish](https://fishshell.com/) shell I am currently using.
   Once you've got everything installed, you can create a virtualenv with the
   following command:

    ```
    virtualenv -p python3 venv
    ```

   Then, you can run the virtual environment with the command:

    ```
    source venv/bin/activate
    ```

3. Next, install the project requirements:

    ```
    pip install -r requirements.txt
    ```

4. Now, run this command to migrate the database
    ```
    python manage.py migrate
    ```

5. Then you can run the application using:

    ```
    python manage.py runserver
    ```

6. Or run the automated tests:
    ```
    python manage.py test
    ```