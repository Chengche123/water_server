from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action

from .serializers import HX2022Serializer
from .models import HX2022


class HX2022Consumer(GenericAsyncAPIConsumer):

    @model_observer(HX2022)
    async def comment_activity(
        self,
        message,
        observer=None,
        subscribing_request_ids=[],
        **kwargs,
    ):
        await self.send_json(message)

    @comment_activity.serializer
    def comment_activity(self, instance: HX2022, action, **kwargs) -> HX2022Serializer:
        '''This will return the comment serializer'''
        return HX2022Serializer(instance).data

    @action()
    async def subscribe_to_hx2022_activity(self, request_id, **kwargs):
        await self.comment_activity.subscribe(request_id=request_id)
