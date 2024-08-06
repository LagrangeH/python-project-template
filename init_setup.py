# TODO: the module is in progress
import logging
import subprocess
from collections.abc import Callable
from typing import Any


class InputValuesSingleton[T: object]:
    _instance: T | None = None
    _values: dict[str, Any] = {}

    def __new__(cls: type[T]) -> T:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def new_value(input_message: str
                  ) -> Callable[[Callable[[T], Any]], property]:

        def decorator(func: Callable[[T], Any]) -> property:
            prop_name: str = func.__name__

            def wrapper(self: T) -> Any:
                if prop_name not in self._values:
                    logging.info(input_message)
                    print(input_message)
                    self._values[prop_name] = input()
                return self._values[prop_name]

            return property(wrapper)

        return decorator

    @new_value("Enter your Python version: ")
    def python_version(self) -> property: ...


class SetupManager:
    @property
    def _all_changes_committed(self) -> bool:
        try:
            # Run 'git status --porcelain' command
            result = subprocess.run(['git', 'status', '--porcelain'],
                                    capture_output=True, text=True, check=True)

            # If the output is empty, all changes are committed
            return len(result.stdout.strip()) == 0

        except subprocess.CalledProcessError:
            print("Error: Not a git repository or git command not found.")
            return False

    def abort(self):
        pass

    @property
    def python_version(self) -> str:
        logging.info("Enter your Python version: ")
        return input()

    def run(self) -> None:
        try:
            subprocess.run('poetry --version')
        except FileNotFoundError:
            logging.error('Poetry is not installed. Please, install Poetry ('
                          'https://python-poetry.org/docs) and try again')
        finally:
            self.abort()
            return

        logging.info("Enter your Python version: ")
        PYTHON_VERSION: str = input()
        subprocess.run(f'poetry env use {PYTHON_VERSION}', shell=True)

        your_name: str = input()

        # create virtual environment
        # install dependencies
        # create config files
        # create tests folder
        # create scripts folder
        # create src folder
        # create .gitignore file
        logging.info('Successful')


def main() -> None:
    try:
        setup_manager = SetupManager()
        setup_manager.run()
    except (KeyboardInterrupt, SystemExit, GeneratorExit):
        logging.error(f"Setup interrupted")


if __name__ == '__main__':
    logging.StreamHandler.terminator = ""
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(message)s',
        datefmt='%H:%M:%S'
    )
    main()
