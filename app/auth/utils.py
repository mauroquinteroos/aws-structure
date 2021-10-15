from app import db
from app.config import AUTH_PREFIX
from utils import methods
from app.auth.models import User, Module, Session
from app.auth.schemas import ModuleSchema


def get_auth_data(request):
    """"
        Obtener el token del header y el ID de la plataforma del body
    """
    auth_token = request.headers.get('Authorization', False)
    platform_id = request.json.get('plataforma_id', False)
    if AUTH_PREFIX in auth_token and platform_id:
        token = split_auth_header(auth_token)
        return {
            'token': token,
            'platform_id': platform_id,
        }
    else:
        return False

def split_auth_header(auth_token):
    array_auth = auth_token.split(' ')
    return array_auth[1]

def get_views_modules(user_id, platform_id):
    """"
        Realizar las consultas de los módulos y vistas a las que el usuario tiene acceso
    """
    user = User.query.filter(User.idusuario == user_id).first()
    modules = Module.query.filter(Module.idplataforma == platform_id).all()
    data = []

    for module in modules:
        views_module = list(filter(lambda view: view.idmodulo == module.idmodulo, user.views))
        module_serialize = ModuleSchema(module, views_module).dump()
        data.append(module_serialize)
    return data

def generate_session(user_id):
    """"
        Crear sesion en la base de datos para validar el acceso del usuario
    """
    try:
        token = methods.generate_token()
        new_session = Session(
            token=token,
            idusuario=user_id,
            estado=1
        )

        db.session.add(new_session)
        db.session.commit()
        return new_session.token
    except Exception as err:
        print(err)
        return False
