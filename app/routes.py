from flask_restx import Namespace, Resource, fields
from flask import abort

from .utils import get_cv_by_id

api_namespace = Namespace('api', description='API operations')

# Models
personal_model = api_namespace.model('Personal', {
    'name': fields.String(required=True, description='The name of the person'),
    'email': fields.String(required=True, description='The email of the person'),
    'phone': fields.String(description='The phone number of the person'),
    'address': fields.String(description='The address of the person')
})

experience_model = api_namespace.model('Experience', {
    'position': fields.String(required=True, description='The job title'),
    'company': fields.String(required=True, description='The company name'),
    'start_date': fields.String(required=True, description='The start date of the job'),
    'end_date': fields.String(description='The end date of the job'),
    'description': fields.String(description='The job description')
})

education_model = api_namespace.model('Education', {
    'degree': fields.String(required=True, description='The degree obtained'),
    'institution': fields.String(required=True, description='The institution name'),
    'start_date': fields.String(required=True, description='The start date of the education'),
    'end_date': fields.String(description='The end date of the education')
})

cv_model = api_namespace.model('CV', {
    'id': fields.Integer(required=True, description='The CV ID'),
    'personal': fields.Nested(personal_model, description='Personal information'),
    'experience': fields.List(fields.Nested(experience_model), description='Work experience'),
    'education': fields.List(fields.Nested(education_model), description='Education history')
})

@api_namespace.route('/personal/<int:cv_id>')
@api_namespace.doc(params={'cv_id': 'CV ID'}, description='Retrieve personal information from the CV by ID')
class PersonalResource(Resource):
    @api_namespace.marshal_with(personal_model)
    def get(self, cv_id):
        cv = get_cv_by_id(cv_id)
        if not cv:
            abort(404, 'CV not found')
        return cv.get('personal')

@api_namespace.route('/experience/<int:cv_id>')
@api_namespace.doc(params={'cv_id': 'CV ID'}, description='Retrieve work experience information from the CV by ID')
class ExperienceResource(Resource):
    @api_namespace.marshal_with(experience_model, as_list=True)
    def get(self, cv_id):
        cv = get_cv_by_id(cv_id)
        if not cv:
            abort(404, 'CV not found')
        return cv.get('experience')

@api_namespace.route('/education/<int:cv_id>')
@api_namespace.doc(params={'cv_id': 'CV ID'}, description='Retrieve education information from the CV by ID')
class EducationResource(Resource):
    @api_namespace.marshal_with(education_model, as_list=True)
    def get(self, cv_id):
        cv = get_cv_by_id(cv_id)
        if not cv:
            abort(404, 'CV not found')
        return cv.get('education')

@api_namespace.route('/cv/<int:cv_id>')
@api_namespace.doc(params={'cv_id': 'CV ID'}, description='Retrieve full CV information by ID')
class CVResource(Resource):
    @api_namespace.marshal_with(cv_model)
    def get(self, cv_id):
        cv = get_cv_by_id(cv_id)
        if not cv:
            abort(404, 'CV not found')
        return cv


