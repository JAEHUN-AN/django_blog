
from django.contrib import admin
from django.urls import path, include

from mybookmark.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),

    # path('bookmark/', BookmarkLV.as_view(), name='index'),    
    # path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),
    # 
    path('bookmark/', include('bookmarkapp.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),  
]