
from .db_link import User_Model_Type, Model, Type, engine
from sqlalchemy.orm import sessionmaker
# from tornado.web import RequestHandler
from notebook.base.handlers import APIHandler
from tornado import web


class Type_Handler(APIHandler):

    def initialize(self):
        sess = sessionmaker(bind=engine)
        self.db = sess()

    @web.authenticated
    def get(self, *args, **kwargs):
        # 创建字典
        t_dict = {}

        # 获取type表的信息
        types = self.db.query(Type)

        f_list = types.filter(Type.Father_ID == None)

        # 确定哪些为父级， 哪些为子集
        # 父级列表
        t_list = []
        for f_type in f_list:

            # 将子集 放在对应的父级下面
            # 获取每个父级ID 对应的子集信息
            child_list = types.filter(Type.Father_ID == f_type.TID)
            # 子集信息列表
            child_ = []
            for child_type in child_list:

                # 模型信息列表
                model_list = []
                # 获取当前类型的模型信息， ID， 限制为十条
                models = self.db.query(User_Model_Type).filter(User_Model_Type.Type_ID == child_type.TID).limit(10)
                for model in models:
                    m_id = model.Model_ID

                    # 获取对应的模型信息
                    m_desc = self.db.query(Model).filter(Model.MID == m_id).first()
                    model_list.append({'mid': m_desc.MID, 'mname': m_desc.Model_Name})
                # 讲模型列表添加至子类型列表
                child_.append({'cid': child_type.TID, 'cname': child_type.Type_name,'mdesc':model_list})
            # 讲子类型添加至父类列表
            t_list.append({'father_id': f_type.TID, 'type_name': f_type.Type_name, 'child': child_})
        t_dict['type'] = t_list
        # 返回最终数据
        return self.write(t_dict)


type_handler = r'/lab/api/type'

