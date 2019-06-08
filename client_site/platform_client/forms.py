from django import forms

class platform_form(forms.Form):
    """
    Form for collecting basic information about an external learning platforms.

    This model contains basic platform metadata such as an ID, name,
    URL, and any other information that would be necessary to
    a courses as part of there system.
    """

    # External Lerning platform information
    org = forms.CharField(required=True)
    thirdparty_platform_name = forms.CharField(required=True)
    
    # URLs
    ServerUrl = forms.CharField(required=True)
    
    # Enrollment details
    integrationstart = forms.DateTimeField(required=True)
    integrationend = forms.DateTimeField(required=True)
    #Date Time Format : 2006-10-25 14:30:59

    # Status details
    isactive = forms.BooleanField(required=True)
    #isactive = True
    # about
    short_description = forms.CharField(required=True)