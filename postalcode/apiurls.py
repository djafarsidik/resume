from rest_framework import routers
from django.urls import include,path
from . import apiviews

router = routers.DefaultRouter()

router.register(r'provinsi', apiviews.ProvinsiViewSets)
router.register(r'kabupaten', apiviews.KabkotaViewSets)


urlpatterns =[
    path ('', include(router.urls)),
]