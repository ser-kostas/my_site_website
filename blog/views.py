from django.shortcuts import render, redirect
from datetime import date
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


def starting_page(request):
    latest_posts = posts
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")


def contact_personal(request):
    return render(request, "blog/contact.html")


def skills(request):
    return render(request, "blog/skills.html")


def education(request):
    return render(request, "blog/education.html")


def machine_learning(request):
    return render(request, "blog/machine-learning-post.html")


def professional_experience(request):
    return render(request, "blog/professional-experience.html")


def crypto(request):
    return render(request, "blog/crypto-page.html")


def personal_website(request):
    return render(request, "blog/website-personal.html")