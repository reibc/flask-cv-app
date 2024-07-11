from flask_restx import Resource
from flask import abort
from .namespaces import api_namespace
from . import models
from .utils import get_cv_by_id


@api_namespace.route('/personal/<int:cv_id>')
@api_namespace.doc(
    params={'cv_id': 'CV ID'},
    description='Retrieve personal information from the CV by ID',
)
class PersonalResource(Resource):
    """Resource to handle personal information retrieval from a CV."""

    @api_namespace.marshal_with(models.personal_model)
    def get(self, cv_id):
        """Get personal information by CV ID."""
        cv = get_cv_by_id(cv_id)
        if not cv:
            abort(404, 'CV not found')
        return cv.get('personal')


@api_namespace.route('/experience/<int:cv_id>')
@api_namespace.doc(
    params={'cv_id': 'CV ID'},
    description='Retrieve work experience information from the CV by ID',
)
class ExperienceResource(Resource):
    """Resource to handle work experience retrieval from a CV."""

    @api_namespace.marshal_with(models.experience_model, as_list=True)
    def get(self, cv_id):
        """Get work experience by CV ID."""
        cv = get_cv_by_id(cv_id)
        if not cv:
            abort(404, 'CV not found')
        return cv.get('experience')


@api_namespace.route('/education/<int:cv_id>')
@api_namespace.doc(
    params={'cv_id': 'CV ID'},
    description='Retrieve education information from the CV by ID',
)
class EducationResource(Resource):
    """Resource to handle education information retrieval from a CV."""

    @api_namespace.marshal_with(models.education_model, as_list=True)
    def get(self, cv_id):
        """Get education information by CV ID."""
        cv = get_cv_by_id(cv_id)
        if not cv:
            abort(404, 'CV not found')
        return cv.get('education')


@api_namespace.route('/cv/<int:cv_id>')
@api_namespace.doc(
    params={'cv_id': 'CV ID'}, description='Retrieve full CV information by ID'
)
class CVResource(Resource):
    """Resource to handle full CV retrieval by ID."""

    @api_namespace.marshal_with(models.cv_model)
    def get(self, cv_id):
        """Get full CV by CV ID."""
        cv = get_cv_by_id(cv_id)
        if not cv:
            abort(404, 'CV not found')
        return cv
