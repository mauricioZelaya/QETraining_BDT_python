import yaml

global generic_data
generic_data = yaml.load(open('../configuration/config.yml'))


def before_all(context):
    context.host = generic_data['APP']['ENDPOINT']
    context.rootpath = generic_data['APP']['TODO_API_ROOTPATH']


def before_feature(context, feature):
    if 'users' in feature.tags:
        context.__MAURICIO_USER__ = generic_data['USERS']['__MAURICIO_USER__']
        context.__MAURICIO_PASS__ = generic_data['USERS']['__MAURICIO_PASS__']
        print(context.__MAURICIO_USER__)

    elif 'videos' in feature.tags:
        context.user = generic_data['USERS']['USER_DENNIS']
        context.apiKey = generic_data['USERS']['API_KEY_DENNIS']

    elif "alejandro" in feature.tags:
        context.__ALEJANDRO_USER__ = generic_data['USERS']['__ALEJANDRO_USER__']
        context.__ALEJANDRO_PASS__ = generic_data['USERS']['__ALEJANDRO_PASS__']


    elif 'playlist' in feature.tags:
        context.user = generic_data['USERS']['USER_PABLO']
        context.apiKey = generic_data['USERS']['API_KEY_PABLO']
        
    elif 'playlist_item' in feature.tags:
        context.user = generic_data['USERS']['USER_DANEIVA']
        context.apiKey = generic_data['USERS']['API_KEY_DANEIVA']
