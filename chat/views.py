from rest_framework.response import Response
from rest_framework.views import APIView
from .pusher import pusher_client


class MessageAPIView(APIView):

    def post(self, request):
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message'],
        })

        return Response([])
