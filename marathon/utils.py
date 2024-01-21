from django.conf import settings
from django.forms.models import model_to_dict
from allauth.account.models import EmailAddress
from .models import Player


def get_user_discord(user: settings.AUTH_USER_MODEL):
    if hasattr(user, 'socialaccount_set'):
        for account in user.socialaccount_set.all():
            if account.provider == 'discord':
                username = account.extra_data.get('username', None)
                nickname = account.extra_data.get('global_name', None)
                return {
                    'discord': username,
                    'nickname': nickname
                }
    return None

def get_user_primary_email(user: settings.AUTH_USER_MODEL):
    return EmailAddress.objects.get_primary_email(user)

def get_player_info_for_user(user: settings.AUTH_USER_MODEL):
    player = Player.objects.get(user=user)
    if player:
        return model_to_dict(player)

    player_info = {}

    discord_info = get_user_discord(user) or {}
    player_info.update(discord_info)
    
    email = get_user_primary_email(user)
    player_info['gmail'] = email

    return player_info
