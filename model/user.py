from run import db
from passlib.hash import pbkdf2_sha256 as sha256


class UserModel(db.Model):
    __tablename__ = 'users'
    u_id = db.Column(db.Integer, primary_key=True)
    u_username = db.Column(db.String(120), unique=True, nullable = False)
    u_password = db.Column(db.String(120), nullable=False)
    u_fullname = db.Column(db.String(120),nullable = False)
    u_email = db.Column(db.String(120), unique=True, nullable = False)
    u_mobile = db.Column(db.BIGINT(), unique=True, nullable = False)
    u_gender = db.Column(db.String(120))
    u_age = db.Column(db.Integer())


    PreexistingCondition = db.relationship('PreConditionModel', lazy='dynamic')
    FamilyHistory = db.relationship('FamilyHistoryModel', lazy='dynamic')
    LabReports = db.relationship('LabReportModel', lazy='dynamic')
    LabReportUpload = db.relationship('LabReportUploadModel', lazy='dynamic')
    RetinaReport = db.relationship('RetinaUploadModel',lazy='dynamic')
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, u_username):
        return cls.query.filter_by(u_username=u_username).first()

    @classmethod
    def find_by_mobile(cls, u_mobile):
        return cls.query.filter_by(u_mobile=u_mobile).first()

    @classmethod
    def find_by_email(cls, u_email):
        return cls.query.filter_by(u_email=u_email).first()

    @classmethod
    def find_by_id(cls, u_id):
        return cls.query.filter_by(u_id = u_id).first()

    @classmethod
    def find_by_ids(cls, u_id):
        return cls.query.filter_by(u_id = u_id)

    def json(self):
        return{
        'u_id' : self.u_id,
        'u_username' : self.u_username,
        'u_password' : self.u_password,
        'u_fullname' : self.u_fullname,
        'u_email' : self.u_email,
        'u_mobile' : self.u_mobile,
        'u_gender' : self.u_gender,
        'u_age': self.u_age,

        }

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password,hash):
        return sha256.verify(password,hash)


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_token'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls,jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)
