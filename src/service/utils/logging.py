import yaml
from pathlib import Path
from loguru import logger


def setup_logging(config_path: str = "config/logging_config.yaml",
                  env: str = "default"):
    """
    Sets up logging configuration using the specified YAML configuration file and environment.

    Parameters:
    config_path (str): The path to the YAML configuration file. Defaults to "config/logging_config.yaml".
    env (str): The environment key to use from the configuration file. Defaults to "default".

    Returns:
    logger: The configured logger instance.

    Raises:
    FileNotFoundError: If the configuration file is not found at the specified path.
    ValueError: If the specified environment is not found in the configuration file.
    """
    config_path = Path(config_path)

    if not config_path.is_file():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    if env not in config:
        raise ValueError(f"Environment '{env}' not found in config file")

    logger.configure(**config[env])

    return logger
