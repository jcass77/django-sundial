from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.text import force_text
from django.utils.translation import ugettext_lazy as _
import pytz

from .settings import TIMEZONE_SESSION_KEY


def set_session_timezone(session, zone):
    session[TIMEZONE_SESSION_KEY] = force_text(zone)


def get_session_timezone(session):
    return session.get(TIMEZONE_SESSION_KEY)


def coerce_timezone(zone):
    try:
        return pytz.timezone(zone)
    except pytz.UnknownTimeZoneError:
        raise ValidationError(
            _('Unknown timezone.'), code='invalid'
        )