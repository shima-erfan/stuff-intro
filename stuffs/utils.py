from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateStuffs(request, stuffs, results):
    page      = request.GET.get('page')
    paginator = Paginator(stuffs, results)

    try:
        stuffs = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        stuffs = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        stuffs = paginator.page(page)

    leftIndex = int(page) - 3
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = int(page) + 4
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    custom_range = range(leftIndex, rightIndex)

    return custom_range, stuffs
