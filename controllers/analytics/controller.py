from app import app

from flask import request, jsonify
from controllers.analytics.schemas import GetAnalyticsRequestSchema, GetAnalyticsResponseSchema
from controllers.analytics.service import AnalyticsService

from signature_service import SignatureService


@app.route('/mocker/analytics', methods=['POST'])
def get_analytics():
    GetAnalyticsRequestSchema.model_validate_json(request.data)
    analytics_service = AnalyticsService()
    signature_service = SignatureService()
    analytics = analytics_service.get_analytics(request.data, signature_service.create_signature(request.data))
    GetAnalyticsResponseSchema.model_validate(analytics)
    return jsonify(analytics)
