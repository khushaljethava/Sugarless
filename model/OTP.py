from run import db

class OTPModel(db.Model):

    __tablename__ = 'Temp_OTP'

    u_id = db.Column(db.Integer, primary_key=True)
    u_mobile = db.Column(db.BIGINT())
    otp = db.Column(db.Integer)




    @classmethod
    def find_by_mobile(cls, u_mobile):
        return cls.query.filter_by(u_mobile=u_mobile).first()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
