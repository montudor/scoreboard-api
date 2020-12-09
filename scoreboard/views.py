from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from .permissions import ScoreboardPermission
from .serializers import ScoreSerializer
from .models import Score

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all().order_by('-score', 'level')
    serializer_class = ScoreSerializer
    permission_classes = [ScoreboardPermission]

    def create(self, request):
        serializer = ScoreSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'detail': 'Invalid score object'}, status=400)


        scores = Score.objects.filter(name=serializer.data['name']).order_by('-score', 'level')
        score = None

        if scores.count() > 0:
            score = scores[0]
            if score.score < serializer.data['score']:
                score.score = serializer.data['score']
                score.level = serializer.data['level']
                score.created = timezone.now()
                score.save()
            serializer = ScoreSerializer(score)
            return Response(serializer.data)

        score = Score(
            name=serializer.data['name'],
            score=serializer.data['score'],
            level=serializer.data['level']
        )
        score.save()

        serializer = ScoreSerializer(score)

        return Response(serializer.data)
