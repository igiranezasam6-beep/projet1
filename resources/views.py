from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Exercise, Video, Subject, Level
from .forms import ExerciseForm

def is_teacher(user):
    return user.is_authenticated and user.is_teacher()

def resource_list(request):
    exercises = Exercise.objects.all().select_related('subject', 'level')
    videos = Video.objects.all().select_related('subject', 'level')
    
    # Filter
    subject_id = request.GET.get('subject')
    level_id = request.GET.get('level')
    
    if subject_id:
        exercises = exercises.filter(subject_id=subject_id)
        videos = videos.filter(subject_id=subject_id)
    if level_id:
        exercises = exercises.filter(level_id=level_id)
        videos = videos.filter(level_id=level_id)

    subjects = Subject.objects.all()
    levels = Level.objects.all()

    return render(request, 'resources/list.html', {
        'exercises': exercises,
        'videos': videos,
        'subjects': subjects,
        'levels': levels,
    })

@login_required
@user_passes_test(is_teacher)
def upload_resource(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.teacher = request.user
            exercise.save()
            return redirect('resource_list')
    else:
        form = ExerciseForm()
    return render(request, 'resources/upload.html', {'form': form})
