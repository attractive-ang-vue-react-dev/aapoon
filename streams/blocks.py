from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class HomeCard(blocks.StructBlock):
    # Title and text and nothing else.
    
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = "streams/home_card.html"
        icon = "edit"
        label = "Title & Text"
class HomeImageSlide(blocks.StructBlock):
    #Homepage image slide section
    title = blocks.CharBlock(required=True, help_text='Add your title')
    subtitle = blocks.TextBlock(required=True, help_text='Add additional text')
    image = ImageChooserBlock(required=True, help_text='Upload slide image')
    class Meta:
        template = "streams/home_slide.html"
        icon = "edit"
        label = "Image & text"