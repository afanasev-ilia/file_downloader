# def poster(request):
#     my_file = request.data['file']
#     file_path = 'media/files/' + request.data['file'].name
#     with open(file_path, 'wb+') as temp_file:
#         for chunk in my_file.chunks():
#             temp_file.write(chunk)
#     return file_path


# def poster(self, request):
#     my_file = request.FILES['file']
#     filename = 'media/files/' + my_file.name
#     with open(filename, 'wb+') as temp_file:
#         for chunk in my_file.chunks():
#             temp_file.write(chunk)
#     return Response(
#            status=status.HTTP_201_CREATED
#     )
