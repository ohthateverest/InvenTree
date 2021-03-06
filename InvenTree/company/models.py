"""
Company database model definitions
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from django.urls import reverse


def rename_company_image(instance, filename):
    """ Function to rename a company image after upload

    Args:
        instance: Company object
        filename: uploaded image filename

    Returns:
        New image filename
    """

    base = 'company_images'

    if filename.count('.') > 0:
        ext = filename.split('.')[-1]
    else:
        ext = ''

    fn = 'company_{pk}_img'.format(pk=instance.pk)

    if ext:
        fn += '.' + ext

    return os.path.join(base, fn)


class Company(models.Model):
    """ A Company object represents an external company.
    It may be a supplier or a customer (or both).
    """

    name = models.CharField(max_length=100, unique=True,
                            help_text='Company name')

    description = models.CharField(max_length=500)

    website = models.URLField(blank=True, help_text='Company website URL')

    address = models.CharField(max_length=200,
                               blank=True, help_text='Company address')

    phone = models.CharField(max_length=50,
                             blank=True)

    email = models.EmailField(blank=True)

    contact = models.CharField(max_length=100,
                               blank=True)

    URL = models.URLField(blank=True, help_text='Link to external company information')

    image = models.ImageField(upload_to=rename_company_image, max_length=255, null=True, blank=True)

    notes = models.TextField(blank=True)

    is_customer = models.BooleanField(default=False)

    is_supplier = models.BooleanField(default=True)

    def __str__(self):
        """ Get string representation of a Company """
        return "{n} - {d}".format(n=self.name, d=self.description)

    def get_absolute_url(self):
        """ Get the web URL for the detail view for this Company """
        return reverse('company-detail', kwargs={'pk': self.id})

    @property
    def part_count(self):
        """ The number of parts supplied by this company """
        return self.parts.count()

    @property
    def has_parts(self):
        """ Return True if this company supplies any parts """
        return self.part_count > 0


class Contact(models.Model):
    """ A Contact represents a person who works at a particular company.
    A Company may have zero or more associated Contact objects
    """

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=100, blank=True)

    email = models.EmailField(blank=True)

    role = models.CharField(max_length=100, blank=True)

    company = models.ForeignKey(Company, related_name='contacts',
                                on_delete=models.CASCADE)
