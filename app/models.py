from flask_restx import fields
from .namespaces import api_namespace

# Models
personal_model = api_namespace.model(
    'Personal',
    {
        'name': fields.String(
            required=True, description='The name of the person'
        ),
        'email': fields.String(
            required=True, description='The email of the person'
        ),
        'phone': fields.String(description='The phone number of the person'),
        'address': fields.String(description='The address of the person'),
    },
)

experience_model = api_namespace.model(
    'Experience',
    {
        'position': fields.String(required=True, description='The job title'),
        'company': fields.String(
            required=True, description='The company name'
        ),
        'start_date': fields.String(
            required=True, description='The start date of the job'
        ),
        'end_date': fields.String(description='The end date of the job'),
        'description': fields.String(description='The job description'),
    },
)

education_model = api_namespace.model(
    'Education',
    {
        'degree': fields.String(
            required=True, description='The degree obtained'
        ),
        'institution': fields.String(
            required=True, description='The institution name'
        ),
        'start_date': fields.String(
            required=True, description='The start date of the education'
        ),
        'end_date': fields.String(description='The end date of the education'),
    },
)

cv_model = api_namespace.model(
    'CV',
    {
        'id': fields.Integer(required=True, description='The CV ID'),
        'personal': fields.Nested(
            personal_model, description='Personal information'
        ),
        'experience': fields.List(
            fields.Nested(experience_model), description='Work experience'
        ),
        'education': fields.List(
            fields.Nested(education_model), description='Education history'
        ),
    },
)
