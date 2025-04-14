from celery import shared_task
from .models import Investment, Investor
from collections import defaultdict
import json

@shared_task
def generate_investment_report(investor_id):
    try:
        investor = Investor.objects.get(id=investor_id)
        investments = Investment.objects.filter(investor=investor)

        report = defaultdict(float)
        for inv in investments:
            report[inv.property.title] += float(inv.amount)

        report_data = {
            "investor": investor.name,
            "investments": dict(report)
        }

        print(f"Report for {investor.name}:\n{json.dumps(report_data, indent=4)}")
        print(f"Simulated email sent to {investor.email}")
    except Investor.DoesNotExist:
        print("Investor not found.")
