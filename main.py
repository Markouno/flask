import flask
from flask import jsonify, request
from flask.views import MethodView
from models import Advertise, Session


app = flask.Flask('app')


class UserView(MethodView):


    def get(self, advertise_id):
        with Session() as session:
            advertise = session.get(Advertise, advertise_id)
            return jsonify({'title': advertise.title,
                            'description': advertise.description,
                            'created_date': advertise.created_date,
                            'author': advertise.author})

    def post(self):
        user_data = request.json
        with Session() as session: 
            new_ad = Advertise(**user_data)
            session.add(new_ad)
            session.commit()
            return jsonify({'title': new_ad.title})

    def delete(self, advertise_id):
        with Session() as session:
            ad = session.get(Advertise, advertise_id)
            session.delete(ad)
            session.commit()
            return jsonify({'status': 'ok'})
        


user_view = UserView.as_view('user_view')
app.add_url_rule('/ad/<int:advertise_id>', view_func=user_view, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/ad', view_func=user_view, methods=['POST'])

app.run()