import yaml

global generic_data
generic_data = yaml.load(open('../configuration/config.yml'))


def before_all(context):
    context.host = generic_data['APP']['ENDPOINT']
    context.rootpath = generic_data['APP']['YOUTUBE_API_ROOTPATH']


def before_feature(context, feature):
    if 'comments' in feature.tags or 'commentThreads' in feature.tags:
        context.user = generic_data['USERS']['USER_MAURICIO']
        context.apiKey = generic_data['USERS']['API_KEY_MAURICIO']

    elif 'videos' in feature.tags:
        context.user = generic_data['USERS']['USER_DENNIS']
        context.apiKey = generic_data['USERS']['API_KEY_DENNIS']

    elif ('search' in feature.tags) or ('captions' in feature.tags):
        context.user = generic_data['USERS']['USER_ALEJANDRO']
        context.apiKey = generic_data['USERS']['API_KEY_ALEJANDRO']

    elif 'playlist' in feature.tags:
        context.user = generic_data['USERS']['USER_PABLO']
        context.apiKey = generic_data['USERS']['API_KEY_PABLO']
        
    elif 'playlist_item' in feature.tags:
        context.user = generic_data['USERS']['USER_DANEIVA']
        context.apiKey = generic_data['USERS']['API_KEY_DANEIVA']
