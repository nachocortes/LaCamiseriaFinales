from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView, View
from core.CRM.models import Cliente
from core.LOGIN.decorators import authenticated
from core.STORE.models import Producto
from core.VENTAS.cart import Cart
from core.VENTAS.forms import AgregarCartProductoForm, CrearPedidoForm
from core.VENTAS.models import PedidoItem, Pedido
from core.VENTAS.utils import render_to_pdf


@login_required
@require_POST
def cart_add(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = AgregarCartProductoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            producto=producto,
            cantidad=cd['cantidad'],
            anular_cantidad=cd['anular'],
        )
    return redirect('cart:cart')

@login_required
@require_POST
def cart_remove(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    cart.remove(producto)
    return redirect('cart:cart')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['actualizar_cantidad_form'] = AgregarCartProductoForm(
            initial={'cantidad': item['cantidad'], 'anular': True}
        )
    return render(request, 'cart/cart.html', {'cart': cart})
@login_required
def pedido_create(request):
    model = Pedido
    cart = Cart(request)
    if request.method == 'POST':
        form = CrearPedidoForm(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.filter(user=request.user).first()
            if not cliente:
                return HttpResponseNotFound("No Cliente matches the given query.")
            pedido = form.save(commit=False)
            pedido.cliente = cliente
            pedido.user = request.user
            pedido.save()
            for item in cart:
                PedidoItem.objects.create(
                    pedido=pedido,
                    producto=item['producto'],
                    precio=item['precio'],
                    cantidad=item['cantidad'],
                )

            cart.clear()
            pedido_created(request, pedido.id)  # Asegúrate de pasar request aquí
            return render(
                request, 'pedidos/pedido/created_pedido.html', {'pedido': pedido, 'cart': cart}
            )
    else:
        form = CrearPedidoForm()
    return render(
        request,
        'pedidos/pedido/create_pedido.html',
        {'cart': cart, 'form': form},
    )


def pedido_created(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    subject = f'Pedido nr. {pedido.id}'
    message = (
        f'Estimado {pedido.nombre},\n\n'
        f'Ha realizado correctamente un pedido.'
        f'Su ID de pedido es el {pedido.id}.'
    )
    mail_sent = send_mail(
        subject, message, 'nachoDamDjango@gmail.com', [pedido.email]
    )
    return mail_sent


@method_decorator(authenticated, name='dispatch')
class PedidoFacturaDetailView(DetailView):
    model = Pedido
    template_name = 'pedidos/pedido/factura.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedido_items'] = self.object.items.all()
        return context


@method_decorator(authenticated, name='dispatch')
class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedidos/pedidolist.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Pedido.objects.none()

        return Pedido.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tiene_pedidos'] = self.get_queryset().exists()
        return context


@method_decorator(authenticated, name='dispatch')
class PdfPedido(View):
    model = Pedido

    def get(self, request, pk, *args, **kwargs):
        pedido = Pedido.objects.get(id=pk)
        pedido_items = pedido.items.all()
        context = {
            'pedido': pedido,
            'pedido_items': pedido_items,
        }
        pdf = render_to_pdf("pedidos/pedido/pdf_pedido.html", context)
        return HttpResponse(pdf, content_type="application/pdf")
