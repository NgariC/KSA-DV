from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _


def current_user():
    import inspect
    request = next((fr[0].f_locals['request'] for fr in inspect.stack() if fr[3] == 'get_response'), None)

    return request.user.id


def log_addition(object):
    """
    Log that an object has been successfully added.
    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import LogEntry, ADDITION
    LogEntry.objects.log_action(
        user_id=current_user(),
        content_type_id=ContentType.objects.get_for_model(object).pk,
        object_id=object.pk,
        object_repr=force_str(object),
        action_flag=ADDITION
    )


def log_change(object):
    """
    Log that an object has been successfully changed.
    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import LogEntry, CHANGE
    LogEntry.objects.log_action(
        user_id=current_user(),
        content_type_id=ContentType.objects.get_for_model(object).pk,
        object_id=object.pk,
        object_repr=force_str(object),
        action_flag=CHANGE,
        change_message=_('Changed')
    )


def log_deletion(object):
    """
    Log that an object will be deleted. Note that this method is called
    before the deletion.
    The default implementation creates an admin LogEntry object.
    """
    from django.contrib.admin.models import LogEntry, DELETION
    LogEntry.objects.log_action(
        user_id=current_user(),
        content_type_id=ContentType.objects.get_for_model(object).pk,
        object_id=object.pk,
        object_repr=force_str(object),
        action_flag=DELETION
    )
