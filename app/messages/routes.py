import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import pymongo
from flask import Response, request, json

from . import messages
from run import app

mongouri = "mongodb://" + app.config['MONGODB_UNAME'] + ":" + app.config['MONGODB_PASS'] + "@" + app.config['MONGODB_HOST'] + ":" + str(app.config['MONGODB_PORT']) + "/?authSource=admin"

@messages.route('/add', methods=['POST'])
def add():
    try:
        mc = pymongo.MongoClient(mongouri)
    except Exception, e:
        return Response(json.dumps({'server_resp': "Could not connect to Mongo: %s" % e}), status=500, mimetype='application/json')
    try:
        collection = mc[app.config['DBS_NAME']]['test']
        message = {"message": request.form['message']}
        collection.insert(message);
        mc.disconnect();
        return Response(json.dumps({'server_resp': "Success"}), status=200, mimetype='application/json')
    except Exception, e:
        return Response(json.dumps({'server_resp': "Mongo error: %s" % e}), status=500, mimetype='application/json')

