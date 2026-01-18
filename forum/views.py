from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Discussion, Comment, Subject, Level
from .forms import DiscussionForm, CommentForm

def forum_list(request):
    discussions = Discussion.objects.all().order_by('-created_at')
    
    # Filter
    subject_id = request.GET.get('subject')
    level_id = request.GET.get('level')
    if subject_id:
        discussions = discussions.filter(subject_id=subject_id)
    if level_id:
        discussions = discussions.filter(level_id=level_id)
        
    subjects = Subject.objects.all()
    levels = Level.objects.all()

    return render(request, 'forum/list.html', {
        'discussions': discussions,
        'subjects': subjects,
        'levels': levels,
    })

@login_required
def create_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.author = request.user
            discussion.save()
            return redirect('forum_list')
    else:
        form = DiscussionForm()
    return render(request, 'forum/create.html', {'form': form})

def discussion_detail(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    comments = discussion.comments.all().order_by('created_at')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.discussion = discussion
            comment.author = request.user
            comment.save()
            return redirect('discussion_detail', pk=pk)
    else:
        form = CommentForm()
    
    return render(request, 'forum/detail.html', {
        'discussion': discussion,
        'comments': comments,
        'form': form,
    })
