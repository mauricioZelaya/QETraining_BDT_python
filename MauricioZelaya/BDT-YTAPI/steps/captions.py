from utils.utils import *
from compare import expect

@when(u'Looking for {videoId} id')
def step_impl(context, videoId):
    context.videoId = videoId
    context.payload = fill_payload(context.apiKey, videoId = context.videoId)
