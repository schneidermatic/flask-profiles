from init.app import app,db

from models import *
from controllers import *

if __name__ == '__main__':
  app.run()