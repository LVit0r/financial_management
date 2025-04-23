from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from expenses.views import ExpensesOverview, NewExp, EditExp, DeleteExp
from investments.views import NewInvest, EditInvest, EntryDelete
#from accounts.views import LoginView, RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', LoginView.as_view(), name='login'),
    #path('register/', RegisterView.as_view(), name='register'),
    path('', ExpensesOverview.as_view(), name='expenses_overview'),
    path('new_expense/', NewExp.as_view(), name='new_exp'),
    path('edit_exp/<int:id>/', EditExp.as_view(), name='editexp'),
    path('delete_exp/<int:id>/', DeleteExp.as_view(), name='delete_exp'),
    path('new_investment/', NewInvest.as_view(), name='new_invest'),
    path('edit_invest/<int:id>', EditInvest.as_view(), name='edit_invest' ),
    path('delete_invest/<int:id>', EntryDelete.as_view(), name='delete_invest' ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
