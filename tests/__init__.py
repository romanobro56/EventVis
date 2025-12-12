# The files might not be in their final directories.
from typing import Collection
import unittest
import sys, os
sys.path.append(os.path.abspath('../backend'))

from backend.app import User
from backend.db.database_client import *

from unittest.mock import Mock
import mongomock
import json