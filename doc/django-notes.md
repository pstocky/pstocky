# Django 使用注意事项

## 恰当的使用 UserModel

#### model 中使用 User 作为外键


```python
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
```

#### 方法中，使用 User

```python
from django.contrib.auth import get_user_model


def create_user():

    UserModel = get_user_model()

    UserModel._default_manager.create_user(
        username=username, password=password
    )
```
