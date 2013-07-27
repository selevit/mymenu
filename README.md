## Installation

1. Add mymenu to `INSTALLED_APPS`.
2. Add `mymenu.context_processors.context` to `TEMPLATE_CONTEXT_PROCESSORS`.
3. Run `python manage.py syncdb`
3. Run `python manage.py migrate mymenu` (south required)

```python
# settings.py

INSTALLED_APPS = (
    # ...
    'mymenu'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # ... (default context processors) 

    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',

    # MyMenu context
    'mymenu.context_processors,context',
)
```

## Usage

Add the menu from a django admin page. Use slug of the menu as access key in templates.

For example, let's render the menu that slug is "top"

```html
{% for menu_item in menu.top.items %}
    {% ifequal request.get_full_path menu_item.url %}
        <span class="active">{{ menu_item.name }}</span>
    {% else %}

    <a href="{{ menu_item.url }}"

    {% if menu_item.title %}
        title="{{ menu_item.title }}"
    {% endif %}

    {% if menu_item.target %}
        target="{{ menu_item.target }}"
    {% endif %}>{{ menu_item.name }}</a>
{% endifequal %}
```
