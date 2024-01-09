from django.core.exceptions import ValidationError


def title_validator(title):
    title_words = title.split()
    if len(title_words) <= 1:
        raise ValidationError(
            "O título deve conter pelo menos 2 palavras."
        )
