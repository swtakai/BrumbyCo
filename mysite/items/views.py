from items.models import Item, Comment, Review
from items.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from items.forms import CreateForm, CommentForm, ReviewForm
from django.urls import reverse_lazy, reverse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

class ItemListView(OwnerListView):
    model = Item
    # By convention:
    # template_name = "items/item_list.html"


class ItemDetailView(OwnerDetailView):
    model = Item
    template_name = "items/item_detail.html"
    def get(self, request, pk) :
        x = Item.objects.get(id=pk)
        comments = Comment.objects.filter(item=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'item' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class ItemCreateView(OwnerCreateView):
    # model = Item
    # fields = ['title', 'text', 'price']
    template_name = 'items/item_form.html'
    success_url = reverse_lazy('items:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect(self.success_url)


class ItemUpdateView(OwnerUpdateView):
    # model = Item
    # fields = ['title', 'text', 'price']
    template_name = 'items/item_form.html'
    success_url = reverse_lazy('items:all')

    def get(self, request, pk):
        item = get_object_or_404(Item, id=pk, owner=self.request.user)
        form = CreateForm(instance=item)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        item = get_object_or_404(Item, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=item)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        item = form.save(commit=False)
        item.save()

        return redirect(self.success_url)

class ItemDeleteView(OwnerDeleteView):
    model = Item

def stream_file(request, pk):
    item = get_object_or_404(Item, id=pk)
    response = HttpResponse()
    response['Content-Type'] = item.content_type
    response['Content-Length'] = len(item.picture)
    response.write(item.picture)
    return response

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Item, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, item=f)
        comment.save()
        return redirect(reverse('items:item_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "items/item_comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        item = self.object.item
        return reverse('items:item_detail', args=[item.id])

def addReview(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = Review()
            data.name = form.cleaned_data['name']
            data.subject = form.cleaned_data['subject']
            data.review = form.cleaned_data['review']
            data.ip = request.METS.get('REMOTE_ADDR')
            data.item_id = id
            current_user = request.user
            data.owner = current_user.id
            data.save()
            messages.success(request, "Your review has been sent. Thank you.")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

# class ReviewCreateView(OwnerCreateView):
#     model = Review
#     fields = ['subject', 'review', 'rating']

# class ReviewCreateView(OwnerCreateView):
#     # model = Item
#     # fields = ['title', 'text', 'price']
#     template_name = 'items/review_form.html'
#     success_url = reverse_lazy('items:all')

#     def get(self, request, pk=None):
#         form = ReviewForm()
#         ctx = {'form': form}
#         return render(request, self.template_name, ctx)

#     def post(self, request, pk=None):
#         form = Review(request.POST, request.FILES or None)

#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template_name, ctx)

#         # Add owner to the model before saving
#         item = form.save(commit=False)
#         item.owner = self.request.user
#         item.save()
#         return redirect(self.success_url)

class ReviewCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Item, id=pk)
        comment = Review(text=request.POST['rating'], owner=request.user, item=f)
        comment.save()
        return redirect(reverse('items:item_detail', args=[pk]))



