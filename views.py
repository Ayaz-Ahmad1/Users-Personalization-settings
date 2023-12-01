# routes.py
from flask import jsonify, request
from models import db, User, PersonalizationSettings
from sqlalchemy.exc import IntegrityError

def configure_routes(app):
    # Route to get personalization settings for a user
    @app.route('/personalization_settings/<int:user_id>', methods=['GET'])
    def get_personalization_settings(user_id):
        try:
            # Retrieve the user with the given ID or return a 404 error
            user = User.query.get_or_404(user_id)

            # Check if user exists
            if user:
                settings = user.personalization_settings
                # Return personalization settings as JSON
                return jsonify(
                    {
                        'error' : None,
                        'data' : {
                            'theme': settings.theme,
                            'language': settings.language,
                            'notifications': settings.notifications
                        }
                    }
                )
            else:
                # Return a 404 error if personalization settings not found for the user
                return jsonify({
                    'data': None,
                    'error': {
                        'message': f'Personalization settings not found for user id {user_id}'
                    }}), 404
        except Exception as e:
            # Return a 404 error if the user with the given ID is not found
            return jsonify({
                'data' : None,
                'error': {
                'message': f'User with id: {user_id} not found.'
                }}), 404

    # Route to save personalization settings for a user
    @app.route('/personalization_settings/<int:user_id>', methods=['POST'])
    def save_personalization_settings(user_id):
        # Get JSON data from the request
        data = request.get_json()
        try:
            # Create a new user with the given ID and add it to the session
            user = User(id=user_id)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            # Return a 400 error if there's a duplicate user ID
            return jsonify(
                {
                'data' : None,
                'error': {'message': 'Duplicate user ID'}}
            ), 400

        # Create personalization settings for the user
        settings = PersonalizationSettings(
            theme=data.get('theme', 'default_theme'),
            language=data.get('language', 'default_language'),
            notifications=data.get('notifications', False),
            user=user
        )

        # Add personalization settings to the session and commit changes
        db.session.add(settings)
        db.session.commit()

        # Return success message
        return jsonify(
            {
                'error' : None,
                'data':{'message': 'Personalization settings saved successfully'}
            }
        )

    # Route to delete personalization settings for a user
    @app.route('/personalization_settings/<int:user_id>', methods=['DELETE'])
    def delete_personalization_settings(user_id):
        try:
            # Retrieve the user with the given ID or return a 404 error
            user = User.query.get_or_404(user_id)
            settings = user.personalization_settings

            # Check if settings exist
            if settings:
                # Delete user and settings from the session and commit changes
                db.session.delete(user)
                db.session.delete(settings)
                db.session.commit()
                # Return success message
                return jsonify(
                    {
                        'error' : None,
                        'data':  {'message': f'Personalization settings for user id {user_id} deleted successfully'}
                    }
                )
            else:
                # Return a 404 error if personalization settings not found for the user
                return jsonify(
                    {'data' : None,
                    'error':
                    {'message': 'Personalization settings not found'}}
                ), 404
        except Exception as e:
            # Return a 404 error if the user with the given ID is not found
            return jsonify(
                {   'data' : None,
                    'error': {'message': f'Cannot delete user that does not exist.'}
                     }
            ), 404

