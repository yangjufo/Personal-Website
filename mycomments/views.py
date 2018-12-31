from django.shortcuts import render, get_object_or_404, redirect
from myblog.models import Post
from myprojects.models import Project


from .forms import PostCommentForm, ProjectCommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.postcomment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'myblog/detail.html', context=context)
    return redirect(post)


def project_comment(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = ProjectCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            return redirect(project)
        else:
            comment_list = project.projectcomment_set.all()
            context = {'project': project,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'myprojects/detail.html', context=context)
    return redirect(project)
