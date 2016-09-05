from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Comment, Choice

# Create your views here.

#Generics for Problematic Statement
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

# CRUD functionality for Comments
class StatementCreate(CreateView):
	model = Comment
	fields = ['comment_text']

class StatementUpdate(UpdateView):
	model = Comment
	fields = ['comment_text']

class StatementDelete(DeleteView):
	model = Comment
	success_url = reverse_lazy('polls:index')

#Generic for Counter Argument

class CounterArgCreate(CreateView):
    model = Choice
    fields = ['comment','choice_text',]

#View for Voting Function


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

# Leave the rest of the views (detail, results, vote) unchanged