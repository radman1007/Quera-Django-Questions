from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer
from .models import Project


class ProjectListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
