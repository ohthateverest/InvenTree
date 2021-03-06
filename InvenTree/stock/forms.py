"""
Django Forms for interacting with Stock app
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from InvenTree.forms import HelperForm

from .models import StockLocation, StockItem


class EditStockLocationForm(HelperForm):
    """ Form for editing a StockLocation """

    class Meta:
        model = StockLocation
        fields = [
            'name',
            'parent',
            'description'
        ]


class CreateStockItemForm(HelperForm):
    """ Form for creating a new StockItem """

    class Meta:
        model = StockItem
        fields = [
            'part',
            'supplier_part',
            'location',
            'belongs_to',
            'serial',
            'batch',
            'quantity',
            'status',
            'notes',
            # 'customer',
            'URL',
        ]


class MoveStockItemForm(forms.ModelForm):
    """ Form for moving a StockItem to a new location """

    note = forms.CharField(label='Notes', required=True, help_text='Add note (required)')

    class Meta:
        model = StockItem

        fields = [
            'location',
        ]


class StocktakeForm(forms.ModelForm):

    class Meta:
        model = StockItem

        fields = [
            'quantity',
        ]


class EditStockItemForm(HelperForm):
    """ Form for editing a StockItem object """

    class Meta:
        model = StockItem

        fields = [
            'supplier_part',
            'batch',
            'status',
            'notes',
            'URL',
        ]
