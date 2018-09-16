#! -*- encoding: utf-8 -*-

from notebook.utils import url_path_join as ujoin

from .add_handler import Add_models, add_handler
from .type_handler import Type_Handler, type_handler


def setup_handler(web_app):
    pass
    '''
    Setup all of the model command handlers.
    '''
    model_hamdler = [
            (add_handler, Add_models),
            (type_handler, Type_Handler)
        ]

    base_url = web_app.settings['base_url']
    model_hamdlers = [(ujoin(base_url, x[0]), x[1]) for x in model_hamdler]

    print(model_hamdlers)

    web_app.add_handlers(".*", model_hamdlers)
