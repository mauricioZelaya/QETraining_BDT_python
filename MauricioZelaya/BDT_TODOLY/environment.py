import yaml
from utils.utils import *

global generic_data
generic_data = yaml.load(open('../configuration/config.yml'))


def before_all(context):
    context.host = generic_data['APP']['ENDPOINT']
    context.rootpath = generic_data['APP']['TODO_API_ROOTPATH']
    context.endpoint = context.host + context.rootpath


def before_feature(context, feature):
    if 'users' in feature.tags:
        context.__MAURICIO_USER__ = generic_data['USERS']['__MAURICIO_USER__']
        context.__MAURICIO_PASS__ = generic_data['USERS']['__MAURICIO_PASS__']
        print(context.__MAURICIO_USER__)
        context.auth = fill_authorization_basic(context.__MAURICIO_USER__, context.__MAURICIO_PASS__)

    elif 'items' in feature.tags:
        context.__DENNIS_USER__ = generic_data['USERS']['__DENNIS_USER__']
        context.__DENNIS_PASS__ = generic_data['USERS']['__DENNIS_PASS__']

    elif "alejandro" in feature.tags:
        context.__ALEJANDRO_USER__ = generic_data['USERS']['__ALEJANDRO_USER__']
        context.__ALEJANDRO_PASS__ = generic_data['USERS']['__ALEJANDRO_PASS__']

    elif "projects" in feature.tags:
        context.__DAN_USER__ = generic_data['USERS']['__DAN_USER__']
        context.__DAN_PASS__ = generic_data['USERS']['__DAN_PASS__']
