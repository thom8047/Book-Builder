from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView
from markdown import markdown

from .models import Book, Chapter


class HomeView(TemplateView):
    template_name = 'home.html'


class BookAdd(CreateView):
    template_name = "book_edit.html"
    model = Book
    fields = '__all__'


class BookDetail(DetailView):
    template_name = 'book_detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        kwargs = super(BookDetail, self).get_context_data(**kwargs)
        kwargs['chapters'] = Chapter.objects.filter(book=kwargs['object'])
        return kwargs


class BookEdit(UpdateView):
    template_name = "book_edit.html"
    model = Book
    fields = '__all__'

    def get_context_data(self, **kwargs):
        kwargs = super(BookEdit, self).get_context_data(**kwargs)
        kwargs['edit'] = True
        return kwargs


class BookList(ListView):
    template_name = 'book_list.html'
    model = Book


class ChapterAdd(CreateView):
    template_name = "chapter_add.html"
    model = Chapter
    fields = '__all__'

    def form_valid(self, form):
        book_id = self.kwargs.get('book_id')
        form.instance.book_id = book_id
        return super().form_valid(form)


class ChapterDetail(DetailView):
    template_name = 'chapter_detail.html'
    model = Chapter
    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['markdown'] = markdown(kwargs['object'].text)
        return kwargs


class ChapterEdit(UpdateView):
    template_name = "chapter_edit.html"
    model = Chapter
    fields = '__all__'


class ChapterList(ListView):
    template_name = 'chapter_list.html'
    model = Chapter


