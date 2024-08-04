"""Bot settings and environment variables"""
import os
from dotenv import load_dotenv


load_dotenv()

SOME_ENV_VAR = os.getenv('SOME_ENV_VAR')
