#-*- coding:utf-8 -*-


def make_app():

    return application


def application(environ, start_response):

    start_response('200 OK', [])

    return ['hello, world']
