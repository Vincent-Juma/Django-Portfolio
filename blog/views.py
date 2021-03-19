from django.shortcuts import render

posts = [
    {
        'author': 'Vincent Juma',
        'title': 'Blog Post-1',
        'content': 'first post',
        'date_posted': 'March 20th, 2021'
    },
    {
        'author': 'Collin Powell',
        'title': 'Blog Post-2',
        'content': 'Second post',
        'date_posted': 'March 21st, 2021'
    },
    {
        'author': 'Joseph Owuoth',
        'title': 'Blog Post-3',
        'content': 'third post',
        'date_posted': 'March 22nd, 2021'
    }
]



def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})