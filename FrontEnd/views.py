# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def login(res):
	return render(res, "index.html", {})

def select(res):
	return render(res, "select.html", {})

def manifest(res):
	return render(res, "manifest.json", {})