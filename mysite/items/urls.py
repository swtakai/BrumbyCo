from django.urls import path, reverse_lazy
from . import views

app_name='items'
urlpatterns = [
    path('', views.ItemListView.as_view(), name='all'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/create',
        views.ItemCreateView.as_view(success_url=reverse_lazy('items:all')), name='item_create'),
    path('item/<int:pk>/update',
        views.ItemUpdateView.as_view(success_url=reverse_lazy('items:all')), name='item_update'),
    path('item/<int:pk>/delete',
        views.ItemDeleteView.as_view(success_url=reverse_lazy('items:all')), name='item_delete'),
        path('item_picture/<int:pk>', views.stream_file, name='item_picture'),
    path('item/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='item_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('items:all')), name='item_comment_delete'),
    path('item/<int:pk>/addreview',
        views.addReview, name='create_review'),
    path('item/<int:pk>/review',
        views.ReviewCreateView.as_view(), name='review_create'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
