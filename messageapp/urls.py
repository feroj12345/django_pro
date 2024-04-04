
from django.urls import path
from messageapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('pra',views.pra),
    path('page',views.page),
    path('dashboard',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('hm',views.hm),
    path('pdetails/<pid>',views.product_details),
    path('about',views.about),
    path('contact',views.contact),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('range',views.range),
    path('addtocart/<pid>',views.addtocart),
    path('cart',views.cart),
    path('remove/<cid>',views.remove),
    path('viewcart',views.viewcart),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
