from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model


class contentModel(models.Model):

    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("the `title` of the content."),
        max_length=128,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("the `description` of the content."),
        max_length=1000,
    )
    numberOfRates = models.PositiveIntegerField(
        verbose_name=_("Number of rates "),
        help_text=_("the `Number of rates` of the content."),
        default=0,

    )
    averageRate = models.FloatField(
        verbose_name=_("Average rate"),
        help_text=_("the `sales number` of the content."),
        default=0,
    )

User = get_user_model()

class rateModel(models.Model):

    content = models.ForeignKey(
        verbose_name=_("content"),
        help_text=_("content"),
        to=contentModel,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        verbose_name=_("user"),
        to=User,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    rate = models.PositiveIntegerField(
        verbose_name=_("rate"),
        default=0,
        validators=[
            MaxValueValidator(5),
        ]
    )
