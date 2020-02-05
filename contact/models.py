from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from wagtail.images.edit_handlers import ImageChooserPanel
class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
        )
class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"

    intro = RichTextField(blank=True)
    summary = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    head_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel("head_image"),
        FieldPanel('intro'),
        FieldPanel('summary'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
         FieldPanel("subject"),
        ], heading="Email Settings"),       
    ]