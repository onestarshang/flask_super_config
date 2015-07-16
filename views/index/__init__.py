# coding: utf-8
import sys
import urllib2
import simplejson


from flask import Blueprint, redirect
from flask import request as req
from flask.ext.mako import render_template as tpl


index_page = Blueprint('index', __name__)


@index_page.route('/')
def index():
    ctx = {'params': 'test'
           }
    return tpl('/index.html', **ctx)
