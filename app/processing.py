from django.contrib.auth.decorators import login_required
from app.models import Giaovien

def get_teach_name(request):
    teach_name = None
    if request.user.is_authenticated:
        try:
            giaovien = Giaovien.objects.get(magv=request.user)
            teach_name = giaovien.tengv.strip()
        except Giaovien.DoesNotExist:
            pass

    return {'teach_name': teach_name}
