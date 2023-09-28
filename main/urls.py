from django.urls import path
from main.views import show_main, create_item, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user, logout_user, show_main_by_id, delete_item, increment_amount, decrement_amount

app_name = 'main'

urlpatterns = [
    path('<int:id>/', show_main_by_id, name='show_main_by_id'),
    path('', show_main, name='show_main'),
    path('create-item/', create_item, name='create_item'),
    path('increment-amount/<int:id>', increment_amount, name='increment_amount'),
    path('decrement-amount/<int:id>', decrement_amount, name='decrement_amount'),
    path('delete-item/<int:id>', delete_item, name='delete_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name= 'show_xml'),
    path('json/', show_json, name = 'show_json'),
    path('xml/<int:id>/', show_xml_by_id, name= 'show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name= 'show_json_by_id')
]