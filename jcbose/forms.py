from django import forms
from .models import Post

class ProfileForm(forms.ModelForm):
	post = forms.CharField(label='Post', max_length=100)
	Name = forms.CharField(label='Name', max_length=100)
	Fathers_name = forms.CharField(label='Father\'s name', max_length=100)
	Mothers_name = forms.CharField(label='Mother\'s name', max_length=100)
	Mobile_no = forms.IntegerField(label='Mobile no.')
	# Email_id = forms.EmailField()
	Resedential_adress=forms.CharField(label='Address', max_length=100)


# class NameForm(forms.ModelForm):
# 	post = forms.CharField()
# 	Name = forms.CharField()
# 	Fathers_name = forms.CharField()
# 	Mothers_name = forms.CharField()
# 	Mobile_no = forms.IntegerField()
# 	Email_id = forms.EmailField()
# 	Resedential_adress=forms.CharField()

# class SchoolDetails(forms.ModelForm):
# 	Name_of_the_school = forms.CharField()
# 	Address_of_school = forms.CharField()
# 	School_Contach_number = forms.IntegerField()
# 	School_Email_address = forms.EmailField()

# class Description(forms.ModelForm):

# 	Title_of_the_Innovation = forms.CharField()

# 	Incurred_cost_in_making_the_model_or_expected_cost_in_development_of_the_prototype = forms.CharField()

# 	Have_you_applied_for_the_patent_earlier_for_this_innovation_If_your_answer_is_yes_then_provide_the_brief_details = forms.CharField()

# 	Have_you_informed_to_any_other_organisation_about_your_innovative_model_or_presented_your_model_in_any_other_national_or_international_competition__or_innovation_exhibition_If_your_answer_is_yes_then_attach_the_relevant_details_along_with_application= forms.CharField()

# 	Idea_behind_the_Innovation_or_Genesis_of_the_innovation = forms.CharField()

# 	Applicability_and_utility_of_the_innovation = forms.CharField()

# 	How_this_innovative_model_solving_the_local_problem_Specify= forms.CharField()

# 	Commercial_application_or_utility_of_your_innovative_model= forms.CharField()

# 	Please_attach_the_relevant_drawing_or_sketch_with_proper_technical_terms=forms.FileField()

# 	Any_other_suggestions_or_recommendation_which_you_want_to_deliver_about_your_innovation:forms.CharField()

