from myarts.models import Item
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ItemListView(OwnerListView):
    model = Item
    # By convention:
    # template_name = "myarts/article_list.html"


class ItemDetailView(OwnerDetailView):
    model = Item


class ItemCreateView(OwnerCreateView):
    model = Item
    fields = ['title', 'text', 'price']


class ItemUpdateView(OwnerUpdateView):
    model = Item
    fields = ['title', 'text', 'price']


class ItemDeleteView(OwnerDeleteView):
    model = Item
