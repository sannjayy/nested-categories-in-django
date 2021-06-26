from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, ProductView, ParenCategoryView

# Router Object
router = DefaultRouter()

router.register('category', CategoryView, basename='category')
router.register('products', ProductView, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('parents/', ParenCategoryView.as_view(), name='parent_categories'),
]
