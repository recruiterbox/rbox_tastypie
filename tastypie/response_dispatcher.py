from tastypie import http
from django.http import HttpResponse
from django.utils.cache import patch_cache_control
from tastypie import response_router
from django.core.handlers.wsgi import WSGIRequest


class HttpResponseDispatcher(object):
    def get_unauthorized_request_response_wsgirequest(self):
        return http.HttpUnauthorized()        
            
    def get_application_error_class(self):
        return http.HttpApplicationError

    def get_response_notfound_class(self):
        return http.HttpResponseNotFound

    def get_unauthorized_response_class(self):
        return http.HttpUnauthorized

    def handle_cache_control(self, request, response):    
        if request.is_ajax() and not response.has_header("Cache-Control"):
            # IE excessively caches XMLHttpRequests, so we're disabling
            # the browser cache here.
            # See http://www.enhanceie.com/ie/bugs.asp for details.
            patch_cache_control(response, no_cache=True)

        return response

    def get_default_response_class(self):
        return HttpResponse

    def create_response(self, content, response_class=HttpResponse, content_type=None, **response_kwargs):
        return response_class(content=content, content_type=content_type,**response_kwargs)

    def get_created_response_class(self):
        return http.HttpCreated

    def get_no_content_response(self):
        return http.HttpNoContent()

    def get_not_found_response(self):
        return http.HttpNotFound()

    def get_multiple_choices_response(self, content):
        return http.HttpMultipleChoices(content)

    def get_accepted_response_class(self):
        return http.HttpAccepted

    def get_bad_request_response(self, content):
        return http.HttpBadRequest(content=content)

    def get_method_notallowed_response(self, content):
        return http.HttpMethodNotAllowed(content)

    def get_too_many_request_response(self):
        return http.HttpTooManyRequests()

    def get_created_response(self, location):
        return http.HttpCreated(location=location)

    def get_not_implemented_response(self):
        return http.HttpNotImplemented()

response_router[WSGIRequest] = HttpResponseDispatcher()