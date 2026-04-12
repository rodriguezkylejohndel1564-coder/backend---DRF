from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.api.views import (
    LoginView,
    ProductViewSet,
    RegisterView,
    AlertViewSet,
    WaterLevelViewSet,
    IncidentReportViewSet,
)

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"alerts", AlertViewSet, basename="alert")
router.register(r"water-levels", WaterLevelViewSet, basename="water-level")
router.register(r"reports", IncidentReportViewSet, basename="report")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
