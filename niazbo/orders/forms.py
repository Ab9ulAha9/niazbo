from django import forms
from .models import orders

class order_form(forms.ModelForm):
    class Meta:
        model = orders
        fields = ['name', 'email', 'phone_number', 'address', 'division']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 rounded-xl border border-gray-300 bg-white text-gray-800 placeholder-gray-400 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-200'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full px-4 py-2 rounded-xl border border-gray-300 bg-white text-gray-800 placeholder-gray-400 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-200'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 rounded-xl border border-gray-300 bg-white text-gray-800 placeholder-gray-400 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-200'
            }),
            'address': forms.Textarea(attrs={
                'class': 'block w-full px-4 py-2 rounded-xl border border-gray-300 bg-white text-gray-800 placeholder-gray-400 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-200 resize-none',
                'rows': 3
            }),
            'division': forms.Select(attrs={
                'class': 'block w-full px-4 py-2 rounded-xl border border-gray-300 bg-white text-gray-800 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-200'
            }),
        }
