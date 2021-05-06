from app import db
from sqlalchemy import Float,Column,Integer,String,ForeignKey,DateTime,Time,Boolean
from datetime import datetime as dt


# No CPF, tive que tirar o "unique", pois estava dando erro quando registrava mais de um procedimento para o mesmo CPF

class Exame(db.Model):
    __tablename__ = "exame"

    id          = Column(Integer, primary_key=True)
    video       = Column(String,nullable=False)
    nome        = Column(String,nullable=False)
    cpf         = Column(String(14),nullable=False)
    password    = Column(String,nullable=False)
    pdf         = Column(String,nullable=False)
    procedimento= Column(String,nullable=False)
    data        = Column(DateTime,nullable=False)

    def __init__(self, video,nome,cpf,password,pdf,procedimento, data = dt.now()):
        self.video    = video   
        self.nome     = nome    
        self.password = password
        self.cpf = cpf
        self.pdf = pdf
        self.procedimento = procedimento
        self.data = data
    
    def url_video(self):
        return f"https://drive.google.com/uc?id={self.video}"

    def url_pdf(self):
        return f"https://drive.google.com/uc?export=download&id={self.pdf}"

    def __repr__(self):
        return "<Exame %r>" % self.id
    
    def save(self):
        if self.id is None:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        if self.id is not None:
            db.session.delete(self)
        db.session.commit()
    
    def data_formatada(self):
        return self.data.strftime("%d/%m/%Y")

class DadosPacientePressao(db.Model):
    __tablename__ = "dadosPacientePressao"

    id                    = Column(Integer, primary_key=True)
    cpf                   = Column(String(14),ForeignKey('exame.cpf'),nullable=False)
    data                  = Column(DateTime,nullable=False)
    pressao_sistolica     = Column(Float)
    pressao_diastolica    = Column(Float)
    pulso                 = Column(Float)
    Exame                 = db.relationship("Exame",foreign_keys=cpf)

    def __init__(self, cpf,pressao_sistolica=0, pressao_diastolica=0, pulso=0, data = dt.now()):
        self.cpf = cpf
        self.pressao_sistolica = pressao_sistolica
        self.pressao_diastolica = pressao_diastolica
        self.pulso = pulso
        self.data = data

    def __repr__(self):
        return "<DadosPacientePressao %r>" % self.id
    
    def save(self):
        if self.id is None:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        if self.id is not None:
            db.session.delete(self)
        db.session.commit()
    
    def data_formatada(self):
        return self.data.strftime("%d/%m/%Y")

class DadosPacienteGlicemia(db.Model):
    __tablename__ = "dadosPacienteGlicemia"

    id                    = Column(Integer, primary_key=True)
    cpf                   = Column(String(14),ForeignKey('exame.cpf'),nullable=False)
    data                  = Column(DateTime,nullable=False)
    glicemia              = Column(Float)
    cafe                  = Column(Boolean)
    almoco                = Column(Boolean)
    janta                 = Column(Boolean)
    Exame                 = db.relationship("Exame",foreign_keys=cpf)

    def __init__(self, cpf, glicemia=0, cafe=0, almoco=0, janta=0, data = dt.now()):
        self.cpf = cpf
        self.glicemia = glicemia
        self.cafe = cafe
        self.almoco = almoco
        self.janta = janta
        self.data = data

    def __repr__(self):
        return "<DadosPacienteGlicemia %r>" % self.id
    
    def save(self):
        if self.id is None:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        if self.id is not None:
            db.session.delete(self)
        db.session.commit()
    
    def data_formatada(self):
        return self.data.strftime("%d/%m/%Y")


