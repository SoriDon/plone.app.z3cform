from plone.app.textfield.widget import IRichTextWidget as patextfield_IRichTextWidget
from plone.schema.interfaces import IFormLayer
from z3c.form.interfaces import IRadioWidget as IBaseRadioWidget
from z3c.form.interfaces import ISelectWidget as IBaseSelectWidget
from z3c.form.interfaces import ISingleCheckBoxWidget
from z3c.form.interfaces import ISubmitWidget as IBaseSubmitWidget
from z3c.form.interfaces import ITextAreaWidget as IBaseTextAreaWidget
from z3c.form.interfaces import ITextLinesWidget as IBaseTextLinesWidget
from z3c.form.interfaces import ITextWidget as IBaseTextWidget
from zope.deferredimport import deprecated
from zope.interface import Interface


# this should not be used anymore

deprecated(
    "Use zope.schema.interfaces.IDate instead (will be removed in Plone 7).",
    IDateField="zope.schema.interfaces:IDate",
)

deprecated(
    "Use zope.schema.interfaces.IDatetime instead (will be removed in Plone 7).",
    IDatetimeField="zope.schema.interfaces:IDatetime",
)


class IPloneFormLayer(IFormLayer):
    """Request layer installed via browserlayer.xml"""


class IFieldPermissionChecker(Interface):
    """Adapter factory for checking whether a user has permission to
    edit a specific field on a content object.
    """

    def validate(field_name, vocabulary_name=None):
        """Returns True if the current user has permission to edit the
        `field_name` field.  Returns False if the user does not have
        permission.  Raises and AttributeError if the field cannot be
        found.
        """


class ITextWidget(IBaseTextWidget):
    """Marker interface for base text input"""


class ITextAreaWidget(IBaseTextAreaWidget):
    """Marker interface for base text input"""


class ITextLinesWidget(IBaseTextLinesWidget):
    """Marker interface for base text input"""


class IDateWidget(ITextWidget):
    """Marker interface for the DateWidget."""


class IDatetimeWidget(ITextWidget):
    """Marker interface for the DatetimeWidget."""


class ITimeWidget(ITextWidget):
    """Marker interface for the TimeWidget"""


class ISelectWidget(IBaseSelectWidget):
    """Marker interface for the SelectWidget."""


class IAjaxSelectWidget(ITextWidget):
    """Marker interface for the Select2Widget."""


class IQueryStringWidget(ITextWidget):
    """Marker interface for the QueryStringWidget."""


class IRelatedItemsWidget(ITextWidget):
    """Marker interface for the RelatedItemsWidget."""


class IRichTextWidget(patextfield_IRichTextWidget):
    """Marker interface for the TinyMCEWidget."""


class ILinkWidget(ITextWidget):
    """Marker interface for the enhanced link widget."""


class IEmailWidget(ITextWidget):
    """Marker interface for the dumb email widget."""


class ISubmitWidget(IBaseSubmitWidget):
    """Marker interface for SubmitWidget."""


class ISingleCheckBoxBoolWidget(ISingleCheckBoxWidget):
    """Marker interface for the SingleCheckboxBoolWidget."""


class IRadioWidget(IBaseRadioWidget):
    """Radio widget."""

    def renderForValue(value):
        """Render a single radio button element for a given value.

        Here the word ``value`` is used in the HTML sense, in other
        words it is a term token.
        """


class IRichTextWidgetInputModeRenderer(Interface):
    """Marker interface to render multiple wysiwyg editors"""
