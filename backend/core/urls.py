from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LoginView, ProductViewSet, RegisterView

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
