from django.urls import path
from .views import InvestmentReportView

urlpatterns = [
    path('api/investments/report/<int:investor_id>/', InvestmentReportView.as_view()),
]
