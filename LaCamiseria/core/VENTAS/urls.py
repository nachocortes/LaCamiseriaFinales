from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('add/<int:producto_id>/', views.cart_add, name='cartAdd'),
    path('remove/<int:producto_id>/', views.cart_remove, name='cartRemove'),
    path('create/', views.pedido_create, name='pedidoCreate'),
    path('factura/<int:pk>/', views.PedidoFacturaDetailView.as_view(), name='pedido_factura'),
    path('pdfPedido/<int:pk>/', views.PdfPedido.as_view(), name='pdf_pedido'),
    path('pedidos/', views.PedidoListView.as_view(), name='pedido_list'),
]
