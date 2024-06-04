from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from core.VENTAS.forms import AgregarCartProductoForm
from .models import Producto, Categoria
from django.views.generic.detail import DetailView
from django.db.models import Q


def inicio_store(request):
    productos = Producto.objects.all().order_by('-id')[:8]
    return render(request, 'store/01_inicio.html', {'productos': productos})


def productos_store(request):
    productos = Producto.objects.all()
    return render(request, 'store/02_productos.html', {'productos': productos})


def about_store(request):
    return render(request, 'store/03_about.html', )


def blog_store(request):
    return render(request, 'store/04_blog.html', )


def contacto_store(request):
    if request.method == 'POST':
        subject = request.POST['asunto']
        message = request.POST['mensaje'] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["nachoDamDjango@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)
        return render(request, "store/06_confirmacion_envio_email.html")
    return render(request, 'store/05_contacto.html', )


def producto_list(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    if categoria_slug:
        categoria = get_object_or_404(Categoria,
                                      translations__slug=categoria_slug)
        productos = productos.filter(categoria=categoria)

    paginator = Paginator(productos, 15)
    page = request.GET.get('page')

    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)
    return render(request,
                  'productos/listaProductos.html',
                  {'categoria': categoria,
                   'categorias': categorias,
                   'productos': productos})


def productos_por_categoria(request, categoria_id=None):
    categorias = Categoria.objects.all()
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

    paginator = Paginator(productos, 15)
    page = request.GET.get('page')

    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    context = {
        'categorias': categorias,
        'productos': productos,
        'categoria_id': categoria_id
    }
    return render(request, 'productos/productos_por_categoria.html', context)

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto/detalleProducto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_producto_form'] = AgregarCartProductoForm()
        return context


class ProductoSearchListView(ListView):
    template_name = 'productos/producto/search.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(categoria__nombre__icontains=self.query())
        return Producto.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['listaProductos'].count()
        print('Este es query', context['query'])
        return context
