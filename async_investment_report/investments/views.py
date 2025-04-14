from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Investor
from .tasks import generate_investment_report

class InvestmentReportView(APIView):
    def get(self, request, investor_id):
        try:
            investor = Investor.objects.get(id=investor_id)
        except Investor.DoesNotExist:
            return Response({"error": "Investor not found"}, status=404)

        task = generate_investment_report.delay(investor.id)
        return Response({"message": "Report generation started", "task_id": task.id})
