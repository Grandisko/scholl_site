# from django.http import HttpResponse
#
# class BoatLoadMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         if request.user.is_manager:
#             boat_load = Boat.objects.get(current_load__lt=50).count()
#             if boat_load > 0:
#                 return HttpResponse('Low boat load notification')
#         return response