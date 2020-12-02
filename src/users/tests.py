import secrets
import string

import pytest

from django.contrib.auth import get_user_model
from django.db import IntegrityError


def get_password(length):
    return ''.join((secrets.choice(string.ascii_letters) for i in range(length)))


@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    password = get_password(8)
    user = User.objects.create_user(email='normal@user.com', first_name="User", last_name="Userson", password=password)
    assert user.email == 'normal@user.com'
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    try:
        # username is None for the AbstractUser option
        # username does not exist for the AbstractBaseUser option
        assert not user.username
    except AttributeError:
        pass
    with pytest.raises(TypeError):
        User.objects.create_user()
    with pytest.raises(ValueError, match='The given email must be set'):
        User.objects.create_user(email='')
    with pytest.raises(ValueError, match='The given email must be set'):
        User.objects.create_user(email='', first_name="User", last_name="Userson", password=password)


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    password = get_password(8)
    admin_user = User.objects.create_superuser('super@user.com', password, first_name='User', last_name='Userson')
    assert admin_user.email == 'super@user.com'
    assert admin_user.first_name == 'User'
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser
    try:
        # username is None for the AbstractUser option
        # username does not exist for the AbstractBaseUser option
        assert not admin_user.username
    except AttributeError:
        pass
    with pytest.raises(IntegrityError):
        User.objects.create_superuser(
            email='super@user.com', password=password, is_superuser=False)
