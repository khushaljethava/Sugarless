from run import db
class SymptomCheckerModel(db.Model):
    __tablename__ = 'SymptomChecker'

    SC_question_id = db.Column(db.Integer, primary_key=True)
    SC_questions = db.Column(db.String(120))



    def __init__(self, SC_question_id, SC_questions):
        self.SC_question_id = SC_question_id
        self.SC_questions = SC_questions

    def json(self):
        return{
        'Questions': self.SC_questions
        }


    @classmethod
    def find_by_Question_id(cls, SC_question_id):
        return cls.query.filter_by(SC_question_id=SC_question_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
