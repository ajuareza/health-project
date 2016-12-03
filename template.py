{% if disease %}
I hear you, {{ disease }}!!
{% endif %}
<form action="{{ form_action }}"
method="{{ form_method }}">
{{ form.as_p }}
</form>
