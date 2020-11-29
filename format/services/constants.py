from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

class HeaderConstants:
    FONT_SIZE = Pt(14)
    FONT_NAME = 'Times New Roman'
    ALIGNMENT = WD_PARAGRAPH_ALIGNMENT.CENTER
    FONT_COLOR = RGBColor(0, 0, 0)
    LINE_SPACING = 1.5
    SPACING_AFTER = Pt(12)
    SPACING_BEFORE = Pt(0)
    

class TextConstants:
    ALIGNMENT = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
    LINE_SPACING = 1.5
    FIRST_LINE_INDENT = Mm(12.5)
    FONT_COLOR = RGBColor(0, 0, 0)
    FONT_SIZE = Pt(14)
    FONT_NAME = 'Times New Roman'
    SPACING_AFTER = Pt(0)

class PageConstants:
    MARGIN_TOP = Mm(20)
    MARGIN_LEFT = Mm(30)
    MARGIN_BOTTOM = Mm(20)
    MARGIN_RIGHT = Mm(10)

class ImageConstants:
    ALIGNMENT = WD_PARAGRAPH_ALIGNMENT.CENTER
    FIRST_LINE_INDENT = Mm(0)

class ImageCaptionConstants(ImageConstants):
    FONT_COLOR = RGBColor(0, 0, 0)
    FONT_SIZE = Pt(14)
    FONT_NAME = 'Times New Roman'
    SPACING_AFTER = Pt(0)
    
class ListConstants(TextConstants):
    LEFT_INDENT = Mm(0)
    FIRST_LINE_INDENT = Mm(0)

class StyleNameConstants:
    TEXT_STYLE = '3bb199dc-d4da-419e-803e-50220ffad537'
    NUMBER_LIST_STYLE = 'feefd279-f760-4f99-bf84-e17287171049'
    BULLET_LIST_STYLE = 'd6a4bbcb-7195-4ebe-9065-89679ce9dc73'
    HEADER_STYLE = 'c2441105-ee4d-4f28-85ec-295e5b95de61'
    IMAGE_STYLE = '01029261-cb3b-4e98-844c-aae1131ed2b6'
    IMAGE_CAPTION_STYLE = '64491bd9-5b36-418a-965e-9e97299d1d31'
