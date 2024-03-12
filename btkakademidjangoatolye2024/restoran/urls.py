from . import views
from django.urls import path
from .views import detail,item_detail,add_comment

app_name = 'restoran' # namespace

urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    # item ekleme
    path('add',views.CreateItem.as_view(),name='create_item'),
    # düzenleme
    path('update/<int:id>',views.update_item,name='update_item'),
    # silme
    path('delete/<int:id>',views.delete_item,name='delete_item'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('item/<int:item_id>/add_comment/', add_comment, name='add_comment'),
    

]
