from django.db import models
from django.utils.translation import gettext_lazy as _
from .settings import DEFAULT_URL_CHECK_INTERVAL_IN_SEC
from django.contrib.auth import get_user_model

User = get_user_model()


class Url(models.Model):
    class Meta:
        db_table = 'url'
    url = models.URLField(_('url'), null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')

