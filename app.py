from flask import Flask


app = Flask(__name__)

from controllers.orders.controller import *
from controllers.analytics.controller import *
from controllers.offers.controller import *
from controllers.player.controller import *

