# giam_sat/management/commands/delete_old_data.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from GIAMSAT.models import DuLieuMayBienAp

class Command(BaseCommand):
    help = 'Delete old data in DuLieuMayBienAp older than 1 month'

    def handle(self, *args, **kwargs):
        one_month_ago = timezone.now() - timedelta(days=30)
        old_data_count = DuLieuMayBienAp.objects.filter(thoi_gian__lt=one_month_ago).count()
        DuLieuMayBienAp.objects.filter(thoi_gian__lt=one_month_ago).delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {old_data_count} old data entries'))
