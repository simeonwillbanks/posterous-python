# Copyright:
#    Copyright (c) 2010, Benjamin Reitzammer <http://github.com/nureineide>, 
#    All rights reserved.
#            
# License:
#    This program is free software. You can distribute/modify this program under
#    the terms of the Apache License Version 2.0 available at 
#    http://www.apache.org/licenses/LICENSE-2.0.txt 


class ResultSet(list):
    """ A list like object that holds results from a Posterous API query. """


class Model(object):
    """ Base class """
    def __init__(self, api=None):
        self._api = api


class Post(Model):
    @classmethod
    def parse(self, api, json):
        post = self(api)

    @classmethod
    def parse_list(self, api, json_list):
        return None

    def update(self, **kwargs):
        pass


class Site(Model):
    @classmethod
    def parse(self, api, json):
        site = self(api)       

    @classmethod
    def parse_list(self, api, json_list):
        return None

    
class Comment(Model):
    @classmethod
    def parse(self, api, json):
        comment = self(api)


class Tag(Model):
    @classmethod
    def parse(self, api, json):
        tag = self(api)

    @classmethod
    def parse_list(self, api, json_list):
        return None


class Media(Model):
    @classmethod
    def parse(self, api, json):
        media = self(api)


class JSONModel(Model):
    @classmethod
    def parse(self, api, json):
        return json


class ModelFactory(object):
    """
    Used by parsers for creating instances of models. 
    """
    post = Post
    site = Site
    comment = Comment
    tag = Tag
    media = Media
    json = JSONModel
