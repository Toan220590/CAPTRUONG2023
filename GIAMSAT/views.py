from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import MayBienAp, DuLieuMayBienAp, CanhBao, ThietLapCanhBao, DuLieuLuuTru, ThietBi
from .serializers import MayBienApSerializer, DuLieuMayBienApSerializer, CanhBaoSerializer, ThietLapCanhBaoSerializer, DuLieuLuuTruSerializer, ThietBiSerializer

class MayBienApViewSet(viewsets.ModelViewSet):
    queryset = MayBienAp.objects.all()
    serializer_class = MayBienApSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        may_bien_ap = self.get_object()
        may_bien_ap.hinh_anh = request.FILES.get('hinh_anh')
        may_bien_ap.save()
        return Response({'status': 'hình ảnh đã được cập nhật'})

class DuLieuMayBienApViewSet(viewsets.ModelViewSet):
    queryset = DuLieuMayBienAp.objects.all()
    serializer_class = DuLieuMayBienApSerializer

class CanhBaoViewSet(viewsets.ModelViewSet):
    queryset = CanhBao.objects.all()
    serializer_class = CanhBaoSerializer

class ThietLapCanhBaoViewSet(viewsets.ModelViewSet):
    queryset = ThietLapCanhBao.objects.all()
    serializer_class = ThietLapCanhBaoSerializer

class DuLieuLuuTruViewSet(viewsets.ModelViewSet):
    queryset = DuLieuLuuTru.objects.all()
    serializer_class = DuLieuLuuTruSerializer

class ThietBiViewSet(viewsets.ModelViewSet):
    queryset = ThietBi.objects.all()
    serializer_class = ThietBiSerializer

    @action(detail=True, methods=['post'])
    def dieu_khien(self, request, pk=None):
        thiet_bi = self.get_object()
        thiet_bi.trang_thai = not thiet_bi.trang_thai
        thiet_bi.save()
        return Response({'status': 'thiết bị đã được điều khiển', 'trang_thai': thiet_bi.trang_thai})
