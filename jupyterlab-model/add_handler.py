
from sqlalchemy.orm import sessionmaker
from notebook.base.handlers import APIHandler


from wtforms.fields import IntegerField, StringField
from wtforms.validators import Required
from wtforms_tornado import Form

from .db_link import Model, engine

class TypesForm(Form):
    model_name = StringField(validators=[Required])
    code = StringField(validators=[Required])
    permission = IntegerField(validators=[Required])
    desc = StringField(validators=[Required])


class Add_models(APIHandler):
    """
    定义添加models类
    """

    def initialize(self):
        session = sessionmaker(bind=engine)
        self.session = session()

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        """
        前端获取数据,执行sql语句保存数据库
        """
        form = TypesForm(self.request.arguments)
        # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
        if form.validate():
            models = Model()
            models.Model_Name = form.data['model_name']
            models.Code = form.data['code']
            models.Permission = form.data['permission']
            models.Desc = form.data['desc']
            self.session.add(models)
            self.session.commit()
            return self.write('Save OK')
        else:
            # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@')
            return self.write(form.errors)




add_handler = r'/lab/api/addmodel'