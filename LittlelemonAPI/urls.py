from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('menu-items', views.MenuItemsView.as_view()),
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items', views.menu_items),                               # function-based
    path('menu-items/<int:id>', views.single_item),                     # function-based
    
    path('v2/menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),                  # class-based
    path('v2/menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),     # class-based
    
    # added for authentication
    path('secret/', views.secret),
    
    # added for authentication
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # added for manager view
    path('manager-view', views.manager_view),  
    
    # added for throttle check
    path('throttle_check', views.throttle_check),
    
    # added for throttle check for authenticated users
    path('throttle_check_auth', views.throttle_check_auth),
    
]

