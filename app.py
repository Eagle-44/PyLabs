import os
from os.path import join, dirname, abspath
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, post_load, ValidationError
from marshmallow_enum import EnumField
from enum import Enum

app = Flask(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Companies(Enum):
    Bosch = 0
    Makita = 1
    Arsenal = 2
    DniproM = 3


class WoodworkingMachine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    manufacture_company = db.Column(db.Enum(Companies))
    power = db.Column(db.Integer, nullable=False)
    rpm = db.Column(db.Integer, nullable=False)
    volume_per_sec = db.Column(db.Float, nullable=False)
    purpose = db.Column(db.String(50), nullable=False)

    def __init__(self, name: str = "", model: str = "", price: float = 0.0, manufacture_company: Companies = None,
                 power: int = 0, rpm: int = 0, volume_per_sec: float = 0.0, purpose: str = ""):
        self.name = name
        self.model = model
        self.price = price
        self.manufacture_company = manufacture_company
        self.power = power
        self.rpm = rpm
        self.volume_per_sec = volume_per_sec
        self.purpose = purpose


class WoodworkingMachineSchema(ma.Schema):

    name = fields.Str(validate=validate.Length(min=1, max=32))
    model = fields.Str(validate=validate.Length(min=1, max=20))
    price = fields.Float(validate=validate.Range(min=0.0, max=9999.0))
    manufacture_company = EnumField(Companies)
    power = fields.Int(validate=validate.Range(min=0, max=9999))
    rpm = fields.Int(validate=validate.Range(min=0, max=9999))
    volume_per_sec = fields.Float(validate=validate.Range(min=0.0, max=9999.0))
    purpose = fields.Str(validate=validate.Length(min=1, max=50))

    @post_load
    def make_wood_machine(self, data, **kwargs):
        return WoodworkingMachine(**data)


woodworkingMachine_schema = WoodworkingMachineSchema()
woodworkingMachines_schema = WoodworkingMachineSchema(many=True)


# endpoint to create new Woodworking Machine
@app.route("/WoodMachine", methods=["POST"])
def add_wood_machine():
    try:
        wood_machine = woodworkingMachine_schema.load(request.json)
        db.session.add(wood_machine)
    except ValidationError as err:
        abort(400, err)
    db.session.commit()
    return jsonify(request.json)


# endpoint to show all Woodworking Machine
@app.route("/WoodMachine", methods=["GET"])
def get_wood_machine():
    all_wood_machines = WoodworkingMachine.query.all()
    result = woodworkingMachines_schema.dump(all_wood_machines)
    return jsonify(result)


# endpoint to get Woodworking Machine detail by id
@app.route("/WoodMachine/<id>", methods=["GET"])
def wood_machine_detail(id):
    wood_machine = WoodworkingMachine.query.get(id)
    if wood_machine is None:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)
    return woodworkingMachine_schema.jsonify(wood_machine)


# endpoint to update Woodworking Machine
@app.route("/WoodMachine/<id>", methods=["PUT"])
def wood_machine_update(id):
    wood_machine = WoodworkingMachine.query.get(id)
    if not wood_machine:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)
    try:
        wood_machina = woodworkingMachine_schema.load(request.json)
        wood_machine.name = wood_machina.name
        wood_machine.model = wood_machina.model
        wood_machine.price = wood_machina.price
        wood_machine.manufacture_company = wood_machina.manufacture_company
        wood_machine.power = wood_machina.power
        wood_machine.rpm = wood_machina.rpm
        wood_machine.volume_per_sec = wood_machina.volume_per_sec
        wood_machine.purpose = wood_machina.purpose
    except ValidationError as err:
        abort(400, err)
    db.session.commit()
    return woodworkingMachine_schema.jsonify(wood_machine)


# endpoint to delete Woodworking Machine
@app.route("/WoodMachine/<id>", methods=["DELETE"])
def wood_machine_delete(id):
    wood_machine = WoodworkingMachine.query.get(id)
    if wood_machine is None:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)
    db.session.delete(wood_machine)
    db.session.commit()

    return woodworkingMachine_schema.jsonify(wood_machine)


if __name__ == '__main__':
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root1:2222@localhost:3306/iotdb'
        db.create_all(app=app)
    except Exception as e:
        print(e)
        print("CANNOT CONNECT TO DB(CHECK config.py SQLALCHEMY_DATABASE_URI IF THIS FIELD IS OK) CREATING SQLITE DB")
        dbdir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(dbdir, 'db.sqlite')
        db.create_all(app=app)
    app.run(debug=True)