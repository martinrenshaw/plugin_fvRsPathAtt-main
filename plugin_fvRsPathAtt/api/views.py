"""
from rest_framework.viewsets import ModelViewSet
from plugin_fvRsPathAtt.models import MyModel1
from .serializers import MyModel1Serializer


class MyModel1ViewSet(ModelViewSet):
    queryset = MyModel1.objects.all()
    serializer_class = MyModel1Serializer
"""
from rest_framework import mixins, viewsets

from plugin_fvRsPathAtt.models import fvRsPathAtt
from plugin_fvRsPathAtt.filters import fvRsPathAttFilter

from .serializers import fvRsPathAttSerializer


class fvRsPathAttView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Create, check status of, update, and delete fvRsPathAtt object."""

    queryset = fvRsPathAtt.objects.all()
    filterset_class = fvRsPathAttFilter
    serializer_class = fvRsPathAttSerializer