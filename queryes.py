import django
import os
from django.db.models import Max, Min, Q

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)

    obj = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
    authors = Author.objects.filter(self_esteem__exact=obj['max_self_esteem'])
    #print(authors)

    obj = Author.objects.aggregate(max_entries=Max('entries'))
    author = Author.objects.get(entries=obj['max_entries'])
    #print(author)

    obj = Entry.objects.filter(Q(tags__name='Кино')|Q(tags__name='Музыка'))
    #print(obj)

    obj = Author.objects.filter(gender='ж').count()
    #print(obj)

    obj = Author.objects.filter(status_rule=True).count()
    total = Author.objects.all().count()
    #print(int(obj/total*100), "%")

    obj = Author.objects.filter(authorprofile__stage__range=(1, 5))
    #print(obj)

    obj = Author.objects.aggregate(max_age=Max('age'))
    author = Author.objects.get(age=obj['max_age'])
    #print(author)

    obj = Author.objects.exclude(phone_number__isnull=True)
    #print(obj)

    obj = Author.objects.filter(age__lt=25)
    #print(obj)

    for auth in Author.objects.all():
        obj = Entry.objects.filter(author=auth).count()
        #print(auth, "написал",obj, "статей")










