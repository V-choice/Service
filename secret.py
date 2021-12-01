#나중에 gitignore에 추가해야함.

from dotenv import load_dotenv
import os
#나중에 gitignore에 추가해야함.
load_dotenv()
db_pw = os.environ.get("pw")
secret_key = os.environ.get("secret")
