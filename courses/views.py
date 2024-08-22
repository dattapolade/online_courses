from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Submission

def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = course.question_set.all()
    return render(request, 'courses/course_details.html', {'course': course, 'questions': questions})

def submit_exam(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    submission = Submission.objects.create(course=course)
    
    for question in course.question_set.all():
        selected_choice = request.POST.get(f'question_{question.id}')
        if selected_choice:
            submission.choices.add(selected_choice)
    
    submission.save()
    return redirect('exam_result', submission_id=submission.id)

def exam_result(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    correct_choices = submission.choices.filter(is_correct=True)
    score = correct_choices.count()
    total_questions = submission.course.question_set.count()
    return render(request, 'courses/exam_result.html', {'submission': submission, 'score': score, 'total_questions': total_questions})
