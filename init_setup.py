import logging
import subprocess


def setup() -> None:
    # Preparing for setup
    logging.StreamHandler.terminator = ""
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(message)s',
        datefmt='%H:%M:%S'
    )
    try:
        subprocess.run('poetry --version')
    except FileNotFoundError:
        logging.error('Poetry is not installed. Please, install Poetry ('
                      'https://python-poetry.org/docs) and try again')
        return

    logging.info("Enter your Python version: ")
    python_version: str = input()

    your_name: str = input()

    # create virtual environment
    # install dependencies
    # create config files
    # create tests folder
    # create scripts folder
    # create src folder
    # create .gitignore file
    logging.info('Successful')


if __name__ == '__main__':
    try:
        setup()
    except (KeyboardInterrupt, SystemExit, GeneratorExit):
        logging.error(f"Setup interrupted")
