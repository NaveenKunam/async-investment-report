from django.core.management.base import BaseCommand
from investments.models import Investor
from investments.tasks import generate_investment_report

class Command(BaseCommand):
    help = 'Send investment reports to all investors'

    def handle(self, *args, **kwargs):
        investors = Investor.objects.all()
        for investor in investors:
            generate_investment_report.delay(investor.id)
            self.stdout.write(self.style.SUCCESS(f"Triggered report task for {investor.name}"))
