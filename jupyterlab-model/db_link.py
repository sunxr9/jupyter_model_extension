
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from .conf import DB_HOST, DB_NAME, DB_PASSWD, DB_USER, DB_CHARTSET

database = 'mysql://%s:%s@%s/%s?%s' % (DB_USER, DB_PASSWD, DB_HOST, DB_NAME, DB_CHARTSET)

engine = sqlalchemy.create_engine(database, encoding='utf-8', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

base = declarative_base()


class User(base):

    __tablename__ = 'users'

    UID = Column(Integer, primary_key=True, autoincrement=True, comment=u'用户ID')
    Foreign_ID = Column(Integer, comment=u'映射ID')

    # Users = relationship('UserModelType')

    def __str__(self):
        return '%s' % self.UID


class Model(base):

    __tablename__ = 'models'

    MID = Column(Integer, primary_key=True, comment=u'模型ID', autoincrement=True)
    Model_Name = Column(String(128), comment=u'模型类名')
    Code = Column(String(2048), comment=u'代码存储')
    Permission = Column(Integer, default=1, comment=u'权限认证')
    Desc = Column(String(128), comment=u'详细信息')

    def __str__(self):
        return self.Model_Name


class Type(base):

    __tablename__ = 'types_model'

    TID = Column(Integer, primary_key=True, autoincrement=True, comment=u'类型ID')
    Type_name = Column(String(32), nullable=False, comment=u'类型名')
    Father_ID = Column(Integer, comment=u'父类ID')

    def __str__(self):
        return self.Type_name


class User_Model_Type(base):

    __tablename__ = 'user_model_type'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    User_ID = Column(Integer, ForeignKey('users.UID'), comment=u'用户ID', nullable=False, primary_key=True)
    Model_ID = Column(Integer, ForeignKey("models.MID"), comment=u'模型ID', nullable=False, primary_key=True)
    Type_ID = Column(Integer, ForeignKey('types_model.TID'), comment=u'类型ID', nullable=False, primary_key=True)


    def __str__(self):
        return "User_Model_Type(user=%s,model=%s,type=%s)" % (self.User_ID, self.Model_ID, self.Type_ID)


def create_DB():
    print(engine)
    base.metadata.create_all(engine)

