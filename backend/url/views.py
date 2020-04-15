import requests
from rest_framework import views, response
from .serializers import UrlSerializer
import concurrent.futures


def get_status_code(url):
    try:
        r = requests.get(url, timeout=10)
        status_code = r.status_code
    except requests.RequestException:
        status_code = 500
    return status_code


class UrlView(views.APIView):
    def get(self, request):
        user = request.user
        urls = user.urls.all()
        result = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_url_model = {executor.submit(get_status_code, url.url): url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url_model):
                url_model = future_to_url_model[future]
                status_code = future.result()
                url_data = UrlSerializer(instance=url_model).data
                url_data['status_code'] = status_code
                result.append(url_data)
        return response.Response(result)

