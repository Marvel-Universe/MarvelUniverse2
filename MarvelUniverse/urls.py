from django.urls import path
from .views.homepage import HomePageView
from .views.about import AboutUsView
from .views.see_all import AllCharactersView, AllComicsView, AllSeriesView
from .views.detail import character_detail_view, comic_detail_view, series_detail_view
from .views.favorites import toggle_favorite
from .views.favorites import FavoriteView
from .views.profile import ProfileView, UpdateProfileImageView


app_name = "MarvelUniverse"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('characters/', AllCharactersView.as_view(), name="characters"),
    path('comics/', AllComicsView.as_view(), name="comics"),
    path('series/', AllSeriesView.as_view(), name="series"),
    path('<str:model>/<int:object_id>/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', FavoriteView.as_view(), name='favorites'),
    path('characters/<int:character_pk>', character_detail_view, name="characters-detail"),
    path('comics/<int:comic_pk>', comic_detail_view, name="comics-detail"),
    path('series/<int:series_pk>', series_detail_view, name="series-detail"),
    path('about/', AboutUsView.as_view(), name='about'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update_profile_image/', UpdateProfileImageView.as_view(), name='update_profile_image'),

]
