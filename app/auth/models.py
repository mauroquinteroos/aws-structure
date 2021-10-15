from app import db


users_views = db.Table(
    'usuario_vista',
    db.Column('idusuario', db.Integer, db.ForeignKey('usuario.idusuario')),
    db.Column('idvista', db.Integer, db.ForeignKey('vista.idvista')),
    info={'bind_key': 'base'}
)


class Module(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'modulo'

    idmodulo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    idplataforma = db.Column(db.Integer)
    views = db.relationship('View', back_populates='module')


class User(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'usuario'

    idusuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    correo = db.Column(db.String(60))
    tipo = db.Column(db.Integer)
    views = db.relationship('View', secondary=users_views, backref='users')


class View(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'vista'

    idvista = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    idmodulo = db.Column(db.Integer, db.ForeignKey('modulo.idmodulo'))
    module = db.relationship('Module', back_populates='views')


class Record(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'bitacora'

    idbitacora = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text)
    idusuario = db.Column(db.Integer)
    flg_tipo = db.Column(db.Integer) # 1: inicio de sesión, 2: cambio de contraseña
    estado = db.Column(db.Integer) # 1: activo, 2: inactivo


class Session(db.Model):
    __tablename__ = 'sesion_usuario'

    idsesion = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text)
    idusuario = db.Column(db.Integer)
    estado = db.Column(db.Integer) # 1: activo, 0: inactivo
