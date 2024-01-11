from django.urls import path
from .views import olp_list, olp_update, olp_delete, icpc_list, icpc_update, icpc_delete, procon_list, procon_update, procon_delete,olp_create, icpc_create,procon_create

urlpatterns = [
    #path for OLP Achievement
    path('olp/', olp_list, name='olp_list'),
    path('olp/create/', olp_create, name='olp_create'),
    path('olp/<int:olp_id>/update/', olp_update, name='olp_update'),
    path('olp/<int:olp_id>/delete/', olp_delete, name='olp_delete'),

    #path for ICPC Achievement
    path('icpc/', icpc_list, name='icpc_list'),
    path('icpc/create/', icpc_create, name='icpc_create'),
    path('icpc/<int:icpc_id>/update/', icpc_update, name='icpc_update'),
    path('icpc/<int:icpc_id>/delete/', icpc_delete, name='icpc_delete'),

    #path for PROCON Achievment
    path('procon/', procon_list, name='procon_list'),
    path('procon/create/', procon_create, name='procon_create'),
    path('procon/<int:procon_id>/update/', procon_update, name='procon_update'),
    path('procon/<int:procon_id>/delete/', procon_delete, name='procon_delete'),
]
