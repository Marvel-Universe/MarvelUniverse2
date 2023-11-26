from django.shortcuts import render, get_object_or_404
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from MarvelUniverse.models import UserData


class ProfileView(View):
    """
    View for rendering the user profile page.

    Attributes:
    - template_name (str): The path to the HTML template used for rendering the profile page.

    Methods:
    - get(request, username): Handles HTTP GET requests to display the user's profile page.

    Usage:
    1. Create an instance of this view and include it in your URL patterns.
    2. Customize the 'MarvelUniverse/profile.html' template to display user-specific information.
    """
    template_name = 'MarvelUniverse/profile.html'

    def get(self, request):
        """
        Handle GET requests to render the user's profile page.

        Args:
        - request (HttpRequest): The HTTP request object.
        - username (str): The username of the user.

        Returns:
        - HttpResponse or JsonResponse: The rendered profile page or JSON response.
        """
        # Get the user object based on the provided username
        this_user = request.user
        user_data, created = UserData.objects.get_or_create(user=this_user)

        formatted_date_joined = naturaltime(this_user.date_joined)

        context = {
            'username': this_user.username,
            'email': this_user.email,
            'profile_img_url': user_data.profile_img_url,
            'trophy_img': user_data.trophy_img,
            'scores': user_data.scores,
            'date_joined': formatted_date_joined,
        }

        return render(request, self.template_name, context=context)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateProfileImageView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        avatar_url = data.get('avatarUrl', '')

        # Update the user's profile image
        user_data = UserData.objects.get(user=request.user)
        user_data.profile_img_url = avatar_url
        user_data.save()

        return JsonResponse({'success': True})