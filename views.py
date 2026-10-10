from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Get selected choices from request POST data
        choices_ids = []
        for key, value in request.POST.items():
            if key.startswith('choice_'):
                choices_ids.append(int(value))
        
        # Create submission and calculate score
        submission = Submission.objects.create(enrollment_id=1) # Adjust based on your enrollment logic
        submission.choices.set(choices_ids)
        submission.save()
        
        return redirect('onlinecourse:exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Calculate total score and results summary
    total_score = 0
    max_score = 0
    for question in course.question_set.all():
        max_score += question.grade
        # Check if user selected correct choices
        # (Implementation details depend on your exact project starter code)
        
    context = {
        'course': course,
        'submission': submission,
        'grade': total_score,
        'max_score': max_score
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
