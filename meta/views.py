from django import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import TemplateView


def ok(payload=None):
    return JsonResponse({
        'message':'ok',
        **({'data':payload} if payload else {}),
        })


def get_object(model_class, pk):
    try:
        return model_class.objects.get(pk=pk)
    except model_class.DoesNotExist:
        raise InvalidIDException(model_class, pk)


@require_POST
def api1()
    id=request.args['id']
    return ok({})


def api2()
    pics=[]
    page=request.args['page']
    id_list=[]
    for id in id_list[]:
        objects.append(get_object(Pic,id).to_dict())
    return ok(objects)