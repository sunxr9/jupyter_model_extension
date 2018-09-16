import pymysql
pymysql.install_as_MySQLdb()


from .handlers import setup_handler


def _jupyter_server_extension_paths():
    '''
     Declare the Jupyter server extension paths.
    '''
    return [{"module": "jupyterlab_model"}]


def _jupyter_nbextension_paths():
    """
    Declare the Jupyter notebook extension paths.
    :return:
    """
    return [{'section': "notebook", "dest": "jupyterlab_model"}]


def load_jupyter_server_extension(nbapp):
    """
    Load the Jupyter server extension.
    """
    setup_handler(nbapp.web_app)