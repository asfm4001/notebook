from django.urls import path
from notes import views

app_name = "note"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('<int:pk>', views.NoteDetailView.as_view(), name='detail'),
    path('list/', views.NoteListView.as_view(), name='list'),
    path('new/', views.NoteCreateView.as_view(), name='create')
]