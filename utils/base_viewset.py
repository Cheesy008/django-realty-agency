from rest_framework import viewsets


class BaseModelViewSet(viewsets.ModelViewSet):
    serializer_classes = None
    default_serializer_class = None

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
