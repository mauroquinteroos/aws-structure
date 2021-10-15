from flask import request, make_response, jsonify
from app.auth.models import Record, User
from app.auth import utils


def get_access():
    """"
        @url '/api/auth/login'
        Obtener la autorización de los módulos y vistas a las que el usuario tiene acceso
    """
    try:
        auth_data = utils.get_auth_data(request)
        if auth_data:
            token = auth_data['token']
            platform_id = auth_data['platform_id']

            active_record = Record.query.filter(Record.token == token).filter(Record.estado == 1).first()
            user = User.query.filter(User.idusuario == active_record.idusuario).first()

            session_token = utils.generate_session(user.idusuario)
            module_list  = utils.get_views_modules(user.idusuario, platform_id)

            if session_token and module_list:
                response = jsonify({
                    'success': True,
                    'data': {
                        'token': session_token,
                        'modules': module_list
                    }
                })
                return make_response(response, 200)
            else:
                raise Exception('No se obtuvo ninguna acceso a la plataforma')
        else:
            raise Exception('Error al obtener el token y el ID de la plataforma')
    except Exception as err:
        print('Error:', err)

        response = jsonify({
            'success': False,
            'data': [],
            'message': 'Error al iniciar sesión'
        })
        return make_response(response, 500)
