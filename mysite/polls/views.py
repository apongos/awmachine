from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Comment, Choice

# Create your views here.

#Generic
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_comment_list'

    def get_queryset(self):
        """Return the last five published comments."""
        return Comment.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Comment
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Comment
    template_name = 'polls/results.html'

class NewStatementView(generic.DetailView):
	model = Comment
	template_name = 'polls/comment_form.html'

class StatementCreate(CreateView):
	model = Comment
	fields = ['comment_text']

class StatementUpdate(UpdateView):
	model = Comment
	fields = ['comment_text']

class StatementDelete(DeleteView):
	model = Comment
	success_url = reverse_lazy('polls:index')

#Views
def detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'polls/detail.html', {'comment': comment})

def results(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'polls/results.html', {'comment': comment})

def vote(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    try:
        selected_choice = comment.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'comment': comment,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(comment.id,)))

def index(request):
    latest_comment_list = Comment.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_comment_list': latest_comment_list,
    }
    return HttpResponse(template.render(context, request))

def newStatement(request, comment):
	new_statement = Comment(comment_text="comment")
	template = loader.get_template('polls/new.html')
	context = {
        'new_statement': new_statement,
    }
	return HttpResponse(reverse('polls:results'))

# Leave the rest of the views (detail, results, vote) unchanged