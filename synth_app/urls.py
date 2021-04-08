from django.urls import path, include
from . import views

urlpatterns = [
    # render
    path('', views.index),
    path('synth', views.synth_page),
    path('dashboard', views.dashboard),
    # redirect
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('synth/create', views.create_patch),
    path('synth/update', views.synth_update),
    path('synth/load/<int:patch_id>', views.load_patch),
    path('synth/destroy/<int:patch_id>', views.destroy_patch),
]






    # path('wishes/new', views.new_wish),
    # path('wishes/edit/<int:wish_id>', views.edit_wish),
    # path('wishes/stats', views.stats_page),

    # path('wishes/create', views.create_wish),
    # path('wishes/update/<int:wish_id>', views.update_wish),
    # path('wishes/grant/<int:wish_id>', views.grant_wish),
    # path('wishes/destroy/<int:wish_id>', views.destroy_wish),
    # path('like/<int:wish_id>', views.like_wish),
    # path('remove_like/<int:wish_id>', views.remove_like_wish),