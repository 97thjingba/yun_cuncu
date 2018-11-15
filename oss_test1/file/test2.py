from django.http import StreamingHttpResponse
def download_file(request):
    def file_iterator(file, chunk_size=512):
        with open(file) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    file = "/static/img/alin.jpg"
    response = StreamingHttpResponse(file_iterator(file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
    return response