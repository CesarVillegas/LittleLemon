from django.urls import path
from . import views


urlpatterns = [
    # path('menu-items', views.MenuItemsView.as_view()),
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items', views.menu_items),                               # function-based
    path('menu-items/<int:id>', views.single_item),                     # function-based
    
    path('v2/menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),                  # class-based
    path('v2/menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),     # class-based
]